from typing import List
from langchain_text_splitters import CharacterTextSplitter
from langchain_chroma import Chroma
from langchain_google_genai.embeddings import GoogleGenerativeAIEmbeddings
from langchain_core.documents.base import Document

MODEL_NAME = 'models/embedding-001'

class VectorStore:
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
