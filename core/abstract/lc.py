from abc import ABC, abstractmethod
from typing import Type, Union
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import SystemMessage
from langchain.prompts import (
    ChatPromptTemplate,
    MessagesPlaceholder,
    HumanMessagePromptTemplate
)
from langchain.memory import ConversationBufferMemory
from langchain.chains.llm import LLMChain

class LC(ABC):
    def __init__(self, system_prompt: str, memory_key: str):
        self.system_prompt = system_prompt
        self.first_ask = True
        self.memory = ConversationBufferMemory(memory_key=memory_key, return_messages=True)
        self.prompt = ChatPromptTemplate.from_messages(
            [
                SystemMessage(
                    content=system_prompt
                ),
                MessagesPlaceholder(
                    variable_name=memory_key
                ),
                HumanMessagePromptTemplate.from_template(
                    '{human_input}'
                )
            ]
        )

    # 확장할 때 llm Type 하나 씩 추가
    # ex) llm: Union[Type[ChatGoogleGenerativeAI], Type[OpenAI]]
    def _set_chain(self, llm: Union[Type[ChatGoogleGenerativeAI]]) -> LLMChain:
        return LLMChain(
            llm=llm,
            prompt=self.prompt,
            verbose=False,
            memory=self.memory
        )

    @abstractmethod
    def generate_response(self, question: str) -> str:
        pass
