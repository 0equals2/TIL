from django.db import models

# Model Template View
class Article(models.Model):
    # id = Primary Key
    title = models.CharField(max_length=100)
    content = models.TextField()

class Comment(models.Model):
    content = models.TextField()
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
