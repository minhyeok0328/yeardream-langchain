# 프로젝트 목표
 LangChain을 이용해서 Knowledge Base를 구축하고, 이를 응용한 QA Engine을 개발
## 구성
- 개발 언어는 Python을 사용합니다
- Gemini API를 통해 LLM 답변을 받습니다. Gemini만 사용합니다
  
#  프로젝트 세팅

 miniconda와 docker 환경설정을 하는 방법

## docker 세팅
프로젝트 최상위 경로에서

1. docker build -t yeardream-langchain .
> Dockerfile에 있는 대로 docker 이미지를 **yeardream-langchain** 이라는 이름으로 새로 생성
2. docker-compose up -d
> docker-compose.yml에 있는 설정대로 docker container를 실행한다
> 이후 vscode로 접속한 뒤 파일탐색창(Explorer)에서 Open Folder 버튼을 누른 뒤에 **/app** 경로를 열고난 뒤 개발하면 됩니다

## miniconda 환경 세팅
프로젝트 최상위 경로에서
1. conda env create -f environment.yml
> environment.yml에 필요한 것들을 정의해 놓고 위 명령어로 한 번에 설치합니다.
2. conda activate yeardream-langchain

# 프로젝트 설명
## 프로젝트 폴더 트리

```
📦core
 ┣ 📂abstract
 ┃ ┣ 📜__init__.py
 ┃ ┗ 📜lc.py
 ┣ 📂config
 ┃ ┣ 📜__init__.py
 ┃ ┣ 📜api_key.py
 ┃ ┗ 📜prompt.py
 ┣ 📂db
 ┃ ┣ 📜__init__.py
 ┃ ┣ 📜sqlite_store.py
 ┃ ┗ 📜vector_store.py
 ┣ 📂models
 ┃ ┣ 📜__init__.py
 ┃ ┗ 📜gemini.py
 ┣ 📂utils
 ┃ ┣ 📜__init__.py
 ┃ ┗ 📜text_splitter.py
 ┣ 📜__init__.py
 ┣ 📜chat.py
 ┣ 📜chat_logger.py
 ┣ 📜crawler.py
 ┗ 📜retriever.py
📦files
 ┗ 📜chain-of-thought-prompting.pdf
📜.gitignore
📜Dockerfile
📜README.md
📜chatting.py
📜docker-compose.yml
📜environment.yml
📜main.py
```


## 각 폴더/파일 (역할) 설명
- **environment.yml**: miniconda 환경 세팅 파일 입니다.
- **docker-compose.yml, Dockerfile**: 도커 환경 세팅 파일 입니다.
- **chatting.py**: 채팅 프로그램이 시작되는 함수가 있는 파일 입니다.
- **core**: 개발한 모듈들이 들어있는 폴더 입니다.
- **files**: RAG에 사용될 pdf 파일이 있습니다.
- **core/abstract**: 추상 클래스가 있는 폴더 입니다.
- **core/config**: api key, system prompt 등의 변수들이 있는 폴더 입니다.
- **core/db**: RAG에 필요한 데이터를 저장하는 코드가 있는 폴더 입니다.
- **core/models**: 채팅 시 사용할 모델들이 있습니다. 지금은 gemini 하나만 있습니다.
- **core/utils**: text_splitter와 같은 유틸 클래스들이 있는 폴더 입니다.

# 주요 class 설명
- **gemini**: gemini API를 호출하고, response를 받는 역할을 합니다.
- **vector-store**: RAG를 구축하기 위해서 Vector DB에 store하는 역할을 합니다.
- **retriever**: Vector DB에서 사용자 입력과 연관된 Knowledge를 찾는 검색하는 역할을 합니다.
- **crawler**: KB를 구축하는데 필요한 문서 데이터를 수집하는 역할을 합니다.
- **chat**: user input과 LLM answer를 기반으로 답변을 어떻게 생성할지 정하는 역할을 합니다.
- **logger**: 실행되면서 기록되는 내용들을 저장합니다.

# 사용방법
 1. main을 실행 시킵니다.
 2. “Prompt here:” 문장이 나타나면 질문 혹은 요청사항을 입력하고 엔터키를 누릅니다.
 3. Gemini가 해당 내용에 관련하여 답변을 합니다.
 4. Gemini가 답변을 완료 하면 “Prompt here:” 이 다시 나타납니다. 이어서 다시 질문을 하거나 질문을 그만두고 싶다면 “bye” 혹은 “exit” 를 입력하고 엔터키를 누릅니다.
 5. 대화 기록을 보고 싶다면 log 폴더에서 txt 파일을 확인 하실 수 있습니다.
