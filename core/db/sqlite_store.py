import sqlite3
from langchain_community.utilities import SQLDatabase

class SqliteStore:
    def __init__(self, sql_file_path: str, store_name: str = 'Langchain', table_name: str = 'documents'):
        try:
            self.sql_file_path = sql_file_path
            self.table_name = table_name
            self.conn = sqlite3.connect(f'{store_name}.db')
            self.cursor = self.conn.cursor()

            self.table_exists()
        except Exception as e:
            print(f'Database connection error: {e}')

    def table_exists(self):
        try:
            self.cursor.execute(f"SELECT name FROM sqlite_master WHERE type='table' AND name='{self.table_name}'")
            is_table_exists = self.cursor.fetchone() is not None

            if not is_table_exists:

                with open(self.sql_file_path, 'r') as f:
                    sql = f.read()

                    self.cursor.execute(sql)
                    self.conn.commit()
                    self.conn.close()

        except Exception as e:
            print(f'An error occurred while creating the table: {e}')