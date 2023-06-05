# coding:utf-8
# time: 2023/6/4
# author: evan
from scrapy import cmdline

if __name__ == '__main__':
    cmdline.execute('scrapy crawl jdbooks'.split())
