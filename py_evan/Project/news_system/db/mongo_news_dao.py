# coding:utf-8
# time: 2023/5/22
# author: evan
from bson import ObjectId

from .mongo_db import client


class MongoNewsDao:
    def insert(self, title, content):
        """
        添加新闻正文记录
        :param title:
        :param content:
        :return:
        """
        try:
            client.news_system.news.insert_one({
                'title': title,
                'content': content
            })
        except Exception as e:
            print(e)

    def serach_news_id(self, title):
        try:
            find_one = client.news_system.news.find_one({'title': title})
            return str(find_one["_id"])
        except Exception as e:
            print(e)

    def update_news(self, id, title, content):
        try:
            client.news_system.news.update_one({
                {'_id', ObjectId(id)},
                {
                    '$set': {
                        'title': title,
                        'content': content
                    }
                }
            })

        except Exception as e:
            print(e)

    def search_content_by_id(self, id):
        try:
            find_one = client.news_system.news.find_one({'_id': ObjectId(id)})
            return str(find_one["content"])
        except Exception as e:
            print(e)

    def delete_by_id(self, id):
        try:
            client.news_system.news.delete_one({'_id': ObjectId(id)})
        except Exception as e:
            print(e)
