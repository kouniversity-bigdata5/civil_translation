# 데이터 작업 폴더
## 설명
민원 서식 번역을 위한 데이터를 모으는데 작업한 내용을 관리하는 폴더

## 필요한 데이터
민원 서식 데이터, 말뭉치 데이터(한국어/동남아어 로 이루어진 쌍)

## 소스 설명
### 국민청원정제.ipynb
- 국민청원 제목 및 내용을 모은 코드(출처 : https://github.com/lovit/petitions_dataset)  
- 우선 위의 패키지를 설치하고, 데이터를 받아야 함(기간: 2017-08 ~ 2019-09, 약 30만건)
- 데이터를 받고 정규식을 활용하여 날짜, 청원분류, 제목, 내용 형태로 csv저장
(데이터로 사용하지 않음)

### 3rd_EDA.ipynb, Text_Preprocessing.ipynb
민원 데이터 전처리 EDA, 세종코퍼스 EDA

### 경기도청, 제주도청, 법원, 노동청 jupyter
각 기관별 서식 크롤링 코드

### html서식유지영문번역, hwp변환(pdf, jpg, html), pdf변환(jpg).ipynb, minwon_text.ipynb
민원 관련 서식 변환 및 텍스트 추출 코드

### naver_dictionary_crawling.ipynb
네이버 사전 크롤링

### 태국 bbc 뉴스 사이트 크롤링.ipynb
태국 뉴스 사이트 크롤링

### insert_minwon.ipynb
세종 말뭉치 db에 민원 서식의 텍스트 데이터 넣기

### 세종말뭉치문장뽑기.ipynb
세종 말뭉치 문장 뽑기

### 세종말뭉치_corpus만들기.ipynb
말뭉치를 sqlite db화 작업(corpus.db 라는 이름으로 저장)