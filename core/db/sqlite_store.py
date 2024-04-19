import datetime
from typing import List
from langchain_core.documents.base import Document
from langchain_community.utilities import SQLDatabase

from langchain_community.vectorstores import SQLiteVSS
from langchain_community.embeddings.sentence_transformer import (
    SentenceTransformerEmbeddings,
)

MODEL_NAME = 'all-MiniLM-L6-v2'
STORE_NAME = 'Langchain'

class SqliteStore:
    def __init__(self, document: List[Document]):
        texts = self.documents_to_texts(document=document)
        SQLDatabase.from_uri(f"sqlite:///{STORE_NAME}.db")

        self.__db = SQLiteVSS.from_texts(
            texts=texts,
            embedding=SentenceTransformerEmbeddings(model_name=MODEL_NAME),
            table='documents',
            db_file='./Langchain.db'
        )

    def documents_to_texts(self, document: List[Document]):
        return [x.page_content for x in document]

    def add_documents(self, new_document: List[Document]):
        self.__db.add_texts(texts=self.documents_to_texts(new_document))

    def query(self, text: str, k: int = 4) -> str:
        try:
            result = self.__db.similarity_search(query=text, k=k)
            return result[0].page_content
        except Exception as e:
            print(e)