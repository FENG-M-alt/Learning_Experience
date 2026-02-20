from django.urls import path
from .views import *
urlpatterns = [
    path('avg',avg_view, name='avg_view')
]