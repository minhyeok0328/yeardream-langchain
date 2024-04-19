import os
from core.db import SqliteStore

SQL_FILE_PATH = os.path.abspath('./sql/create_table.sql')

def setting():
    try:
        store = SqliteStore(sql_file_path=SQL_FILE_PATH)
        print(store)

    except Exception as e:
        print(f'Database Connect Error: {e}')