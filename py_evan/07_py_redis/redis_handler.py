# coding:utf-8
# time: 2023/5/17
# author: evan

import redis

import redis_utils

red = redis.Redis(
    connection_pool=redis_utils.pool
)


def pipeline_handle():
    """
    pipeline操作redis事务
    :return:
    """
    pipeline = red.pipeline()
    pipeline.watch('money')
    pipeline.multi()
    pipeline.set('money', 1000)
    pipeline.incrby('money', 300)
    pipeline.incrby('money', -122)
    pipeline.execute()
    pipeline.reset()


if __name__ == '__main__':
    red.set('name', 'leon')
    name = red.get('name').decode('utf-8')
    print(name)
    red.hset('user1', 'sex', 'male')
    d = red.hgetall('user1')
    for k, v in d.items():
        print(f'{k.decode("utf-8")}:{v.decode("utf-8")}')
    print(red.hget('user1', 'sex'))
    pipeline_handle()
    del red
