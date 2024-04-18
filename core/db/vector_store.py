from typing import Iterable, List
from langchain_text_splitters import CharacterTextSplitter
from langchain_chroma import Chroma
from langchain_google_genai.embeddings import GoogleGenerativeAIEmbeddings
from langchain_core.documents.base import Document

MODEL_NAME = 'models/embedding-001'

class VectorStore:
    def __init__(self, chunk_size: int = 500, k: int = 1, content: List[Document] = []):
        self.k = k
        self.text_splitter = CharacterTextSplitter(chunk_size=chunk_size)
        new_document = self.text_splitter.split_documents(content)
        self.__db = Chroma.from_documents(new_document, GoogleGenerativeAIEmbeddings(model=MODEL_NAME))

    def add_document(self, new_document: Iterable[Document]):
        document = self.text_splitter.split_documents(new_document)
        self.__db.add_documents(document)

    def query(self, text: str) -> str:
        result = self.__db.similarity_search(query=text, k=self.k)
        return result[0].page_content
