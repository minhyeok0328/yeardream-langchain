import datetime
import os

FOLDER_PATH = os.path.abspath('./log')
FOLDER_NAME_RULE = '%Y-%m-%d %H'
CHAT_TIME_STAMP = '%Y-%m-%d %H:%M:%S'

class ChatLogger:
    def __init__(self):
        """
        채팅 로그를 저장할 이름을 생성합니다.
        """
        self.now = datetime.datetime.now()
        os.makedirs(FOLDER_PATH, exist_ok=True)  

        # 파일 이름은 log/chat_log_현재날짜시분초
        self.filepath = f'{FOLDER_PATH}/chat_log_{self.now.strftime(FOLDER_NAME_RULE)}.txt'

    def save_log(self, input: str, is_user: bool = True):
        """
        사용자 입력을 로그 파일에 저장하는 함수 입니다.
        """
        with open(self.filepath, 'a') as f:
            input_str = f"{self.now.strftime(CHAT_TIME_STAMP)} | {'User:' if is_user is True else 'AI:'} {input} \n"
            f.write(input_str)
