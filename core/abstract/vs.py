from typing import List
from abc import ABC, abstractmethod
from langchain_core.documents.base import Document


class VS(ABC):
    def __init__(self, document:List[Document]):
        pass

    @abstractmethod
    def add_document(self, new_document:List[Document]):
        pass

    @abstractmethod
    def query(self, text:str, k:int) -> str:
        pass
    
   