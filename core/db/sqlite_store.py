from typing import List
from langchain_core.documents.base import Document
from langchain_community.utilities import SQLDatabase

class SqliteStore:
    def __init__(self, sql_file_path: str, document: List[Document] = [], store_name: str = 'Langchain', table_name: str = 'documents'):
        try:
            self.sql_file_path = sql_file_path
            self.table_name = table_name
            self.__db = SQLDatabase.from_uri(f"sqlite:///{store_name}.db")

            self.table_exists()
        except Exception as e:
            print(f'Database connection error: {e}')

    def table_exists(self):
        try:
            is_table_exists = self.__db.run(f"SELECT name FROM sqlite_master WHERE type='table' AND name='{self.table_name}'")

            if not is_table_exists:
                with open(self.sql_file_path, 'r') as f:
                    sql = f.read()
                    self.__db.run(sql)

        except Exception as e:
            print(f'An error occurred while creating the table: {e}')

    def add_document(self, new_document: List[Document]):
        pass

    def query(self, text: str, k: int) -> str:
        pass