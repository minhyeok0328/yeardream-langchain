from core import Chat
from core.models import Gemini
from core.config import SYSTEM_PROMPT, API_KEY

def excute_chatting():
    chat = Chat(Gemini, SYSTEM_PROMPT['QA'], API_KEY['GEMINI'])

    while True:
        prompt = input('Prompt here: ')
        response = chat.model.ask(prompt)

        if prompt.lower() in ['exit', 'bye']:
            print('Bye~~')
            break

        print(response)
