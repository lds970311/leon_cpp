# coding:utf-8
# time: 2023/6/27
# author: evan
from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(label='用户名', max_length=16, empty_value='nobody', initial='admin')
    password = forms.CharField(label='密码', max_length=64, required=True, widget=forms.PasswordInput)
    email = forms.EmailField(label='邮件', max_length=24)
    age = forms.IntegerField(label='年龄', required=True)
    sex = forms.ChoiceField(label='性别', choices=(
        ('1', '男'),
        ('0', '女')
    ))
    birthday = forms.DateField(label='生日'),
    avatar = forms.ImageField(label='用户头像')
    is_marry = forms.BooleanField(label='是否结婚')
