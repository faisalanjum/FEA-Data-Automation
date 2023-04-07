from helpers import fetch_files
import models
import pandas as pd
import sys
import pathlib
from datetime import datetime,timedelta
sys.path.append(str(pathlib.Path(__file__).resolve().parents[2]))
from dbconnect import connect_to_database
from migrate_db import migrate_models,clean_database
from backend.controllers.DataRetreivalControllerFEA import DataRetreivalControllerFEA
from populate import get_series,populate_series,populate_unique_identifiers
import logging
logging.basicConfig(filename='logs/update_cron.log',level=logging.DEBUG)
logger=logging.getLogger(__name__)
 

# fetches the unique identifiers from excel files
def update_series(directory,subdir,extnsn):

    excel_files=fetch_files(dir_name=directory,sub_dir_name=subdir,extension_type=extnsn)
    for f in excel_files[:9]:
        name=str(f).split("\\")
        name=str(name[-1]).split(".")
        name=name[0].replace("-","")

        model_mapper=getattr(models,name)
        data=pd.read_excel(f)
        groups=data.groupby('Frequency').agg(lambda x: list(x))
        for row_index, row in groups.iterrows():
            get_updated_data(model_mapper,str(row_index),row["ID"])



#funtion to check the last date of if the series and request data 

def get_updated_data(model_mapper,frequency,series):
    sessn=connect_to_database()
    db_ssn=sessn()

    for item in series:
        try:
            controller_obj=DataRetreivalControllerFEA()
            data=controller_obj.get_latest_series(model_mapper,item)
            if data:
                increment_dict={"w":7,"m":31,"q":94,"a":366}
                
               
                print('data gathering initialized for series {} frequency {}'.format(item,frequency))
            
                date=(datetime.strptime(data["date"], '%Y-%m-%d') + timedelta(days=increment_dict[frequency])).strftime('%Y-%m-%d')
                print(date)
                
                get_series(db_ssn,mapper=model_mapper,frequency=frequency,start_date=date,series=item,date_to_compare=data["date"])
        except Exception as e :
            raise e

if __name__ == "__main__":


    # clean the database
    try:
        logger.info("Cleaning database")
        clean_database()
        logger.info("Database cleaned")
    except Exception as e:
        logger.error("Error cleaning database{}".format(e))
        



    # migrate the models
    try:
        logger.info("Migrating models")
        migrate_models()
        logger.info("Models migrated")
    except Exception as e:
        logger.error("Error migrating models /n {}".format(e))


    # populate the database
    try:
        logger.info("Populating database")
        populate_unique_identifiers("assets","unique_identifiers",".xlsx")
        
        populate_series(directory="assets",subdir="unique_identifiers",extnsn=".xlsx")
        logger.info("Database populated")
    except Exception as e:
     
       
        logger.error("Error populating database /n {}".format(e))



    
# call to below function will update the data by checking the last date of the series and request data

# update_series("assets","unique_identifiers",".xlsx")

