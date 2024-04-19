from typing import List, Union, Type
from langchain_chroma import Chroma
from langchain_google_genai.embeddings import GoogleGenerativeAIEmbeddings
from langchain_core.documents.base import Document
from langchain_community.vectorstores.faiss import FAISS
from langchain_community.embeddings.huggingface import HuggingFaceEmbeddings

MODEL_NAME = 'models/embedding-001'

class ChromaVectorStore:
    def __init__(self, document: List[Document] = []):
        self.__db = Chroma.from_documents(
            documents=document,
            embedding=GoogleGenerativeAIEmbeddings(model=MODEL_NAME)
        )

    def add_document(self, new_document: List[Document]):
        self.__db.add_documents(new_document)

    def query(self, text: str, k: int = 1) -> str:
        try:
            result = self.__db.similarity_search(query=text, k=k)
            return result[0].page_content
        except Exception as e:
            print(e)


class FaissVectorStore:
    def __init__(self, document:List[Document] = []):
        self.__db = FAISS.from_documents(documents=document, 
                                         embedding=HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2"))

    def add_document(self, new_document:List[Document]):
        self.__db.add_documents(new_document)

    def query(self, text:str, k:int = 1) -> str:
        try:
            result = self.__db.similarity_search(query=text, k=k)
            return result[0].page_content
        except Exception as e:
            print(e)

class VectorStore:
    def __init__(self, db:Union[Type[ChromaVectorStore], Type[FaissVectorStore]], document:List[Document]):
        self.db = db(document=document)

    def add_document(self, new_document:List[Document]):
        self.db.add_document(new_document=new_document)

    def query(self, text:str, k:int=1) -> str:
        return self.db.query(text=text, k=k)