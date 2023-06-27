# coding:utf-8
# time: 2023/6/23
# author: evan

from django.urls import path

from accounts import views

urlpatterns = [
    path('user/info/', views.user_info, name='user_info')
]
