# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface

import pymongo


class Scrapy01Pipeline:
    def __init__(self):
        self.client = pymongo.MongoClient("localhost", 27017)
        self.client.admin.authenticate('admin', '19970311')

    def process_item(self, item, spider):
        self.client.spiders.pics.insert_one(item)
        return item
