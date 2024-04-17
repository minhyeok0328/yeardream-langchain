import os
from langchain_community.document_loaders import WebBaseLoader
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_google_genai.embeddings import GoogleGenerativeAIEmbeddings
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_core.prompts import SystemMessagePromptTemplate, ChatPromptTemplate, MessagesPlaceholder
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_chroma import Chroma

class Chat:
    def __init__(self, model: str = 'gemini-pro', temperature: float = 0.0, system_prompt: str = ''):
        self.chat = ChatGoogleGenerativeAI(
            model = model,
            temperature = temperature
        )
        self.system_prompt = ChatPromptTemplate.from_messages(
            [
                ('system', system_prompt),
                MessagesPlaceholder(variable_name='message')
            ]
        )

    def generate_response(self, question):
        chain = self.system_prompt | self.chat
        response = chain.invoke({
            'message': [HumanMessage(question)]
        })

        return response.content


# chat = Chat()
# prompt = input('Prompt: ')
# print(chat.question(prompt))

 