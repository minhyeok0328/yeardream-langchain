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
