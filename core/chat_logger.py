import datetime
import os

FOLDER_NAME = 'log'

class ChatLogger():
    def __init__(self):
        """
        채팅 로그를 저장할 이름을 생성합니다.
        """
        now = datetime.datetime.now()
        self.timestamp = now.strftime("%Y-%m-%d %H:%M:%S")
        os.makedirs(FOLDER_NAME, exist_ok=True)  

        # 파일 이름은 log/chat_log_현재날짜시분초
        self.filepath = f'{FOLDER_NAME}/chat_log_{self.timestamp}.txt'

    def save_log(self, is_user: bool, input: str):
        """
        사용자 입력을 로그 파일에 저장하는 함수 입니다.
        """
        with open(self.filepath, "+a") as f:
            input_str = f"{self.timestamp} | {'User:' if is_user is True else 'AI:'} {input} \n"
            f.write(input_str)
