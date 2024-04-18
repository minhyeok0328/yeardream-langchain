from typing import Union, Type, List
from core.models import Gemini
from core.db import VectorStore
from langchain_core.documents.base import Document

PDF_PATH = '/app/gemini-test/Chain-of-Thought-prompting.pdf'

class Chat:
    # 모델 새로 추가될 때 model Type 하나 씩 추가
    # ex) model: Union[Type[Gemini], Type[Claude]]
    def __init__(self, model: Union[Type[Gemini]], system_prompt: str, temperature: float = 0.0, content: List[Document] = []):
        self.db = VectorStore(content=content)
        self.model = model(
            system_prompt=system_prompt,
            temperature=temperature
        )

    def ask(self, input_prompt: str) -> str:
        rag_content = self.db.query(input_prompt)

        return self.model.generate_response(rag_content + input_prompt)
