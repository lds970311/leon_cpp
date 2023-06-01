# coding:utf-8
# time: 2023/5/31
# author: evan
# beautiful soup操作
import json
import os

import requests
from bs4 import BeautifulSoup

from proxy_config import headers, proxies


def bs4_handle_01():
    html = """
    <html><head><title>The Dormouse's story</title></head>
    <body>
    <p class="title" name="dromouse"><b>The Dormouse's story</b></p>
    <p class="story">Once upon a time there were three little sisters; and their names were
    <a href="http://example.com/elsie" class="sister" id="link1"><!-- Elsie --></a>,
    <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
    <a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
    and they lived at the bottom of a well.</p>
    <p class="story">...</p>
    """

    html2 = '''
    <div class="panel">
        <div class="panel-heading">
            <h4>Hello</h4>
        </div>
        <div class="panel-body">
            <ul class="list" id="list-1">
                <li class="element">Foo</li>
                <li class="element">Bar</li>
                <li class="element">Jay</li>
            </ul>
            <ul class="list list-small" id="list-2">
                <li class="element">Foo</li>
                <li class="element">Bar</li>
            </ul>
        </div>
    </div>
    '''

    # soup = BeautifulSoup(html, 'lxml')
    # print(soup.prettify())
    # print(soup.title.string)

    soup = BeautifulSoup(html2, 'lxml')
    # find_all，name=ul,可以获取到当前文本中所有ul标签的数据,返回的是一个列表
    # print(soup.find_all(name='ul'))
    # tag类型
    # print(type(soup.find_all(name='ul')[0]))
    # 可以进行嵌套查询
    for ul in soup.find_all(name="ul"):
        for li in ul.find_all(name='li'):
            # tag
            print(li.string)
    print("*" * 100)

    # 通过属性查找匀速
    div = soup.find_all('div', attrs={'class': 'panel'})

    print(len(div))

    print("*" * 120)
    for i in div:
        lis = i.find_all('li', attrs={'class': 'element'})
        print(lis)

    print("*" * 120)

    uls = soup.select('ul.list')
    print(len(uls))
    print(uls)


def get_book_by_bs4():
    session = requests.Session()
    all_data = []
    for i in range(1, 5):
        url = f"http://yushu.talelin.com/book/search?q=javascript&page={i}"
        resp = session.get(url, headers=headers, proxies=proxies)
        content = resp.text

        soup = BeautifulSoup(content, 'lxml')
        all_divs = soup.find_all('div', attrs={'class': 'col-md-7 flex-vertical description-font'})
        print(len(all_divs))

        for div in all_divs:
            try:
                spans = div.find_all('span')
                info_dict = {
                    'title': spans[0].string,
                    'author': spans[1].string.split('/')[0],
                    'press': spans[1].string.split('/')[1],
                    'price': spans[1].string.split('/')[2],
                    'desc': spans[2].string
                }
                all_data.append(info_dict)
            except Exception as e:
                print(e)
                continue

    all_json = json.dumps(all_data, ensure_ascii=False)
    path = os.path.join(os.path.dirname(__file__), 'datas', 'all_books_js.json')
    with open(path, 'w') as f:
        f.write(all_json)


if __name__ == '__main__':
    get_book_by_bs4()
