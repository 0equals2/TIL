#장고(DJANGO)

##1. 라이브러리 설치

install library - pip install django==2.1.8

##2. 장고 시작하기
 
 장고 - 웹 프레임워크 
 
 기본적인 구조나 필요한 코드들은 제공.
 
 좋은 웹 서비스를 제작하는데 집중해라!
 
 in settings.py 
 
 LANGUAGE_CODE = ko-kr
 
 TIME_ZONE = 'Asia/Seoul'
 
 USE_I18N = True - 국제화

 USE_L10N = True - 현지화
 
 UES_TZ = False - time zone 사용
 

##3. 장고의 작동법

클라이언트(요청) - 서버(응답)

* Model - data관리

* Template - 사용자가 보는 화면 - templates.html

* View - 중간 관리자 - app.py

* (controll - 관리자)

클라이언트가 요청 - V가 사용자의 요청을 분석 - V가 M에 데이터를 요청 
 
 M은 Database를 찾아 데이터를 V에 보내줌
 
 
 데이터를 토대로 T에 보내 html에 실어서 클라이언트에게 보여줌. 
 
 
 ## 4. 장고의 구성
 
 ### 프로젝트 dir
 
 ####마스터 앱
 
 
 
 ####서브 앱
 
 앱을 등록하면 마스터 앱의 세팅.py에