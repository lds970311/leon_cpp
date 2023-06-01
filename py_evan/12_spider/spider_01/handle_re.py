# coding:utf-8
# time: 2023/5/30
# author: evan
import json
import os
import re

import requests

from proxy_config import proxies, headers


def re_handle():
    pattern = re.compile(r'\d+')
    match = pattern.match('one12twothres123', 3)
    print(match.group())

    all = pattern.findall('one12twothres123')
    print(all)

    pattern = re.compile(r'[\s\,\;]+')
    match = pattern.split('a,b;; c  d')
    print(match)  # ['a', 'b', 'c', 'd']

    string = '<h1 class="test">imooc</h1>'
    pattern = re.compile(r'<(.\d)\sclass="(?P<classname>.*?)">.*?</(\1)>')
    match = re.search(pattern, string)
    print(match.group('classname'))
    print(match.group(1))


def handle_search_re(content):
    item_search = re.compile('description-font">.*?</div>', re.S)
    all_item = item_search.findall(content)
    title_pattern = re.compile('title">(.*?)</span>')
    info_pattern = re.compile(r'<span>(.*?)</span>')
    scribe_pattern = re.compile(r'<span class="summary">(.*?)</span>')
    all_list = []
    for item in all_item:
        try:
            info_dict = {
                'title': title_pattern.search(item).group(1),
                'author': info_pattern.search(item).group(1).split('/')[0],
                'press': info_pattern.search(item).group(1).split('/')[1],
                'price': info_pattern.search(item).group(1).split('/')[2],
                'desc': scribe_pattern.search(item).group(1)
            }
            all_list.append(info_dict)
        except Exception as e:
            print(e)
            continue
    return all_list


def write_to_file(path, data):
    with open(path, 'a+', encoding='utf-8') as f:
        f.write(data)


def scribe_yushu():
    '''
    爬去鱼书网的图书信息
    :return:
    '''
    path = os.path.join(os.path.dirname(__file__), 'datas', 'all_books_python.json')
    session = requests.Session()

    all = []
    for i in range(1, 5):
        url = f"http://yushu.talelin.com/book/search?q=python&page={i}"
        response = session.get(url, proxies=proxies, headers=headers)
        res = handle_search_re(response.text)
        all.extend(res)
    data = json.dumps(all, ensure_ascii=False)
    write_to_file(path, data)


if __name__ == '__main__':
    scribe_yushu()
