import datetime
import os

class ChatLogger():
    def __init__(self):
        """
        채팅 로그를 저장할 이름을 생성합니다.
        """
        now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        folder_name = "log"
        is_log_folder = os.path.isdir(folder_name)
        #  로그 폴더가 없다면 생성한다.
        if is_log_folder is False:
            os.mkdir("log")
        # 파일 이름은 log/chat_log_현재날짜시분초
        self.filepath = folder_name +"/" + "chat_log_"+ now + ".txt"
        
        
    def input_log(self, is_user:bool,  input:str):
        """
        사용자 입력을 로그 파일에 저장하는 함수 입니다.
        """
        now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open(self.filepath, "+a") as f:
            if is_user is True:
                input_str =now + " | User : " + input
            else:
                input_str =now + " | AI : " + input
            f.write(input_str)
            # 한칸 엔터를 위해 \n 추가함
            f.write("\n")

