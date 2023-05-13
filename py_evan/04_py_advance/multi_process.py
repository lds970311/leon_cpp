# coding:utf-8
# time: 2023/5/11
# author: evan
# python多进程与多线程
import multiprocessing
import time


def work_a(lock):
    lock.acquire()
    for i in range(100):
        print(i, 'a')
        time.sleep(0.3)
    lock.release()
    return 8


def work_b():
    for i in range(30):
        print(1, 'b')
        time.sleep(0.6)
    return 10


if __name__ == '__main__':
    """
        a = multiprocessing.Process(target=work_a)
        b = multiprocessing.Process(target=work_b)
        a.start()
        b.start()

    """

    # 使用进程尺
    pool = multiprocessing.Pool(5)
    # 获取锁
    manager = multiprocessing.Manager()
    lck = manager.Lock()

    result_a = pool.apply_async(func=work_a, args=(lck,))
    result_b = pool.apply_async(func=work_b)

    print('res_a = ', result_a.get())
    print('res_b =', result_b.get())
    pool.close()
    pool.join()
