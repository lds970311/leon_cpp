# coding:utf-8
# time: 2023/5/29
# author: evan
from django.http import HttpResponse

'''
重写内置错误处理视图，注意不要开启debug模式
'''


def page_500(request):
    return HttpResponse('服务器正忙，请稍后再试')


def page_404(request, exception):
    return HttpResponse('您访问的页面跑丢了，555！')
