# coding:utf-8
# time: 2023/7/15
# author: evan

from django.urls import path

from system import views

urlpatterns = [
    path('slider/list/', views.slider_list, name='slider_list'),
]
