from abc import ABC, abstractmethod
from typing import List
from langchain_core.documents.base import Document

class Store:
    @abstractmethod
    def add_document(self, new_document: List[Document]):
        pass

    @abstractmethod
    def query(self, text: str, k: int) -> str:
        pass