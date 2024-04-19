from typing import Union, Type
from core.models import Gemini
from core import Retriever

class Chat:
    # 모델 새로 추가될 때 model Type 하나 씩 추가
    # ex) model: Union[Type[Gemini], Type[Claude]]
    def __init__(self, model: Union[Type[Gemini]], system_prompt: str, retriever: Type[Retriever], temperature: float = 0.0):
        self.retriever = retriever
        self.model = model(
            system_prompt=system_prompt,
            temperature=temperature
        )

    def ask(self, input_prompt: str) -> str:
        knowledge_content = self.retriever.find_related_knowledge(input_prompt)

        return self.model.generate_response(f'{knowledge_content}\n {input_prompt}')
