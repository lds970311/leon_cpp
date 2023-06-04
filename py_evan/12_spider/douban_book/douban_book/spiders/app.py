import scrapy
from scrapy.http.response.html import HtmlResponse

from ..items import DoubanBookItem


class AppSpider(scrapy.Spider):
    name = 'app'
    allowed_domains = ['book.douban.com']
    start_urls = ['https://book.douban.com/latest']

    def parse(self, response: HtmlResponse):
        books = response.xpath("//ul[@class='chart-dashed-list']/li")
        for books in books:
            title = books.xpath(".//h2/a[@class='fleft']/@href").get()

            yield scrapy.Request(url=title, callback=self.parse_book_detail, dont_filter=True)

        next_url = response.xpath("//span[@class='next']//a/@href").get()
        if next_url is not None:
            new_url = response.urljoin(next_url)
            print(new_url)
            yield scrapy.Request(url=new_url, callback=self.parse)

    def parse_book_detail(self, response: HtmlResponse):
        print('haha')
        item = DoubanBookItem()
        item['author'] = response.xpath("//div[@id='info']/span[1]/a/text()").get()
        item['publisher'] = response.xpath("//div[@id='info']/a[1]/text()").get()
        print(item['author'], item['publisher'])
        yield item
