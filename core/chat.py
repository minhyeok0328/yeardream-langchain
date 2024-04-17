from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import SystemMessage
from langchain.prompts import (
    ChatPromptTemplate,
    MessagesPlaceholder,
    HumanMessagePromptTemplate
)
from langchain.memory import ConversationBufferMemory
from langchain.chains.llm import LLMChain

VARIABLE_NAME = 'chat_history'
CHAT_KEY = 'human_input'
MODEL_NAME = 'models/gemini-1.5-pro-latest'

class Chat:
    def __init__(self, system_prompt: str = '', model: str = MODEL_NAME, temperature: float = 0.0):
        memory = ConversationBufferMemory(memory_key=VARIABLE_NAME, return_messages=True)
        prompt = ChatPromptTemplate.from_messages(
            [
                SystemMessage(
                    content=system_prompt
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
        try:
            return self.llm_chain.predict(human_input=question)
        except Exception as e:
            print('An error has occurred. please try again.', e)
