# coding:utf-8
# time: 2023/5/29
# author: evan

from django.urls import path, re_path

from .views import hello_world, article_list, render_str, MyView
from .views import world

urlpatterns = [
    #    path('admin/', admin.site.urls),
    path("world/", world),
    path("hello_world/", hello_world),
    re_path(r'^article/(?P<month>0?[1-9]|1[012])/$', article_list),
    path('render_str', render_str, name='render_str'),
    path('my_view/', MyView.as_view(), name='my_view')
]
