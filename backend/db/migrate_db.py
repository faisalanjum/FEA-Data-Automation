from dbconnect import connect_to_database
from models import  Base

#function to drop/delete the database
def clean_database():
    engine=connect_to_database(get_engine_only=True)
    Base.metadata.drop_all(engine)
    print("database cleaned")


#function to migrate the code
def migrate_models():
    engine=connect_to_database(get_engine_only=True)

    try:
        Base.metadata.create_all(engine)
        print("migrations completed")
    except Exception as e:
        raise e


# clean database tables
# clean_database()
# migrate_models()