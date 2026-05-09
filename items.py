# !/usr/bin/env python3
from psycopg2.errors import InvalidTextRepresentation

def insert_item(db, item):
    
    query = '''
            INSERT INTO items (item_id, item_name, item_class, 
                                item_sub_class, item_type, inventory_type, quality, item_level)
                        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
            ON CONFLICT (item_id) DO NOTHING;
            '''
    with db.conn.cursor() as cur:
        try:
            cur.execute(query, item)
        except InvalidTextRepresentation: 
            #TODO [LOOT-21] out of 108539 items, only 103168 could be inserted. 5371 items (5%) could not. Need to fix
            # print(f'Error with {item}, skipping.')
            pass
        db.conn.commit()
