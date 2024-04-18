from typing import List
from langchain.document_loaders.pdf import PyPDFLoader
from langchain_core.documents.base import Document
from langchain_text_splitters import CharacterTextSplitter
 
class Crawler:
    def __init__(self, pdf_file_path: str, chunk_size: int = 300):
        self.pdf_file_path = pdf_file_path
        self.text_splitter = CharacterTextSplitter(chunk_size=chunk_size)

    def get_pdf_document(self) -> List[Document]:
        try:
            return PyPDFLoader(self.pdf_file_path).load()
        except Exception as e:
            print(f'An error occurred while reading the pdf file. \n {e}')
