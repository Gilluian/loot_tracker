import psycopg2


class LootTracker:
    def __init__(self, db_config, schema_path):
        self.db_config = db_config
        self.schema_path = schema_path
        self.conn = None

        try:
            self.conn = psycopg2.connect(**self.db_config)
            print("Database connection established.")
        except psycopg2.OperationalError as e:
            error = str(e)
            if 'does not exist' in error and self.db_config['dbname'] in error:
                self.create_initial_database()
                self.conn = psycopg2.connect(**self.db_config)
                self.create_initial_tables(self.conn, self.schema_path)
            else:
                print(f"Operational error connecting to database: {e}")
            
        # except Exception as e:
        #     print(f"1 Error connecting to database: {e}")

    def __del__(self):
        if self.conn:
            self.conn.close()
            print("Database connection closed.")

    def create_initial_database(self):
        # Create the database
        try:
            self.conn=psycopg2.connect(dbname='postgres',user=self.db_config['user'],password=self.db_config['password'],host='localhost',port=self.db_config['port'])
            self.conn.autocommit=True

            with self.conn.cursor() as cursor:
                cursor.execute(f"CREATE DATABASE {self.db_config['dbname']}")
            print(f"Database {self.db_config['dbname']} created successfully.")
            self.conn.close()
        except Exception as e:
            print(f"2 Error connecting to database: {e}")

        

    def create_initial_tables(self, conn, schema_path):
        # Create the initial tables
        with open(schema_path, 'r') as f:
            sql = f.read()
        with conn.cursor() as cur:
            cur.execute(sql)
            conn.commit()
        print("Initial tables created successfully.")
