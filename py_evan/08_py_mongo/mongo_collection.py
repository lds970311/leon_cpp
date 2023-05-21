# coding:utf-8
# time: 2023/5/21
# author: evan

from pymongo import MongoClient

client = MongoClient(host='localhost', port=27017)
client.admin.authenticate('admin', '19970311')
