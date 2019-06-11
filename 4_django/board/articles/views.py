from django.shortcuts import render,redirect
from .models import Article, Comment
# Create your views here.
def index(request):
    articles = Article.objects.all()
    context = {
        'articles':articles
    }
    return render(request, 'articles/index.html', context)

def detail(request, article_id):
    article = Article.objects.get(id=article_id)
    context = {
        'article':article
    }
    return render(request, 'articles/detail.html', context)

def new(request):
    return render(request, 'articles/new.html')

def create(request):
    if request.method == "POST":
        article = Article()
        article.title = request.POST.get('title')
        article.content = request.POST.get('content')
        article.user = request.user
        article.save()
        return redirect('articles:detail', article.id)
    else:
        return render(request, 'articles/form.html')



def delete(request, article_id):
    article = Article.objects.get(id=article_id)
    article.delete()
    return redirect('articles:index')

def edit(request, article_id):
    article = Article.objects.get(id=article_id)
    context = {
        'article':article
    }
    return render(request, 'articles/form.html', context)

def update(request, article_id):
    if request.method == "POST":
        article = Article.objects.get(id=article_id)
        article.title = request.POST.get('title')
        article.content = request.POST.get('content')
        article.save()
        return redirect('articles:detail', article.id)
    else:
        article = Article.objects.get(id=article_id)
        context = {
            'article': article
        }
        return render(request, 'articles/form.html', context)

def comment_create(request, article_id):
    comment = Comment()
    article = Article.objects.get(id=article_id)
    comment.content = request.POST.get('content')
    comment.article = article
    comment.user = request.user
    comment.save()

    return redirect("articles:detail", article_id)

def comment_delete(request, article_id, comment_id):
    comment = Comment.objects.get(id=comment_id)
    comment.delete()
    return redirect("articles:detail", article_id)

def comment_all(request):
    return render(request, 'articles/comment_all.html')

