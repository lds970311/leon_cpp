# coding:utf-8
# time: 2023/6/18
# author: evan

from django.urls import path

from .views import index

urlpatterns = [
    path('a/', index)
]
