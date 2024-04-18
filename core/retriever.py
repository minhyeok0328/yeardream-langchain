from typing import List
from core.db import VectorStore
from langchain_core.documents.base import Document
from langchain_text_splitters import CharacterTextSplitter

class Retriever:
    def __init__(self, chunk_size: int = 500, k: int = 1, content: List[Document] = []):
        self.k = k
        self.text_splitter = CharacterTextSplitter(chunk_size=chunk_size)
        init_document = self.text_splitter.split_documents(content)

        self.db = VectorStore(document=init_document)

    def find_related_knowledge(self, user_input: str) -> str:
        related_knowledge = self.db.query(text=user_input)

        return related_knowledge