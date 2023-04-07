from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os

# Load the environment variables from the .env file
load_dotenv()

def connect_to_database(get_engine_only=False):
    """
    Connect to the database and return a session object.

    Args:
        get_engine_only: if True, only return the engine object.

    Returns:
        A session object or an engine object.
    """
    # Get the database schema from the environment variables
    schema = os.getenv("POSTGRES_SCHEMA_FEA")

    # Create an engine object for the database
    try:
        engine = create_engine(os.environ["DB_URL_FEA"], echo=False, connect_args={"options": "-csearch_path={}".format(schema)})
        
        # Return the engine object if requested
        if get_engine_only:
            return engine
        
        # Create a session object from the engine and return it
        session = sessionmaker(engine, expire_on_commit=False)
        print("Connection Established!")
        return session

    except Exception as e:
        raise ConnectionError("There is some error connecting to the database")
