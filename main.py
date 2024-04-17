import os
from core.chat import Chat

def main():
    if 'GOOGLE_API_KEY' not in os.environ:
        os.environ['GOOGLE_API_KEY'] = 'AIzaSyBoYe5WvsNjT7iiUIZCYtKNvg5_L5yIsCc'

    while True:
        chat = Chat()
        prompt = input('Prompt here: ')

        if prompt.lower() in ['exit', 'bye']:
            print('채팅을 종료합니다.')
            break

        response = chat.generate_response(prompt)
        print(response)

if __name__ == "__main__":
    main()
