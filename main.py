import os
from dotenv import load_dotenv
from db_funcs import LootTracker as lt

load_dotenv()

def main():
    db_config = {
        'dbname': os.getenv('DB_NAME'),
        'user': os.getenv('DB_USER'),
        'password': os.getenv('DB_PASSWORD'),
        'host': os.getenv('DB_HOST'),
        'port': os.getenv('DB_PORT')
    }
    db = lt(db_config)



    startup()
    run_program()
    cleanup(db)

def startup():

    print("Starting the program...")


def run_program():
    print('doing the things...')

    
def cleanup(db):
    del db
    print("Cleaning up...") 
    

    
if __name__ == "__main__":
    main()