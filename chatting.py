from core import Chat, Crawler, Retriever, ChatLogger
from core.db import VectorStore
from core.utils import TextSplitter
from core.models import Gemini
from core.config import SYSTEM_PROMPT

PDF_PATH = './files/Chain-of-Thought-prompting.pdf'

def execute_chatting():
    logger = ChatLogger()
    crawler = Crawler(pdf_file_path=PDF_PATH)
    text_splitter = TextSplitter()
    content = crawler.get_pdf_document()
    retriever = Retriever(
        db=VectorStore(document=text_splitter.split(content))
    )
    chat = Chat(
        model=Gemini,
        system_prompt=SYSTEM_PROMPT['QA'],
        retriever=retriever
    )

    while True:
        prompt = input('Prompt here: ')

        if prompt.lower() in ['exit', 'bye']:
            print('Bye~~')
            break

        logger.save_log(input=prompt)
        response = chat.ask(prompt)
        logger.save_log(input=response, is_user=False)
        print(response)
