# coding:utf-8
# time: 2023/5/17
# author: evan

from mysql.connector.pooling import MySQLConnectionPool

__config = {
    'host': '192.168.31.192',
    'port': 3306,
    'user': 'root',
    'password': '19970311',
    'database': 'news_system',
}

try:
    pool = MySQLConnectionPool(
        **__config,
        pool_size=15
    )
except Exception as e:
    print(f'mysql链接失败：{e}')
