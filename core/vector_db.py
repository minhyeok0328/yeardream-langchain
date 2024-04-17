
from langchain_chroma import Chroma
from typing import List
from langchain_core.documents.base import Document
from langchain_core.vectorstores import VectorStoreRetriever
from langchain_google_genai.embeddings import GoogleGenerativeAIEmbeddings

class VectorDB():
    def __init__(self) -> None:
        """
        생성자. Chroma, 문서 리스트, VectorStoreRetriever 를 멤버변수로 선언합니다.
        """
        self.documents : List[Document] = [] 
        self.vectorDB : Chroma = None
        self.retriever : VectorStoreRetriever = None

    def append_documents(self, data:List[Document] | Document):
        """
        벡터 디비의 도큐먼트를 저장 합니다.
            1. 만약 None 이 들어 온다면 기존 저장되어 있는 문서 데이터는 삭제합니다.
            2. List[Document] | Document 값이 들어온다면 입력한 데이터를 추가 저장합니다.
            3. 이의외 형태의 데이터는 우선 아무작동을 하지 않습니다.
        """
    
        if isinstance(data, Document):
            self.documents.append(data)
        elif isinstance(data, List):
            self.documents.extend(data)

    def delete_documents(self, index:int = None) : 
        """
        클래스가 저장하고 있는 도큐먼트를 삭제합니다.
            1. 인덱스틑 널어서 해당 인덱스의 데이터를 삭제합니다.
            2. None을 넣는다면 전체 데이터를 삭제합니다.
            3. 만약 도큐먼트의 인덱스를 넘은 데이터를 삭제하려고 하면 아무 반응하지 않습니다.
        """
        try:
            if index is not None:
                self.documents.pop(index)
            else:
                self.documents.clear()
        except Exception as e:
            print(e)

    def make_store(self):
        """
        저장되어 있는 데이터를 바탕으로 Chroma를 만듭니다.
            1. 만약 documents 에 아무 값이 없다면 스토어를 생성하지 않습니다.
        """

        if len(self.documents) != 0:
            self.vectorDB = Chroma.from_documents(
                documents=self.documents,
                embedding=GoogleGenerativeAIEmbeddings(model='models/embedding-001')
            )

    def find_document(self, input_str:str, k:int=1):
        """
        입력한 내용을 바탕으로 스토어에서 가장 유사한 데이터의 개수를 가져온다.
            1. 리턴하는 도큐먼트의 값을 넣지 않으면 기본 1로 설정됩니다.
            2. 입력하는 내용은 스트링 형태 입니다.
            3. 멤버변수 vectorDB가 None이라면 None을 리턴합니다.
        """
        if self.vectorDB is not None:
            self.retriever = self.vectorDB.as_retriever(k=k)
            response = self.retriever.invoke(input=input_str)

            return response
        else:
            return None
