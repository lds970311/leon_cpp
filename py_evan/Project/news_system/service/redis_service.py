# coding:utf-8
# time: 2023/5/19
# author: evan
from Project.news_system.db.redis_dao import RedisNewsDao


class RedisNewsService:
    __redis_dao = RedisNewsDao()
