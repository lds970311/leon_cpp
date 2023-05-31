# coding:utf-8
# time: 2023/5/30
# author: evan

from django import template

register = template.Library()


@register.filter(name='phonenum_filter')
def phonenum_filter(phone_num: str):
    """
    自定义手机号过滤器
    :param phone_num:
    :return:
    """
    return phone_num[0:3] + "****" + phone_num[7:]
