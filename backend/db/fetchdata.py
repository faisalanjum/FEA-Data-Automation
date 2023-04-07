import sys
import pathlib
sys.path.append(str(pathlib.Path(__file__).resolve().parents[2])) 
from backend.controllers.DataRetreivalController import DataRetreivalController
from models import Identifiers,ProductendusequarterlyforecastSeriesList, ProductstatcanmacroeconomyandenduseSeriesList


def get_identifiers_by_id():

    try:
        data_ret_obj=DataRetreivalController()
        data=data_ret_obj.query_data(ProductendusequarterlyforecastSeriesList,"nE96VX9r",)
        return data

    except Exception as e:
        raise e


def get_statcan_data_by_id():

    try:
        data_ret_obj=DataRetreivalController()
        data=data_ret_obj.query_data(ProductstatcanmacroeconomyandenduseSeriesList,"3l02QegR",)
        return data

    except Exception as e:
        raise e


def get_statcan_data_by_name():

    try:
        data_ret_obj=DataRetreivalController()
        data=data_ret_obj.query_data(ProductstatcanmacroeconomyandenduseSeriesList,"ahef_ca_statcan",'name')
        return data

    except Exception as e:
        raise e


data=get_identifiers_by_id()


data2 = get_statcan_data_by_id()
data3 = get_statcan_data_by_name()


# print(data)
print(data2)
print("-----------------")
print(data3)





