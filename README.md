##  📊 유튜브 API를 활용한 카테고리별 유튜버 파급력 데이터 크롤링 및 시각화

<br>

### ✔ 프로젝트 설명
- - -
#### 1. 프로젝트 목적

유튜브 내에서 가장 핫한 카테고리(동물, 영화, 게임, 스포츠, 먹방)와 해당 유튜버들의 구독자 수, 조회 수, 좋아요 수, 댓글 수, 영상의 댓글 등 `유튜브 API에 있는 정보`들을 활용해 파급력을 한눈에 시각화하여 볼 수 있는 웹 페이지 구현한 프로젝트입니다.
<br>

#### 2. 팀원 및 역할 

| 송지혜 | 박재연 | 이소연 | 김선호 | 김지석 |
|---|---|---|---|---|
| - 데이터 분석 <br> - 프론트 & 백엔드 (상세 화면 구현) |  - 데이터 분석 <br> - 프론트 & 백엔드 (메인 화면 구현) | - 데이터 분석, 크롤링 <br> - 데이터 시각화 (Graph) | - 데이터 분석, 크롤링 <br> - 데이터 시각화 (wordCloud) | - 데이터 분석, 크롤링 <br> - DB 구축, 데이터 적재 |

#### 3. 개발 기간
5월 1일 - 5월 5일

#### 4. 기능 및 구현 목록
(1) 메인 화면 
- 각 카테고리 별 총 구독자 순, 총 조회 수 순, 총 좋아요 순 유튜버 순위 산출 
- 각 카테고리의 상위 유튜버 구독자 대비 평균 조회 수와 업로드 빈도율 데이터 시각화 (Graph)
- 각 카테고리별 영상 제목과 댓글에서 가장 많이 언급되는 키워드 시각화 (Word Cloud)
- 각 카테고리별 조회 수 높은 동영상 추출 후 링크 연결

(2) 상세 화면 
- 개인 유튜버의 일별, 주별, 월별 조회 수 대비 좋아요 수 비율과 구독자 대비 조회 수 비율 데이터 시각화 (Graph) 
- 개인 유튜버의 제목, 댓글에서 가장 많이 언급되는 키워드 시각화 (Word Cloud)
- 개인 유튜브 채널의 댓글 좋아요 수가 가장 높은 댓글 추출 후 html 템플릿으로 표출 
- 개인 유튜브 채널의 조회 수가 높은 동영상 추출 후 링크 연결

<br>

###  ✔ 기술 스택
- - -
<strong> 📌 프론트엔드 </strong> 
<br>
<img src="https://img.shields.io/badge/css-1572B6?style=for-the-badge&logo=css3&logoColor=white"> <img src="https://img.shields.io/badge/html-E34F26?style=for-the-badge&logo=html5&logoColor=white">

<strong> 📌 백엔드 </strong>
<br>
<img src="https://img.shields.io/badge/django-092E20?style=for-the-badge&logo=django&logoColor=white"> <img src="https://img.shields.io/badge/python-3776AB?style=for-the-badge&logo=python&logoColor=white"> 

<strong> 📌 데이터베이스 </strong>
<br>
 <img src="https://img.shields.io/badge/amazonaws-232F3E?style=for-the-badge&logo=amazonaws&logoColor=white"> <img src="https://img.shields.io/badge/mysql-4479A1?style=for-the-badge&logo=mysql&logoColor=white"> 

<strong> 📌 형상 관리  </strong>
<br>
<img src="https://img.shields.io/badge/github-181717?style=for-the-badge&logo=github&logoColor=white"> <img src="https://img.shields.io/badge/git-F05032?style=for-the-badge&logo=git&logoColor=white">

<strong> 📌 데이터 분석, 크롤링 및 시각화 </strong>
<br>
<img src="https://img.shields.io/badge/jupyter notebook-F37626?style=for-the-badge&logo=jupyter&logoColor=white"> <img src="https://img.shields.io/badge/python-3776AB?style=for-the-badge&logo=python&logoColor=white"> 

<strong> 📌 그외 협업 도구  </strong>
<br>
<img src="https://img.shields.io/badge/slack-4A154B?style=for-the-badge&logo=slack&logoColor=white"> <img src="https://img.shields.io/badge/Trello-0052CC?style=for-the-badge&logo=Trello&logoColor=white"> 

<br>

###  ✔ 프로젝트 실행 방법
- - -

1. 먼저 프로젝트를 local의 repository로 `git clone` 명령어를 통해 복제합니다. (원본 repository의 주소입니다.)
```
git clone https://github.com/DEVCOURSE-TEAM-04-02/youtubeProject.git
```

2. 이후 프로젝트 폴더로 이동해 줍니다.
```
cd youtube_project
```

3. Django Server로 접속하기 위해서는 먼저 Python의 가상 환경을 만들고, 활성화해 주어야 합니다. 이미 만들어져 있다면 활성화만 해 주면 됩니다.
(project-name은 자유롭게 설정합니다.)
```
python -m venv project-name
project-name\Scripts\activate.bat 
```

4. requirements.txt를 통해 실행에 필요한 패키지를 설치합니다. (cd를 통해 youtube_project로 이동 후 해당 명령어를 입력해야 합니다.)
```
pip install -r requirements.txt
```

5. 이후 manage.py를 이용해 서버 실행
```
python manage.py runserver 
```

6. 명령어를 입력 후 `Starting development server at PORT주소`가 뜨면 해당 `PORT주소`를 인터넷 창에 입력하여 웹 페이지를 접속합니다.

<br>

###  ✔ DB ERD 및 테이블 명세서
- - -
![image](https://user-images.githubusercontent.com/83694062/236517639-2ce0a8a5-bfb5-45cb-9e23-f14409d569d2.png)
![image](https://user-images.githubusercontent.com/83694062/236524174-67757512-e925-4bd9-a896-6384231809df.png)


###  ✔ 데이터 출처 
- - -
[📚 YOUTUBE API](https://developers.google.com/youtube/v3/getting-started?hl=ko)

