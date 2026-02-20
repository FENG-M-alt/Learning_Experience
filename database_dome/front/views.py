from django.shortcuts import render
from django.http import HttpRequest
from django.db.models import Avg
from .models import Book
# Create your views here.

def avg_view(request):
    n = Book.objects.aggregate(Avg('price'))
    print(n)
    return HttpRequest("成功")