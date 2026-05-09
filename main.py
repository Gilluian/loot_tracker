import os
from dotenv import load_dotenv
from db_funcs import LootTracker

load_dotenv()

def main():
    # Collects the database config values from the env file.
    db_config = {
        'dbname': os.getenv('DB_NAME'),
        'user': os.getenv('DB_USER'),
        'password': os.getenv('DB_PASSWORD'),
        'host': os.getenv('DB_HOST'),
        'port': os.getenv('DB_PORT'),
    }
    schema_path = os.getenv('SCHEMA_PATH')
   
    db = startup(db_config, schema_path)
    run_program()
    cleanup(db)

def startup(cfg, schema_path):
    # initial checks. creates the database tables, creates initial users. 
    return LootTracker(cfg, schema_path)


def run_program():
    print('doing the things...')

    
def cleanup(db):
    del db
    print("Cleaning up...") 
    

    
if __name__ == "__main__":
    main()