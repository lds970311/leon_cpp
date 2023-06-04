# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from pymongo import MongoClient


class DoubanBookPipeline:
    def __init__(self):
        self.client = MongoClient('localhost', 27017)
        self.client.admin.authenticate('admin', '19970311')

    def process_item(self, item, spider):
        data = dict(item)
        self.client.spiders.douban_book.insert_one(data)
        return item

    def __del__(self):
        self.client.close()
