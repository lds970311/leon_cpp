# coding:utf-8
# time: 2023/5/30
# author: evan
from django.urls import path

from .views import index

urlpatterns = [
    path('index/', index, name='index')
]
