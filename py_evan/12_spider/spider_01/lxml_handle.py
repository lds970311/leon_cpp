# coding:utf-8
# time: 2023/5/31
# author: evan
# lxml操作
import json
import os

import requests
from lxml import etree

from proxy_config import headers, proxies


def handle_lxml():
    html_data = '''
    <div>
      <ul>
           <li class="item-0"><a href="link1.html">first item</a></li>
           <li class="item-1"><a href="link2.html">second item</a></li>
           <li class="item-inactive"><a href="link3.html"><span class="bold">third item</span></a></li>
           <li class="item-1"><a href="link4.html">fourth item</a></li>
           <li class="item-0"><a href="link5.html">fifth item</a>
       </ul>
    </div>
    '''

    html = etree.HTML(html_data)
    print(etree.tostring(html).decode())
    xpath = html.xpath('//div/ul/li[contains(@class,"item")]')
    print(
        xpath)  # [<Element li at 0x7f0f7c5dd500>, <Element li at 0x7f0f7c5dd580>, <Element li at 0x7f0f7c5dd480>, <Element li at 0x7f0f7c5dd5c0>, <Element li at 0x7f0f7c5dd600>]
    for li in xpath:
        # print(li.xpath('./a//text()'))
        print(li.xpath("./a//@href"))


def get_books_data_by_lxml():
    session = requests.session()
    all_data = []
    for i in range(1, 6):
        url = f"http://yushu.talelin.com/book/search?q=go&page={i}"
        response = session.get(url, headers=headers, proxies=proxies)
        html = etree.HTML(response.text)
        block = html.xpath("//div[@class='col-md-7 flex-vertical description-font']")
        for div in block:
            book_details = div.xpath("./span[2]/text()")[0].split('/')
            try:
                info_dict = {
                    'title': div.xpath("./span[1]/text()")[0],
                    'author': book_details[0],
                    'press': book_details[1],
                    'price': book_details[2],
                    'desc': div.xpath("./span[2]/text()")[0],
                }
            except IndexError as e:
                info_dict = {
                    'title': div.xpath("./span[1]/text()")[0],
                    'author': book_details[0],
                    'press': '暂无数据',
                    'price': '暂无价格数据',
                    'desc': div.xpath("./span[2]/text()")[0],
                }
            finally:
                all_data.append(info_dict)
    path = os.path.join(os.path.dirname(__file__), 'datas', 'all_books_go.json')
    all_json = json.dumps(all_data, ensure_ascii=False, indent=2)
    with open(path, 'w') as f:
        f.write(all_json)


if __name__ == '__main__':
    get_books_data_by_lxml()
