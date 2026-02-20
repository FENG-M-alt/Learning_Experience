from django.shortcuts import render
from django.http import HttpResponse
from django.db import connection
from .models import Book # "."代表在同级的文件夹下寻找
# Create your views here.


def index(request):
    # 获取游标对象
    cursor = connection.cursor()
    # 拿到游标对象后执行sql语句
    cursor.execute("select * from book")
    # 获取所有的数据
    rows = cursor.fetchall()
    # 遍历查询到的数据
    for row in rows:
        print(row)
    return HttpResponse("查到成功")

def add_book(request):
    book = Book(name='红楼梦', author='罗贯中', price=100)
    book.save()
    return HttpResponse("图书插入成功")

def query_book(request):
    books = Book.objects.all()
    for book in books:
        print(f"{book.id}, {book.name}, {book.author}, {book.pub_time}, {book.price}")
    
    try:
        book = Book.objects.get(name='sa')
    except Book.DoesNotExist:
        print("图书不存在！")
    return HttpResponse("查询成功")

def update_view(request):
    book = Book.objects.first()
    book.name = '西游记' 
    book.save()
    return HttpResponse("修改成功")

def order(request):
    books = Book.objects.all()
    for book in books:
        print(book.name)
    return HttpResponse("排序成功")