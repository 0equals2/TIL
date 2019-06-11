from django.shortcuts import render, redirect
from .models import Article


# Form HTML
def new_article(request):
    return render(request, 'board/new_article.html')


# SAVE new article
def create_article(request):
    if request.method == 'POST':
        article = Article()
        article.title = request.POST.get('title')
        article.content = request.POST.get('content')
        article.save()
        return redirect(f'/board/{article.id}')
    else:
        return redirect('/board/new/')


# Read all
def article_list(request):  # 전체 article 조회하기
    articles = Article.objects.all()  # []

    return render(request, 'board/article_list.html', {
        'articles': articles,
    })


# Read one
def article_detail(request, article_id):  # 특정 article 조회하기
    article = Article.objects.get(id=article_id)

    return render(request, 'board/article_detail.html', {
        'article': article,
    })


# Update
def edit_article(request, article_id):
    article = Article.objects.get(id=article_id)
    return render(request, 'board/edit_article.html', {
        'article': article,
    })


def update_article(request, article_id):
    if request.method == 'POST':
        article = Article.objects.get(id=article_id)
        article.title = request.POST.get('title')
        article.content = request.POST.get('content')
        article.save()
        return redirect(f'/board/{article.id}')
    else:
        return redirect(f'/board/{article_id}/edit/')



# Delete
def delete_article(request, article_id):
    article = Article.objects.get(id=article_id)
    article.delete()
    return redirect('/board/')
