# coding:utf-8
# time: 2023/5/11
# author: evan
# python魔法函数
from functools import reduce


def filter_handle():
    f = filter(lambda item: item % 2 != 0, [1, 2, 3, 4])
    print(list(f))  # [1, 3]


def map_handle():
    res = map(lambda x: x ** 2, [5, 6, 9, 8])
    print(list(res))  # [25, 36, 81, 64]


def reduce_handle():
    res = reduce(lambda x, y: x * y, [4, 5, 6])
    print(res)  # 120


if __name__ == '__main__':
    # filter_handle()
    # map_handle()
    reduce_handle()
