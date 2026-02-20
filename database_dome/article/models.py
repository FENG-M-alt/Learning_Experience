from django.db import models

# Create your models here.

class User(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=100)

class UserExtension(models.Model):
    birthday = models.CharField(max_length=20)
    university = models.CharField(max_length=100)
    user = models.OneToOneField('User', on_delete=models.CASCADE)

class Article(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()

    author = models.ForeignKey('User', on_delete=models.CASCADE)