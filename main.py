import os
from dotenv import load_dotenv
from db_funcs import LootTracker
import csv
# import items

load_dotenv()

def main():
    # Collects the database config values from the env file.
    db_config = {
        'dbname': os.getenv('DB_NAME'),
        'user': os.getenv('DB_USER'),
        'password': os.getenv('DB_PASSWORD'),
        'host': os.getenv('DB_HOST'),
        'port': int(os.getenv('DB_PORT'))
    }
    schema_path = os.getenv('SCHEMA_PATH')

    db = LootTracker(db_config, schema_path)
    startup(db)
    run_program()
    cleanup(db)

def startup(db):
    # import items

    load_items_to_database(db)

    # import players
    pass

def run_program():
    #print('doing the things...')
    # use requests and hit up softres.it for raider info
    # import loot log
    pass

def cleanup(db):
    # close our database
    del db
    # close requests connections if open

    #print("Cleaning up...") 
    
def load_items_to_database(db):
    from items import insert_item
    item_file_path = 'items.csv' #TODO: make this an env variable
    with open(item_file_path, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        items = list(reader)
        header = items.pop(0)
        header[0] = 'WoW_Item_ID'
    print('Adding items to database...')
    for i in items:
        insert_item(db, i)
    db.conn.commit()



if __name__ == "__main__":
    main()