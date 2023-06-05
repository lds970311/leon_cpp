import re

import scrapy
from scrapy.http.response.html import HtmlResponse
from scrapy_redis.spiders import RedisSpider

from ..items import JdBooksRedisItem


class JdbooksSpider(RedisSpider):
    name = 'jdbooks'
    redis_key = 'jd'

    # allowed_domains = ['list.jd.com']
    # start_urls = ['https://list.jd.com/list.html?cat=1713%2C3258&ev=3744_4990%5E&page=1&s=1&click=0']

    def __init__(self, *args, **kwargs):
        domain = kwargs.pop('domain', "")
        self.allow_domains = filter(None, domain.split(","))
        super(JdbooksSpider, self).__init__(*args, **kwargs)

    def parse(self, response: HtmlResponse):
        books = response.xpath("//div[@id='J_goodsList']/ul/li")
        item = JdBooksRedisItem()
        if len(books) != 0:
            for book in books:
                item["title"] = book.xpath(".//div[@class='p-name']//em/text()").get()
                item["price"] = book.xpath(".//div[@class='p-price']//i/text()").get()
                # print(title, price)

            pattern = re.compile('page=(\d*?)&s=(\d*?)&')
            result = pattern.findall(response.url)[0]
            print(f'正在抓取网页：{response.url}')
            page = int(result[0]) + 1
            s = int(result[1]) + 30
            next_url = f"https://list.jd.com/list.html?cat=1713%2C3258&ev=3744_4990%5E&page={page}&s={s}&click=0"
            yield scrapy.Request(url=next_url, callback=self.parse)
