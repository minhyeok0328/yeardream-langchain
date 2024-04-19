import os
from chatting import execute_chatting
from setting import setting
from core.config import API_KEY

def main():
    if 'GOOGLE_API_KEY' not in os.environ:
        os.environ['GOOGLE_API_KEY'] = API_KEY['GEMINI']

    execute_chatting()

if __name__ == '__main__':
    main()
