# coding:utf-8
# time: 2023/5/11
# author: evan
# python多进程与多线程
import multiprocessing
import time


def work_a():
    for i in range(100):
        print(i, 'a')
        time.sleep(0.3)


def work_b():
    for i in range(30):
        print(1, 'b')
        time.sleep(0.6)


if __name__ == '__main__':
    a = multiprocessing.Process(target=work_a)
    b = multiprocessing.Process(target=work_b)
    a.start()
    b.start()
