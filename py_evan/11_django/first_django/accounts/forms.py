# coding:utf-8
# time: 2023/6/27
# author: evan
import re

from account.models import User
from accounts.models import UserProfile
from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(label='用户名', max_length=16, empty_value='nobody', initial='admin')
    password = forms.CharField(label='密码', max_length=64, required=True, widget=forms.PasswordInput)

    def clean(self):
        data = super().clean()
        print(data)
        # 如果单个字段有错误，直接返回，不执行后面的验证
        if self.errors:
            return
        username = data['username']
        password = data['password']
        # username = data.get('username', None)
        # password = data.get('password', None)
        if username and password:
            # 查询用户名和密码匹配的用户
            user_list = User.objects.filter(username=username)
            err_list = []
            if user_list.count() == 0:
                err_list.append(forms.ValidationError('用户名不存在'))
                # raise forms.ValidationError('用户名不存在')
            # 验证密码是否正确
            # TODO 使用加密算法进行验证
            if not user_list.filter(password=password).exists():
                # raise forms.ValidationError('密码不正确')
                err_list.append(forms.ValidationError('密码不正确'))
            if err_list:
                raise forms.ValidationError(err_list)
        return data

    phone = forms.CharField(label='手机号', max_length=11, required=True)

    def clean_phone(self):
        '''
        验证手机号
        :return:
        '''
        data = self.cleaned_data['phone']
        pattern = r'^1[3-9][0-9]{9}$'
        if not re.search(pattern, data):
            raise forms.ValidationError('请输入正确的手机号%s', code='invaild_phone', params=(data,))
        return data

    email = forms.EmailField(label='邮件', max_length=24)
    age = forms.IntegerField(label='年龄', required=False)
    sex = forms.ChoiceField(label='性别', choices=(
        ('1', '男'),
        ('0', '女')
    ))
    birthday = forms.DateField(label='生日'),
    avatar = forms.ImageField(label='用户头像', required=False)
    is_marry = forms.BooleanField(label='是否结婚')
    dssc = forms.CharField(label='说明', widget=forms.Textarea)


class UserChangeForm(forms.ModelForm):
    """
    从ORM模型创建表单
    """

    class Meta:
        model = User
        fields = ["username", 'password', 'avatar']
        labels = {
            'username': '用户名称'
        }
        widgets = {
            'password': forms.PasswordInput(attrs={
                'style': 'border: 1px solid red'
            })
        }

    def save(self, commit=False):
        user_obj = super().save(commit=commit)
        user_obj.save()
        UserProfile.objects.create(user=user_obj, username=user_obj.username)
        return user_obj
