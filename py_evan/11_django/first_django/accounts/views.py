# Create your views here.
from django.db import transaction
from django.http import HttpResponse, HttpRequest
from django.shortcuts import render

from accounts.forms import LoginForm
# Create your views here.
from accounts.models import User, UserProfile


def user_info(request):
    """ 用户详情-查询优化 """
    user = User.objects.get(pk=1)
    # profile_list = UserProfile.objects.all()
    profile_list = UserProfile.objects.all().select_related('user')

    # 使用SQL查询
    user_list = User.objects.raw('SELECT * FROM  `accounts_user`')
    return render(request, 'user_info.html', {
        'user': user,
        'profile_list': profile_list,
        'user_list': user_list
    })


def user_register(request: HttpRequest):
    '''
    用户注册
    :param request:
    :return:
    '''
    user = User.objects.create(username='ashley', password='444555', nickname='as')
    profile = UserProfile.objects.create(user=user, username='ashley')
    return HttpResponse('ok')


@transaction.atomic
def user_register_transaction(request: HttpRequest):
    user = User.objects.create(username='ashley1', password='444555', nickname='as')
    profile = UserProfile.objects.create(user=user, username='ashley1')
    return HttpResponse('ok')


def login(request: HttpRequest):
    form = LoginForm()
    return render(request, 'user_login.html', {
        'form': form
    })
