from core import Chat, Crawler
from core.models import Gemini
from core.config import SYSTEM_PROMPT

PDF_PATH = '/app/files/Chain-of-Thought-prompting.pdf'

def excute_chatting():
    crawler = Crawler(pdf_file_path=PDF_PATH)
    content = crawler.get_pdf_document()

    chat = Chat(model=Gemini, system_prompt=SYSTEM_PROMPT['QA'], content=content)

    while True:
        prompt = input('Prompt here: ')

        if prompt.lower() in ['exit', 'bye']:
            print('Bye~~')
            break

        response = chat.ask(prompt)
        print(response)
