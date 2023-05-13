# coding:utf-8
# time: 2023/5/12
# author: evan
import os
import threading
import time
from concurrent.futures import ThreadPoolExecutor

lock = threading.Lock()


def work(i):
    lock.acquire()
    print(i, os.getpid())
    time.sleep(1)
    lock.release()
    return 'result %s' % i


if __name__ == '__main__':
    print(os.getpid())
    t = ThreadPoolExecutor(2)
    result = []
    for i in range(20):
        t_result = t.submit(work, (i,))
        result.append(t_result)

    for res in result:
        print(res.result(), end=' ')
