import json
import math

import scrapy
from scrapy.http import Response


class TubatuSpider(scrapy.Spider):
    name = 'tubatu'
    allowed_domains = ['https://xiaoguotu.to8to.com/']
    start_urls = ['https://xiaoguotu.to8to.com/index/caselist/2']

    def parse(self, response: Response, **kwargs):
        print(response.request.headers)
        current_url = response.request.url

        current_page = int(current_url.split('/')[-1])
        js = json.loads(response.text)
        result = js['result']
        total = int(js['total'])  # 总条数
        # 计算总页数
        page_num = math.ceil(total / len(result))

        if current_page < page_num:
            next_url = f"https://xiaoguotu.to8to.com/index/caselist/{current_page + 1}"
            yield scrapy.Request(url=next_url, callback=self.parse)

        for item in result:
            print(item)
