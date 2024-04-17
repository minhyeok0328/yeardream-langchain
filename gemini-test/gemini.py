import os
from langchain_community.document_loaders import WebBaseLoader
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_google_genai.embeddings import GoogleGenerativeAIEmbeddings
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_core.prompts import SystemMessagePromptTemplate, ChatPromptTemplate, MessagesPlaceholder
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_chroma import Chroma

if 'GOOGLE_API_KEY' not in os.environ:
    os.environ['GOOGLE_API_KEY'] = 'API_KEY'

chat = ChatGoogleGenerativeAI(model='gemini-pro', temperature=0)
prompt = ChatPromptTemplate.from_messages(
    [
        ('system', 'Answer only yes or no.'),
        MessagesPlaceholder(variable_name='message')
    ]
)

chain = prompt | chat 
response = chain.invoke(
    {'message': [HumanMessage('Is apple fruit?')]}
)
print(response.content)