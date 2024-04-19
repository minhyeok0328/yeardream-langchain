from typing import List
from langchain_core.documents.base import Document
from langchain_text_splitters import CharacterTextSplitter

class TextSplitter:
    def __init__(self, chunk_size: int = 300):
        self.text_splitter = CharacterTextSplitter(chunk_size=chunk_size)

    def split(self, document: str) -> List[Document]:
        return self.text_splitter.split_documents(documents=document)
