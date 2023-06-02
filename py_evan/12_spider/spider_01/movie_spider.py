# coding:utf-8
# time: 2023/6/1
# author: evan
import math
import re
import threading
import time

import requests
from lxml import etree
from pymongo import MongoClient

from proxy_config import headers, proxies


class MovieSpider:
    __url__prefix = "http://movie.54php.cn/movie/"
    __mongo_host__ = 'localhost'
    __mongo__port = 27017
    __mongo__username = 'admin'
    __mongo__password = '19970311'

    def __init__(self):
        self.client = MongoClient(self.__mongo_host__, self.__mongo__port)
        self.client.admin.authenticate(self.__mongo__username, self.__mongo__password)
        self.session = requests.Session()
        self.total_pages = self.__parse_page_nums()

    def __parse_page_nums(self):
        response = self.session.get(self.__url__prefix, headers=headers, proxies=proxies, timeout=(5, 5))
        html = etree.HTML(response.text)
        element = html.xpath("//span[@class='pagination_count']/text()")[0]
        result = re.findall("\d+", element)
        page_num = math.ceil(int(result[0]) / int(result[1]))
        return page_num

    def __parse_list(self, pagenum=1):
        response = self.session.get(f'{self.__url__prefix}?&p={pagenum}', headers=headers, proxies=proxies,
                                    timeout=(5, 5))
        html = etree.HTML(response.text)
        try:
            links = html.xpath("//a[@class='thumbnail']/@href")
        except Exception:
            self.__parse_list(pagenum)
        for link in links:
            try:
                self.__parse_detail(link)
                time.sleep(0.5)
            except Exception as e:
                print(e)
                continue

    def __parse_detail(self, url: str):
        response = self.session.get(url, headers=headers, timeout=(5, 5))
        html = etree.HTML(response.text)
        movie_info = {
            'name': html.xpath("//div[@class='page-header']/h1/text()")[0],
            'type': html.xpath("//div[@class='panel-body']/p[2]/text()")[0].replace("类型：", "").split('/'),
            'actor': html.xpath("//div[@class='panel-body']/p[3]/text()")[0].replace("主演：", ""),
            'describe': html.xpath("//div[@class='panel-body']/p[4]/text()")[0],
            'address': html.xpath("//div[@class='panel-body']/p[5]/text()")[0].replace("下载地址：", "")
        }
        print(movie_info)
        self.write_to_mongo(movie_info)

    def write_to_mongo(self, movie_info):
        self.client.spiders.movies.insert_one(movie_info)

    def scraw_all(self):
        for i in range(1, self.total_pages + 1):
            thread = threading.Thread(target=self.__parse_list, args=(i,))
            thread.start()
            time.sleep(2)

    def get_all(self):
        for i in range(1, self.total_pages + 1):
            self.__parse_list(i)
            time.sleep(2)


if __name__ == '__main__':
    spider = MovieSpider()
    spider.scraw_all()
