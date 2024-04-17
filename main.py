import os
from core.chat import Chat

def main():
    if 'GOOGLE_API_KEY' not in os.environ:
        os.environ['GOOGLE_API_KEY'] = 'AIzaSyBoYe5WvsNjT7iiUIZCYtKNvg5_L5yIsCc'

    chat = Chat()
    prompt = input('Prompt: ')
    response = chat.generate_response(prompt)
    print(response)

if __name__ == "__main__":
    main()
