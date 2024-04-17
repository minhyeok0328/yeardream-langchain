#  프로젝트 세팅

 miniconda와 docker 환경설정을 하는 방법

## docker 세팅
프로젝트 최상위 경로에서

1. docker build -t yeardream-langchain .
> Dockerfile에 있는 대로 docker 이미지를 **yeardream-langchain** 이라는 이름이로 새로 생성
2. docker-compose up -d
> docker-compose.yml에 있는 설정대로 docker container를 실행한다
> 이후 vscode로 접속해서 **/app** 경로에서 개발하면 됩니다

## miniconda 환경 세팅
프로젝트 최상위 경로에서

1. conda env create -f environment.yml
> environment.yml에 필요한 것들을 정의해 놓고 위 명령어로 한 번에 설치합니다.
2. conda activate yeardream-langchain