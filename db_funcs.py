import psycopg2


class LootTracker:
    def __init__(self, db_config):
        self.db_config = db_config
        self.conn = None

        try:
            self.conn = psycopg2.connect(**self.db_config)
            print("Database connection established.")
        except Exception as e:
            print(f"Error connecting to database: {e}")

    def __del__(self):
        if self.conn:
            self.conn.close()
            print("Database connection closed.")
