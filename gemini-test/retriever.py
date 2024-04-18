import os
from langchain_community.document_loaders import WebBaseLoader
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_google_genai.embeddings import GoogleGenerativeAIEmbeddings
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_core.prompts import SystemMessagePromptTemplate, ChatPromptTemplate, MessagesPlaceholder
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_chroma import Chroma
from langchain.document_loaders.pdf import PyPDFLoader

if 'GOOGLE_API_KEY' not in os.environ:
    os.environ['GOOGLE_API_KEY'] = 'AIzaSyB4LUMIRNaneUx29NVSIlL6cliRy14CrdQ'

#loader = WebBaseLoader('https://docs.smith.langchain.com/overview')
#loader = WebBaseLoader('https://www.google.com/search?client=firefox-b-d&q=chat+gpt')
loader = PyPDFLoader("./Chain-of-Thought-prompting.pdf")
text = loader.load()

splitter = RecursiveCharacterTextSplitter(chunk_size=50, chunk_overlap=0)
splits = splitter.split_documents(text)
# print(splits[:2])

vectorDB = Chroma.from_documents(
        documents=splits,
        embedding=GoogleGenerativeAIEmbeddings(model='models/embedding-001')
    )

retriever = vectorDB.as_retriever(k=1)
input_prompt = input('User: ')
response = retriever.invoke(input=input_prompt)
print(response)