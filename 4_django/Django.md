Django dynamic (↔ static )

Why?

front-end 											|									 fullstack
framework																				 framework

react 																						Django

angular												|									 Ruby

vuejs																						spring

화면을 만드는 것이 목표											서버 프로그램 전체, 화면, 


How?  MTV 디자인 패턴 (↔ MVC 디자인 패턴)

M Model 데이터를 관리

T Template 사용자가 보는 화면

V View 중간 관리자

요청이 들어가면 중간관리자가 호출할 수 있는 주소인지 확인(url 분석)을 한다. 모델에게 필요한 것을 요구. 모델이 중간관리자에게 해당 내용을 전달. 중간관리자가 화면 구성을 템플릿에게 전달. 탬플릿이 화면을 송출.
(cf. Flask에서의 app.py는 view와 유사)

```
요청이 들어오면 urls.py 에서 명단을 확인 매핑되어 있는 함수로 보낸다. views.py 에서 함수에 해당되는 무언가를 내보낸다.   
```



```
$ django-admin startproject 프로젝트명
$ django-admin startapp 앱명 #앱을 생성하면 마스터 세팅에 반드시 등록해줘야 한다.
```

자동으로 디렉토리와 기본 세팅이 생성된다.

프로젝트 명으로 생성된 폴더 안에 프로젝트 명으로 된 폴더가 이중으로 생성되어 있다.

상위 폴더는 프로젝트라 부르고, 하위 폴더는 앱이라 부르는데 최초 생성된 앱은 마스터 앱이라 칭한다.

```python
# settings.py 설정
use_I18N internationalization #18자
use_L10N locanlization #10자
```

```
url.py url은 전부 url에 모을 것이다
views.py 행동은 전부 views에 모은다. 
os.path.join(BASE_DIR, 'templates') templates라는 폴더를 찾으면 거기에서 꺼내겠다. (하지만 앞으로 쓸 일은 없는....)
```

```
path('url/',)
```









#장고템플릿랭귀지