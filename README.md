# 교환학생을 위한 커뮤니티 

### c9 : https://ide.c9.io/hyunkyung12/final_teamproject

### github : 

## 1. 기능

- 정보
	- 위치
	- 자격증

> 정보에 대한 것을 일일이 입력할지,
국제처에 있는 내용을 가져올지 생각해보기

크롤링 참고) https://github.com/askdjango/vod-crawling/blob/master/JOINS%20%EC%9D%B8%EB%AC%BC%EC%A0%95%EB%B3%B4%20%ED%81%AC%EB%A1%A4%EB%A7%81/main.ipynb

- 일정
	- 캘린더

- 후기
	- 생활
	- 면접
	- 자격

- 게시판
	- 게시글
	- 댓글
	- (좋아요)

- 회원가입
	- 모든 정보는 회원만 열람가능
	- 후기,게시판 : 글쓴이만 수정가능

## 2. Model

#### 1. 게시판

##### Post

| title| text| photo | author | created_date | published_date |
|--------|--------|--------|--------|-------|-------|
| CharField | TextField | ImageField | ForeignKey | DateTimeField | DateTimeField | 

##### Comment

| post | suthor| text | created_date | approved_comment |
|--------|--------|--------|--------|-------|
| ForeignKey | CharField | TextField | DateTimeField | BooeleanField | 

참고) https://jinpark-dg.gitbooks.io/django-girls-extended-tutorial-korean/content/homework_create_more_models/index.html

###### VIEW : scaffold를 이용하면 쉽게 할 수 있음, https://github.com/spapas/django-generic-scaffold 

#### 2. 정보 
##### Inform
| title | maps | content |
|--------|--------|--------|
| CharField | CharField | TextField | 

+) 위치를 지도로 표시할 경우
참고) https://github.com/askdjango/sample-photowall/commit/1475dbecbecac6d95be43c00a7a7c9c0950950f7

###### VIEW : 구현 방향에 따라 다름 (생각해서 추가)

#### 3. 후기 (게시판과 유사, Post 상속)
##### class Review(Post)
##### Post
| title| text | photo | author | created_date | published_date |
|--------|--------|--------|--------|-------|-------|
| CharField | TextField | ImageField | ForeignKey | DateTimeField | DateTimeField |

##### Comment
| post | suthor| text | created_date | approved_comment |
|--------|--------|--------|--------|-------|
| ForeignKey | CharField | TextField | DateTimeField | BooeleanField | 

> 카테고리화 하기 ?

#### 4. 일정
schedular package 사용할수 있음 (다른방법도 상관없어요!)
참고) https://github.com/llazzaro/django-scheduler 

#### 5. 회원가입

##### User (기본제공)
참고)  https://www.slideshare.net/DustinJunginSeoul/qna-blog-using-django-orm
https://wayhome25.github.io/django/2017/03/14/django-07-kilogram-03-signup/
http://dgkim5360.tistory.com/entry/django-model-inheritance 3. Proxy models

###### VIEW : index,login,signin

#### 관계설정? 딱히?
참고) http://gustnxodjs.tistory.com/1 


## 3. 외부파일
- bootstrap4
- 더 불러오는 경우 추가

## 4. 규칙
- html파일의 class이름은 앞에 model이름 꼭 붙이기 (충돌방지)
	ex)post모델의 title class는 ``<div class="post-title"``
    
- 자신의 기능이 한단계 완성될때마다 일단 git에 업로드 해놓기 

- 기본적 협업은 c9의 collaborate 기능을 사용, 교수님이 git을 좋아하신다고 하니 git에도 차근차근 올려보기

- 다른사람의 기능을 수정할때는 말하고 수정하기 (merge 할수도)

- css는 일단 수정하지 않기 , 전체적 테마를 잡은 후 수정

## 5. 생각해볼것

- 정보와 일정 기능에서, 해당 데이터를 어떻게 가져올지 생각해보기

- 메인에서 각 기능으로 어떻게 연결할지 생각하기
	ex) 메인에는 사진만, nav-bar로 연결
    ex) 쿵처럼 메인에 각 기능별 화면 나오게 (어떻게?)

### 기능에 대해 생각해 본것 (제 개인적인 생각입니다)
- 후기 기능과 게시판 기능의 명확한 구별이 없음
> 게시판 내에 팁과 커뮤니티를 만들고, 후기 내에 생활,면접,자격 에 대한 카테고리를 만든다고 회의록에 적혀있는데
> 그냥 게시판 기능 내의 카테고리를 크게 자유게시판/후기 정도로 나누어 후기 카테고리 내에 생활/면접/... 등으로 나누는 것이 좋을듯 합니다.

- 메인페이지의 구성과 각 페이지의 구성을 어느정도는 생각을 해놓고 개발을 해야할것 같아서, 다음에 모였을때는 이것에 대해 얘기를 해봐요!
- 각각 맡으신 기능별로, 일단 기본적으로 할 수 있는 기능부터 생각을 해보고 심화과정은 차차 추가하는 식으로 하면 좋을것 같아요
> ex) 게시판 기능의 경우
	- 글쓰기, 삭제
	- 글 수정
	- 댓글 기능
	- 좋아요 기능

	> 이런식으로 분류를 해서 할수 있는것 까지만 이라도 완성을 해보는것이 나을듯 해요!

## 6. 대략적 설계 (기능 : 앱이름)

- 게시판 : board
- 정보 : inform
- 일정 : schedule

