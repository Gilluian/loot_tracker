

def run_sql_file(file_path, db):
    with open(file_path, 'r') as f:
        sql = f.read()
    with db.conn.cursor() as cur:
        cur.execute(sql)
        db.conn.commit()