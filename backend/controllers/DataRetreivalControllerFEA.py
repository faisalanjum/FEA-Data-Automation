import sys
import pathlib
from typing import List, Union
from db.dbconnect import connect_to_database as db_fea

sys.path.append(str(pathlib.Path(__file__).resolve().parents[1]))

class DataRetreivalControllerFEA:
    """
    A class used to query data from a database.

    Attributes:
        session: a database connection object.
    """

    def __init__(self):
        """Initialize the database connection."""
        self.session = db_fea()

    def query_data(self, mapper, parameter_val=None, parameter="id") -> List[dict]:
        """
        Query data from the database based on a specified parameter.

        Args:
            mapper: a mapper object representing the table to query from.
            parameter_val: a value for the parameter to query on.
            parameter: the name of the parameter to query on (default is "id").

        Returns:
            A list of dictionary objects representing the queried data.
        """
        session = self.session()

        # Query data based on a single parameter value
        if isinstance(parameter_val, str):
            q_res = session.query(mapper).filter(getattr(mapper, parameter) == parameter_val).all()
            return [q.toDict() for q in q_res]

        # Query data based on a list of parameter values
        elif isinstance(parameter_val, list):
            prm = getattr(mapper, parameter)
            q_res = session.query(mapper).filter(prm.in_(parameter_val)).all()
            return [q.toDict() for q in q_res]

        # Query all data if no parameter value is specified
        elif parameter_val is None:
            q_res = session.query(mapper).all()
            return [q.toDict() for q in q_res]

        else:
            raise ValueError("parameter_val must be a string or list")

    def close_session(self):
        """Close the database connection."""
        self.session.close()

    def get_latest_series(self, mapper, parameter_val=None, parameter="id") -> Union[dict, None]:
        """
        Query the latest series of data from the database based on a specified parameter.

        Args:
            mapper: a mapper object representing the table to query from.
            parameter_val: a value for the parameter to query on.
            parameter: the name of the parameter to query on (default is "id").

        Returns:
            A dictionary object representing the latest series of data, or None if no data is found.
        """
        session = self.session()

        # Query the latest series of data based on a single parameter value
        if isinstance(parameter_val, str):
            q_res = session.query(mapper).filter(getattr(mapper, parameter) == parameter_val).order_by(mapper.date.desc()).first()
            return q_res.toDict() if q_res else None

        # Query the latest series of data based on a list of parameter values
        elif isinstance(parameter_val, list):
            prm = getattr(mapper, parameter)
            q_res = session.query(mapper).filter(prm.in_(parameter_val)).order_by(mapper.date.desc()).first()
            return q_res.toDict() if q_res else None

        # Query the latest series of data if no parameter value is specified
        elif parameter_val is None:
            q_res = session.query(mapper).order_by(mapper.date.desc()).first()
            return q_res.toDict() if q_res else None

        else:
            raise ValueError("parameter_val must be a string or list")
