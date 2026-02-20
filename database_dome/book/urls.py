from django.urls import path
from .views import *

urlpatterns = [
    path("", index, name='index'),
    path("add", add_book, name='add_name'),
    path("query", query_book, name='query_book'),
    path("update", update_view, name='update_view'),
    path("order", order, name='order'),
]