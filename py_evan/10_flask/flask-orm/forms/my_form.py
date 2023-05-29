# coding:utf-8
# time: 2023/5/28
# author: evan
import re

from flask_wtf import FlaskForm
from flask_wtf.file import FileRequired, FileAllowed
from wtforms import StringField, PasswordField, SubmitField, FileField
from wtforms.validators import DataRequired, ValidationError


def password_required(form, field):
    """
    全集验证器
    :param form:
    :param field:
    :return:
    """
    usrname = field.data
    pattern = r'^\w{3,10}$'
    if not re.search(pattern, usrname):
        raise ValidationError('用户名验证失败')
    return field


class LoginForm(FlaskForm):
    """
    登录表单
    """

    def validate_username(self, field):
        """
        局部表单验证器
        :param field:
        :return:
        """

        usrname = field.data
        pattern = r'^\w{3,10}$'
        if not re.search(pattern, usrname):
            raise ValidationError('用户名验证失败')
        return field

    username = StringField(label='用户名')
    password = PasswordField(label='密码', validators=[DataRequired('请输入密码'), password_required])
    avatar = FileField(label='头像',
                       validators=[FileAllowed(['jpg', 'png'], '仅支持png，jpg格式')])
    submit = SubmitField('注册')
