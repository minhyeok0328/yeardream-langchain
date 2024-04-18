from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import CharacterTextSplitter
from langchain_chroma import Chroma
from langchain.document_loaders.pdf import PyPDFLoader
from langchain_core.vectorstores import VectorStoreRetriever
from langchain_google_genai.embeddings import GoogleGenerativeAIEmbeddings

MODEL_NAME = 'models/embedding-001'

# 웹 크롤링 대신 pdf를 불러와서 사용
class Vector:
    def __init__(self, file_path: str, chunk_size: int = 500, k: int = 1):
        pdf_document = PyPDFLoader(file_path).load()
        text_splitter = CharacterTextSplitter(chunk_size=chunk_size)
        documents = text_splitter.split_documents(pdf_document)

        self.k = k
        self.__db = Chroma.from_documents(documents, GoogleGenerativeAIEmbeddings(model=MODEL_NAME))

    def query(self, text: str) -> str:
        result = self.__db.similarity_search(query=text, k=self.k)
        return result[0].page_content