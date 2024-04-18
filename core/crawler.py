from typing import List
from langchain.document_loaders.pdf import PyPDFLoader
from langchain_core.documents.base import Document
 
class Crawler:
    def __init__(self, pdf_file_path: str):
        self.pdf_file_path = pdf_file_path

    def get_pdf_document(self) -> List[Document]:
        try:
            return PyPDFLoader(self.pdf_file_path).load()
        except Exception as e:
            print(f'An error occurred while reading the pdf file. \n {e}')
