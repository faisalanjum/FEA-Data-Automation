from decimal import Decimal
from msilib.schema import Class
from xmlrpc.client import DateTime
from sqlalchemy import PrimaryKeyConstraint, String, DATETIME, Column, Float
from sqlalchemy import ForeignKey,UniqueConstraint
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import MetaData
from sqlalchemy import inspect
import os
from dotenv import load_dotenv
load_dotenv()
meta_obj=MetaData(schema=os.getenv("POSTGRES_SCHEMA"))

Base=declarative_base(metadata=meta_obj)
# Base.metadata.schema = os.environ["POSTGRES_SCHEMA"]

class Identifiers(Base):
    __tablename__="identifiers"
    
    # u_id=Column(Integer,primary_key=True,autoincrement=True)
    ID = Column(String)
    Name = Column(String)
    Description = Column(String)
    Numerator_Units = Column(String)
    Denominnator_Units = Column(String,nullable=True)
    Aggregation_Rule = Column(String)
    Disaggregation_Rule = Column(String)
    Frequency = Column(String)
    Has_Data = Column(String)
    Is_Primary = Column(String)

    __table_args__ = (PrimaryKeyConstraint('ID', 'Name',"Frequency"),)

    
    def toDict(self):
        return { c.key: getattr(self, c.key) for c in inspect(self).mapper.column_attrs }


class ProductendusequarterlyforecastSeriesList(Base):

    __tablename__="product_end_use_quarterly_forecast_series"
    name=Column(String)
    description=Column(String)
    frequency=Column(String) 
    source =Column(String)
    created_at=Column(String)
    updated_at=Column(String)
    date=Column(String)
    period=Column(Integer)
    value=Column(Float)
    display=Column(String)
    label=Column(String)
    relationship_info=Column(String(100000))
    id=Column(String)
    type=Column(String)
    download_link=Column(String)

    def toDict(self):
        return { c.key: getattr(self, c.key) for c in inspect(self).mapper.column_attrs }

    __table_args__ = (PrimaryKeyConstraint('name', 'id','period','date',"value","frequency","created_at"),)





class ProductcensusbureaumacroeconomyandenduseSeriesList(Base):

    __tablename__="product_census_bureau_macroeconomy_and_enduse_series"
    # u_id=Column(Integer,primary_key=True,autoincrement=True)
    name=Column(String)
    description=Column(String)
    frequency=Column(String) 
    source =Column(String)
    created_at=Column(String)
    updated_at=Column(String)
    date=Column(String)
    period=Column(Integer)
    value=Column(Float)
    display=Column(String)
    label=Column(String)
    relationship_info=Column(String(100000))
    id=Column(String)
    type=Column(String)
    download_link=Column(String)

    def toDict(self):
        return { c.key: getattr(self, c.key) for c in inspect(self).mapper.column_attrs }

    __table_args__ = (PrimaryKeyConstraint('name', 'id','period','date',"value","frequency","created_at"),)




class ProductfederalreserveSeriesList(Base):

    __tablename__="Product_federal_reserve_series"
    # u_id=Column(Integer,primary_key=True,autoincrement=True)
    name=Column(String)
    description=Column(String)
    frequency=Column(String) 
    source =Column(String)
    created_at=Column(String)
    updated_at=Column(String)
    date=Column(String)
    period=Column(Integer)
    value=Column(Float)
    display=Column(String)
    label=Column(String)
    relationship_info=Column(String(100000))
    id=Column(String)
    type=Column(String)
    download_link=Column(String)

    def toDict(self):
        return { c.key: getattr(self, c.key) for c in inspect(self).mapper.column_attrs }

    __table_args__ = (PrimaryKeyConstraint('name', 'id','period','date',"value","frequency","created_at"),)





class ProductlumberquarterlyforecastSeriesList(Base):

    __tablename__="product_lumber_quarterly_forecast_series"
    # u_id=Column(Integer,primary_key=True,autoincrement=True)
    name=Column(String)
    description=Column(String)
    frequency=Column(String) 
    source =Column(String)
    created_at=Column(String)
    updated_at=Column(String)
    date=Column(String)
    period=Column(Integer)
    value=Column(Float)
    display=Column(String)
    label=Column(String)
    relationship_info=Column(String(100000))
    id=Column(String)
    type=Column(String)
    download_link=Column(String)

    def toDict(self):
        return { c.key: getattr(self, c.key) for c in inspect(self).mapper.column_attrs }

    __table_args__ = (PrimaryKeyConstraint('name', 'id','period','date',"value","frequency","created_at"),)

 
class ProductmacroeconomyquarterlyforecastSeriesList(Base):

    __tablename__="product_macro_economy_quarterly_forecast_series"
    # u_id=Column(Integer,primary_key=True,autoincrement=True)
    name=Column(String)
    description=Column(String)
    frequency=Column(String) 
    source =Column(String)
    created_at=Column(String)
    updated_at=Column(String)
    date=Column(String)
    period=Column(Integer)
    value=Column(Float)
    display=Column(String)
    label=Column(String)
    relationship_info=Column(String(100000))
    id=Column(String)
    type=Column(String)
    download_link=Column(String)
    def toDict(self):
        return { c.key: getattr(self, c.key) for c in inspect(self).mapper.column_attrs }

    # __table_

    __table_args__ = (PrimaryKeyConstraint('name', 'id','period','date',"value","frequency","created_at"),)



class ProductmonthlylumberadvisorSeriesList(Base):

    __tablename__="product_monthly_lumber_advisor_series"
    # u_id=Column(Integer,primary_key=True,autoincrement=True)
    name=Column(String)
    description=Column(String)
    frequency=Column(String) 
    source =Column(String)
    created_at=Column(String)
    updated_at=Column(String)
    date=Column(String)
    period=Column(Integer)
    value=Column(Float)
    display=Column(String)
    label=Column(String)
    relationship_info=Column(String(100000))
    id=Column(String)
    type=Column(String)
    download_link=Column(String)

    __table_args__ = (PrimaryKeyConstraint('name', 'id','period','date',"value","frequency","created_at"),)



    def toDict(self):
        return { c.key: getattr(self, c.key) for c in inspect(self).mapper.column_attrs }
    


class ProductmonthlymacroeconomicadvisorSeriesList(Base):

    __tablename__="product_monthly_macro_economic_advisor"
    # u_id=Column(Integer,primary_key=True,autoincrement=True)
    name=Column(String)
    description=Column(String)
    frequency=Column(String) 
    source =Column(String)
    created_at=Column(String)
    updated_at=Column(String)
    date=Column(String)
    period=Column(Integer)
    value=Column(Float)
    display=Column(String)
    label=Column(String)
    relationship_info=Column(String(100000))
    id=Column(String)
    type=Column(String)
    download_link=Column(String)

    def toDict(self):
        return { c.key: getattr(self, c.key) for c in inspect(self).mapper.column_attrs }

    __table_args__ = (PrimaryKeyConstraint('name', 'id','period','date',"value","frequency","created_at"),)


class ProductstatcanmacroeconomyandenduseSeriesList(Base):

    __tablename__="product_statcan_macro_economy_and_end_use_series"
    # u_id=Column(Integer,primary_key=True,autoincrement=True)
    name=Column(String)
    description=Column(String)
    frequency=Column(String) 
    source =Column(String)
    created_at=Column(String)
    updated_at=Column(String)
    date=Column(String)
    period=Column(Integer)
    value=Column(Float)
    display=Column(String)
    label=Column(String)
    relationship_info=Column(String(100000))
    id=Column(String)
    type=Column(String)
    download_link=Column(String)

    def toDict(self):
        return { c.key: getattr(self, c.key) for c in inspect(self).mapper.column_attrs }

    __table_args__ = (PrimaryKeyConstraint('name', 'id','period','date',"value","frequency","created_at"),)


class ProductstatcansawmillsSeriesList(Base):

    __tablename__="Product_statcan_sawmills_Series"
    # u_id=Column(Integer,primary_key=True,autoincrement=True)
    name=Column(String)
    description=Column(String)
    frequency=Column(String) 
    source =Column(String)
    created_at=Column(String)
    updated_at=Column(String)
    date=Column(String)
    period=Column(Integer)
    value=Column(Float)
    display=Column(String)
    label=Column(String)
    relationship_info=Column(String(100000))
    id=Column(String)
    type=Column(String)
    download_link=Column(String)

    def toDict(self):
        return { c.key: getattr(self, c.key) for c in inspect(self).mapper.column_attrs }

    __table_args__ = (PrimaryKeyConstraint('name', 'id','period','date',"frequency","created_at"),)
