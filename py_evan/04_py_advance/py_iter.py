# coding:utf-8
# time: 2023/5/11
# author: evan
# python的迭代器
from typing import Iterator, Any


def iter_handle():
    iterator = iter([1, 2, 3, 4])
    while True:
        res = _next(iterator)
        if res is None:
            break
        else:
            print(res)


def iter_handle2():
    for i in range(10):
        yield i


def _next(iter_obj: Iterator[Any]) -> Any:
    try:
        return next(iter_obj)
    except StopIteration:
        return None


def iter_handle3():
    iter_obj = (i for i in range(10))
    for i in range(10):
        print(_next(iter_obj))


if __name__ == '__main__':
    # iter_handle()
    iter_obj = iter_handle2()
    '''
    for i in iter_obj:
        print(i, end=' ') # 0 1 2 3 4 5 6 7 8 9 
    '''

    '''
    print(next(iter_obj))
    print(next(iter_obj))
    print(next(iter_obj))
    '''
    iter_handle3()
