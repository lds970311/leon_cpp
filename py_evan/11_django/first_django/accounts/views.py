# Create your views here.
import os

from accounts.forms import LoginForm, UserChangeForm
# Create your views here.
from accounts.models import User, UserProfile
from django.db import transaction
from django.http import HttpResponse, HttpRequest
from django.shortcuts import render
from first_django.settings import MEDIA_ROOT


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
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            print('表单验证通过')
        else:
            print(form.errors)

    form = LoginForm()
    return render(request, 'user_login.html', {
        'form': form
    })


def user_change(request: HttpRequest):
    if request.method == 'POST':
        form = UserChangeForm(data=request.POST)
        if form.is_valid():
            print('表单验证通过')
            form.save()
        else:
            print(form.errors)

    form = UserChangeForm()
    return render(request, 'user_change.html', {
        'form': form
    })


def upload(request: HttpRequest):
    if request.method == 'POST':
        file = request.FILES['avatar']
        if file:
            filename = os.path.join(MEDIA_ROOT, 'test.jpg')
            with open(filename, 'wb+') as f:
                for chunk in file.chunks():
                    f.write(chunk)
            print('上传成功')
    return render(request, 'upload_file.html')
