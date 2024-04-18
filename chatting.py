from core import Chat
from core.models import Gemini
from core.config import SYSTEM_PROMPT

def excute_chatting():
    chat = Chat(model=Gemini, system_prompt=SYSTEM_PROMPT['QA'])

    while True:
        prompt = input('Prompt here: ')

        if prompt.lower() in ['exit', 'bye']:
            print('Bye~~')
            break

        response = chat.ask(prompt)
        print(response)
