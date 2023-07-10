# coding:utf-8
# time: 2023/6/23
# author: evan

from django.urls import path

from accounts import views

urlpatterns = [
    path('user/info/', views.user_info, name='user_info'),
    path('user/register/', views.user_register, name='user_register'),
    path('user/signup/', views.user_register_transaction, name='user_register_transaction'),
    path('user/login/', views.login, name='login')
]
