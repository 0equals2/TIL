```python
    article = models.ForeignKey(Article,on_delete=models.CASCADE) 
```

게시물이 없는데 댓글을 달 수 없고, 게시물이 삭제되면 게시물에 딸려있는 댓글을 함께 삭제한다. (1:n 관계에서 필수로 설정)  #CASCADE 대문자로 적기!

댓글과 관련된 게시물은 게시물 id가 숫자로 저장되지만 article object를 다룰 수 있게 된다.

### !실제로 파이썬 코드로 어떻게 댓글을 작성하는지 알아보기!

python manage.py shell < 터미널에서 shell을 열어서 바로 댓글 작성해보기

``` python
from articles.models import Article, Comment
Comment.objects.all() #데이터 전부 불러오기
Comment.objects.first() #첫번째로 작성한 모델을 불러오기
Comment.objects.first().content #작성한 내용보기
comment = Comment.object.fisrt()
comment.conetent # 내용
comment.id # 1
comment.article # <Article: Article object (5)>
comment.article_id # 5 #Django가 알아서 지정해준 (Foreign Key를 사용했기 때문에)
```

content, article 열을 만들었기 떄문에 참조가능하다. id와 article_id는 Django가 알아서 부여

``` python
article = comment.article
article # <Article: Article object (5)>
article.comment_set #저장한 댓글 목록 조회 #이걸로 바로 조회는 불가
article.comment_set.all() #리스트 형태로 반환
```

게시물에 댓글을 다는 것은 CRUD 구조를 가질 수 밖에 없음. 하지만 고민해야 하는 포인트는 댓글과 게시물의 차이점! 댓글은 게시물 안에 작성하는 것이 일반적. 게시물을 작성할 때는 게시물 작성 폼을 만들었다. 하지만 댓글은 독자적이지 않은 폼을 어디에 작성해야 하는가? detial 페이지에 작성하는 것이 가장 일반적. (새로운 페이지를 보여주는 것도 상관은 없다.) ex. comments on  instagram, twitter 인덱스 페이지와 댓글 페이지가 별도로 존재.

### !댓글을 지우는 일과 게시물을 지우는 일을 구분!

