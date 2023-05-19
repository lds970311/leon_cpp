# coding:utf-8
# time: 2023/5/18
# author: evan
# redis案例
import random
from concurrent.futures import ThreadPoolExecutor

import redis

from redis_utils import pool

executor = ThreadPoolExecutor(200)


def vote():
    """
    模拟投票
    :return:
    """
    connection = redis.Redis(connection_pool=pool)
    if connection.exists('ballot'):
        connection.delete('ballot')
    names = {'马云': 0, '丁磊': 0, '张朝阳': 0, '马化腾': 0, '李彦宏': 0}
    connection.zadd('ballot', names)

    name_list = [x for x in names.keys()]

    # 模拟300人投票
    for i in range(0, 300):
        ticket = random.choice(name_list)
        connection.zincrby('ballot', 1, ticket)

    # 展示排名
    rank_list = connection.zrevrange('ballot', 0, -1)
    for i in rank_list:
        print(i.decode('utf-8'))
    del connection


if __name__ == '__main__':
    vote()
