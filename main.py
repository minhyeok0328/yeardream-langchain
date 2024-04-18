import os
from chatting import excute_chatting
from core.config import API_KEY

def main():
    if 'GOOGLE_API_KEY' not in os.environ:
        os.environ['GOOGLE_API_KEY'] = API_KEY['GEMINI']
    
    excute_chatting()

if __name__ == '__main__':
    main()
