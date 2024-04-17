import os
from langchain_community.document_loaders import WebBaseLoader
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_google_genai.embeddings import GoogleGenerativeAIEmbeddings
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_core.prompts import SystemMessagePromptTemplate, ChatPromptTemplate, MessagesPlaceholder
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_chroma import Chroma

# API key
if 'GOOGLE_API_KEY' not in os.environ:
    os.environ['GOOGLE_API_KEY'] = 'AIzaSyDz8xBhSaEbgFenLa7ZU6YXhFMG51SGIZQ'

# 'system'. 'human', 'ai' ?
chat = ChatGoogleGenerativeAI(model='gemini-1.5-pro-latest', temperature=1.0)
prompt = ChatPromptTemplate.from_messages(
    [
        ('system', "Answer only 'yes' or 'no'. Don't add any explanation about your answer."),
        MessagesPlaceholder(variable_name='message')
    ]
)

chain = prompt | chat 
input_prompt = input("data call with Gemini, Done.")
response = chain.invoke(
    {'message': [HumanMessage(input_prompt)]}
)
print(response.content)
                                   