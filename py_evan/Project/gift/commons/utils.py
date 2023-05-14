# coding:utf-8
# time: 2023/5/12
# author: evan

import os
import time

from .error import JsonNotFoundError, NotFileError, NotJsonError


def check_file(file_path: str) -> None:
    if not os.path.exists(file_path):
        raise JsonNotFoundError(f"{file_path} 文件不存在！")
    if not os.path.isfile(file_path):
        raise NotFileError(f'{file_path} 不是一个文件！')
    if not file_path.endswith('.json'):
        raise NotJsonError(f'{file_path} 不是一个json文件！')


def timestamp2string(timesstamp: float) -> str:
    timeobj = time.localtime(timesstamp)
    return time.strftime('%Y-%m-%d %H:%M:%S', timeobj)
