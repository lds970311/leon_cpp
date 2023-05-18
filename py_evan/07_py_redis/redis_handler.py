# coding:utf-8
# time: 2023/5/17
# author: evan

import redis

pool = redis.ConnectionPool(
    host="192.168.31.192",
    port=6379,
    password='19970311',
    db=0,
    max_connections=20
)

connection = pool.get_connection()
if __name__ == '__main__':
