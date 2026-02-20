from django.urls import path
from .views import *

urlpatterns = [
    path('text', article_text, name="article_text"),
    path('one', one_to_many, name="one_to_many"),
]