# coding:utf-8
# time: 2023/5/10
# author: evan
# os和sys模块

import os
import time


def os_handle():
    current_path = os.getcwd()
    print(current_path)
    dirs = os.listdir('/home/lds/Desktop/Programs/leon_cpp/py_evan')
    print(dirs)  # ['py_module', 'oop', 'main.py', 'py_base', '.idea']
    os.makedirs(f'{current_path}/leon/time')  # 创建文件夹
    time.sleep(1)
    os.removedirs(f'{current_path}/leon/time')


def get_all_files(path):
    if not os.path.exists(path):
        return

    dirs = os.listdir(path)
    print(dirs)
    for dir in dirs:
        if not os.path.isdir(dir):
            print(dir)
            continue
        else:
            get_all_files(dir)


if __name__ == '__main__':
    # os_handle()
    get_all_files('/home/lds/Desktop/Programs/leon_cpp/py_evan')
