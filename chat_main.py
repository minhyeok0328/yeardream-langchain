import os
from core.chat import Chat

def main():
    if 'GOOGLE_API_KEY' not in os.environ:
        os.environ['GOOGLE_API_KEY'] = 'API_KEY'

    chat = Chat()
    while True:
        prompt = input('Prompt here: ')
        response = chat.generate_response(prompt)

        if prompt.lower() in ['exit', 'bye']:
            print('Bye~~')
            break

        print(response)

if __name__ == "__main__":
    main()
