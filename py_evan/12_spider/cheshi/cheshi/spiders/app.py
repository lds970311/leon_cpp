import scrapy
from scrapy.http.response.html import HtmlResponse


class AppSpider(scrapy.Spider):
    name = 'app'

    def start_requests(self):
        url = "https://api.cheshi.com/services/common/api.php?api=login.Login"
        data = {
            'act': 'login',
            'mobile': '17673045972',
            'source': 'pc',
            'password': '19970311',
            'hold_time': 'yes'
        }

        yield scrapy.FormRequest(url=url, formdata=data, callback=self.parse)

    def parse(self, response: HtmlResponse):
        url = "https://my.cheshi.com/user/"
        yield scrapy.Request(url=url, callback=self.parse_admin)

    def parse_admin(self, response: HtmlResponse):
        print(response.text)
