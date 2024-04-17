from typing import Type
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import SystemMessage
from langchain.prompts import (
    ChatPromptTemplate,
    MessagesPlaceholder,
    HumanMessagePromptTemplate
)
from langchain.memory import ConversationBufferMemory
from langchain.chains.llm import LLMChain

class LC:
    def __init__(self, system_prompt: str, variable_name: str, memory_key: str):
        self.memory = ConversationBufferMemory(memory_key=memory_key, return_messages=True)
        self.prompt = ChatPromptTemplate.from_messages(
            [
                SystemMessage(
                    content=system_prompt
                ),
                MessagesPlaceholder(
                    variable_name=variable_name
                ),
                HumanMessagePromptTemplate.from_template(
                    '{human_input}'
                )
            ]
        )

    # 확장할 때 llm Type 하나 씩 추가
    # ex) llm: Type[ChatGoogleGenerativeAI] | Type[OpenAI]
    def _set_chain(self, llm: Type[ChatGoogleGenerativeAI]) -> LLMChain:
        return LLMChain(
            llm=llm,
            prompt=self.prompt,
            verbose=False,
            memory=self.memory
        )

    def ask(self, question: str) -> str:
        raise NotImplementedError('The ask method must be implemented.')
