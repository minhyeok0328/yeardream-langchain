from typing import List
from langchain_core.documents.base import Document
from langchain_community.vectorstores.faiss import FAISS
from langchain_community.embeddings.huggingface import HuggingFaceEmbeddings
from core.abstract import VS

MODEL_NAME = "all-MiniLM-L6-v2"

class FaissVectorStore(VS):
    def __init__(self, document:List[Document] = []):
        super().__init__(document=document)
        
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