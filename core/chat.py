from typing import Literal
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage, SystemMessage
from langchain.prompts import (
    ChatPromptTemplate,
    MessagesPlaceholder,
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate,
    PromptTemplate,
)
from langchain.memory import ConversationBufferMemory
from langchain.chains.llm import LLMChain

VARIABLE_NAME = 'chat_history'
CHAT_KEY = 'human_input'

class Chat:
    def __init__(self, system_prompt: str = '', model: str = 'models/gemini-1.5-pro-latest', temperature: float = 0.0):
        memory = ConversationBufferMemory(memory_key=VARIABLE_NAME, return_messages=True, ai_prefix='Gemini')
        prompt = ChatPromptTemplate.from_messages(
            [
                SystemMessage(
                    content='You are a QA Bot that creates answers based on documentation data you collect.'
                ),
                MessagesPlaceholder(
                    variable_name=VARIABLE_NAME
                ),
                HumanMessagePromptTemplate.from_template(
                    '{human_input}'
                )
            ]
        )
        llm = ChatGoogleGenerativeAI(
            model = model,
            temperature = temperature
        )
        self.llm_chain = LLMChain(
            llm=llm,
            prompt=prompt,
            verbose=True,
            memory=memory
        )

    def generate_response(self, question: str) -> str:
        response = self.llm_chain.predict(human_input=question)
        return response
