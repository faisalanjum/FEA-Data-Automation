

import requests
import pandas as pd
import sys
import pathlib 
import os
import models
import time
import json
from dotenv import load_dotenv
#load the env variables
load_dotenv()

from dbconnect import connect_to_database
from helpers import fetch_files
from sqlalchemy.exc import IntegrityError



# fetches the unique identifiers from excel files
def populate_unique_identifiers(directory,subdir,extnsn):

    excel_files=fetch_files(dir_name=directory,sub_dir_name=subdir,extension_type=extnsn)
    sessn=connect_to_database()
    db_ssn=sessn()

    dfs=[]

    for f in excel_files[:9]:
        data=pd.read_excel(f)
        data.rename(columns={"Numerator Units":"Numerator_Units","Denominnator Units":"Denominnator_Units","Aggregation Rule":"Aggregation_Rule", "Disaggregation Rule": "Disaggregation_Rule","Has Data":"Has_Data","Is Primary":"Is_Primary"},inplace=True)
        dfs.append(data)

    data=pd.concat(dfs)
    data=data.drop_duplicates(subset=["ID","Frequency"],keep="first")
    insert_into_database(db_ssn,models.Identifiers,data.to_dict(orient="records"))
    print("records added")


# fetches the unique identifiers from excel files
def populate_series(directory,subdir,extnsn,start_date=None,end_date=None):

    excel_files=fetch_files(dir_name=directory,sub_dir_name=subdir,extension_type=extnsn)
    print(excel_files)
    sessn=connect_to_database()
    db_ssn=sessn()
    

    for f in excel_files[:9]:
        print(f)
        dfs=[]
        name=str(f).split("\\")
        print(name[-1])
        name=str(name[-1]).split(".")
        name=name[0].replace("-","")

        model_mapper=getattr(models,name)
        data=pd.read_excel(f)
      
        data=data.drop_duplicates(subset=["ID","Frequency","Name"],keep="first")   
        groups=data.groupby('Frequency').agg(lambda x: list(x))
        for row_index, row in groups.iterrows():
            data_list=get_series(db_ssn,model_mapper,str(row_index),row["ID"],start_date=start_date,end_date=end_date)
            if type(data_list) == list:
                data=pd.concat(data_list)
                data=data.drop_duplicates()
                dfs.append(data)

        data=pd.concat(dfs)
        data=data.drop_duplicates()
        data.to_csv("data.csv")
        insert_into_database(db_ssn,model_mapper,data.to_dict(orient="records"))
        print("records added for file {}".format(name))



#wrapper function to add data iny
def insert_into_database(ssn,mapper,data):
    try:
        ssn.bulk_insert_mappings(mapper,data)   
        ssn.commit()
        print("records added")
        
    except IntegrityError:

        try:
            ssn.rollback()
            ssn.bulk_update_mappings(mapper,data)   
            ssn.commit()
            print("records updated")
        

        except Exception as e:
            print("Record already updated")
            raise e
        




# function to request_data

def request_data(db_ssn,url,mapper,date_to_compare = None):
    r=requests.get(url)

    if r.status_code == 200:
        resp=r.json() 

        data=process(db_ssn,resp,mapper,date_to_compare)
        return data
        

    elif r.status_code == 429:
        print(" rate limit exceeded waiting for 1 secs to call again ")
        time.sleep(1)
        request_data(db_ssn,url,mapper)
        

    else:
        print(f"error{r.status_code} occured" )








# api call to get series data

def get_series(db_ssn,mapper,frequency:str,series,unit:str="Imperial",include:str="[products,units]",start_date=None,end_date=None,date_to_compare=None):
    

    if type(series) == list:
        try:
            api_key=os.environ['API_KEY']
            root_url=os.environ["API_ROOT_URL"]+"/api/clients/series/data"

            data_rec=[]




            for item in series:
                parms="?series[]={}&frequency={}&include={}&api_key={}".format(item,frequency,include,api_key)

                if start_date and end_date:
                    date_parms= "&start_date={}&end_date={}".format(start_date,end_date)
                    parms+=date_parms

                elif start_date and not end_date:
                    date_parms= "&start_date={}".format(start_date)
                    parms+=date_parms

                elif end_date and not start_date:
                    date_parms="&end_date={}".format(end_date)
                    parms+=date_parms

                
                url=root_url+parms
                data=request_data(db_ssn,url,mapper)
                data_rec.append(data)
            return data_rec
                

        except Exception as e:
            raise e

    else:
        try:
            api_key=os.environ['API_KEY']
            root_url=os.environ["API_ROOT_URL"]+"/api/clients/series/data"


            parms="?series[]={}&frequency={}&include={}&api_key={}".format(series,frequency,include,api_key)

            if start_date and end_date:
                date_parms= "&start_date={}&end_date={}".format(start_date,end_date)
                parms+=date_parms

            elif start_date and not end_date:
                date_parms= "&start_date={}".format(start_date)
                parms+=date_parms

            elif end_date and not start_date:
                date_parms="&end_date={}".format(end_date)
                parms+=date_parms

            
            url=root_url+parms

            
            

            data=request_data(db_ssn,url,mapper,date_to_compare)
            return data
            

        except Exception as e:
            raise e




#process data

def process(db_ssn,resp,mapper,date_to_compare):

    series_df=pd.DataFrame.from_dict(resp["data"][0]["attributes"])
    series_df=series_df.join(pd.DataFrame(series_df.pop('data').values.tolist()))
    series_df["meta"]=json.dumps(resp["meta"])
    series_df["id"]=resp["data"][0]["id"]
    series_df["type"]=resp["data"][0]["type"]
    series_df["source"]=resp["meta"]["sources"]
    series_df["download_link"]=resp["links"]["download"]
    relationship_string=json.dumps(resp["data"][0]["relationships"])
    series_df["relationship_info"]=relationship_string
    series_df=series_df.drop_duplicates (keep="first")

    if date_to_compare:
        series_df=series_df[series_df["date"] > date_to_compare]

    if not series_df.empty:

        print("{} data points retreived".format(len(series_df)) )
        return series_df       
    else:
        print("no data avaliable")

#uncomment the below code to populate the unique identifiers data from excel sheets

# populate_unique_identifiers("assets","unique_identifiers",".xlsx")

# below code populates the series data

# start_time = time.time()

# populate_series("assets","unique_identifiers",".xlsx")

# print("--- %s seconds ---" % (time.time() - start_time))
