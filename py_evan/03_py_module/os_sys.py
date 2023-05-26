# coding:utf-8
# time: 2023/5/10
# author: evan
# os和sys模块

import os
import sys
import time


def os_handle():
    current_path = os.getcwd()
    print(current_path)
    dirs = os.listdir('/home/lds/Desktop/Programs/leon_cpp/py_evan')
    print(dirs)  # ['03_py_module', '02_oop', 'app.py', '01_py_base', '.idea']
    os.makedirs(f'{current_path}/leon/time')  # 创建文件夹
    time.sleep(1)
    os.removedirs(f'{current_path}/leon/time')


def os_path_handle():
    print(os.path.exists('/home/lds/Desktop/Programs/leon_cpp/py_evan'))  # True
    print(os.path.isabs('/home/lds/Desktop/Programs/leon_cpp/py_evan'))  # True
    print(os.path.getsize('/home/lds/Desktop/Programs/leon_cpp/py_evan'))  # 4096

    os.path.isdir()


def print_directory_contents(path):
    """
    递归遍历一个文件夹下的所有文件夹和文件，并打印它们的名称。
    """
    for name in os.listdir(path):
        full_path = os.path.join(path, name)
        if os.path.isdir(full_path):
            print_directory_contents(full_path)
        else:
            print(os.path.split(full_path)[1])


def sys_handle():
    print(sys.modules)
    print(sys.path)
    print(sys.getdefaultencoding())  # utf-8
    print(sys.platform)  # linux
    print(sys.version)  # 3.8.10 (default, Mar 13 2023, 10:26:41)
    print(sys.argv)  # ['/home/lds/Desktop/Programs/leon_cpp/py_evan/03_py_module/os_sys.py']


if __name__ == '__main__':
    # os_handle()
    print_directory_contents('/home/lds/Desktop/Programs/leon_cpp/py_evan')
    # os_path_handle()
    # print(dir(os.path))
    print('*' * 100)
    sys_handle()
