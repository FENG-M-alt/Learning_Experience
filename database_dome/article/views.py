from cairo import Content
from django.shortcuts import render
from .models import User, Article 
from django.http import HttpResponse
# Create your views here.

def article_text(request):
    user = User(username='卡莫纳', password='111')
    user.save()
    article = Article(author=user, title='117策划', content='xxx')
    article.save()
    return HttpResponse("xxx")

def one_to_many(requert):
    user = User.objects.first()
    articles = user.article_set.all()
    for article in articles:
        print(article.title)
    return HttpResponse("成功!")