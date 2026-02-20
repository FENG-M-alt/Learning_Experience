from django.db import models

# Create your models here.

class Book(models.Model):
    name = models.CharField(max_length=100)
    author = models.CharField(max_length=20,null=False)
    pub_time = models.DateTimeField(auto_now_add=True)
    price = models.FloatField(default=0)

    class Meta:
        db_table = "book_table"
        ordering = ["-pub_time", 'name'] # 前一个相同时按照后一个排序


class Author(models.Model):
    is_active = models.BooleanField()
    usename = models.CharField(max_length=200)
    date_joined = models.DateTimeField(auto_now_add=True)
    email = models.EmailField()
    visit_count = models.IntegerField()
    profield = models.TextField()
    website = models.URLField()

class Tag(models.Model):
    name = models.CharField(max_length=100)