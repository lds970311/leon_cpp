# coding:utf-8
# time: 2023/5/30
# author: evan
import time

import requests

from proxy_config import proxies, headers

url = 'http://httpbin.org'


def post_test():
    data = {
        'name': 'evan',
        'age': 27
    }

    response = requests.post('http://httpbin.org/post', data=data, headers=headers, proxies=proxies)
    print(response.text)  # "origin": "121.226.89.100",


def test_get_with_params():
    data = {
        'name': 'evan',
        'address': 'Shanghai'
    }

    resp = requests.get(url, params=data, headers=headers, proxies=proxies)
    print(resp.url)  # http://httpbin.org/?name=evan&address=Shanghai
    # print(resp.json())


def get_json():
    resp = requests.get(url + '/ip')
    print(resp.json())


def get_cookie():
    response = requests.get('https://www.baidu.com', headers=headers, proxies=proxies)
    h = response.headers
    for k, v in h.items():
        print(f'{k} : {v}')


def set_cookie():
    cookie = {
        'time': '2021-12-01',
        'address': 'NYC'
    }
    resp = requests.get(url + '/cookies', headers=headers, proxies=proxies, cookies=cookie)
    print(resp.text)

    '''
    {
      "cookies": {
        "address": "NYC", 
        "time": "2021-12-01"
      }
    }
    '''


def save_login_info():
    session = requests.session()
    # 需要提供请求的数据
    login_data = {
        "email": "dazhuang_python@sina.com",
        "password": "abcd1234"
    }

    login_response = session.post(url="http://yushu.talelin.com/login", data=login_data)
    # print(login_response.text)

    # 自动化的带上session,个人的登录凭据信息
    personal_response = session.get(url="http://yushu.talelin.com/personal")
    print(personal_response.text)


def get_auth():
    """
    请求中设置证书
    :return:
    """
    # verify默认是开启的
    # 是一个自签名的证书的网站
    # 当前浏览器是没有这个网站的证书的
    response = requests.get(url="https://218.28.111.252/login.html", verify=False, headers=headers,
                            allow_redirects=True)
    print(response.text)  # requests.exceptions.SSLError: HTTPSConnectionPool


def get_yushu_data():
    session = requests.session()
    for i in range(1, 5):
        time.sleep(1)
        url = f'http://yushu.talelin.com/book/search?q=python&page={i}'
        response = session.get(url, proxies=proxies, headers=headers)
        if response.status_code >= 200:
            content = response.text
            with open(f'./datas/page_{i}.html', 'w', encoding='utf-8') as f:
                f.write(content)
        else:
            print(f'当前{i}页面无法获取')
            continue
    else:
        print('爬去完成')


if __name__ == '__main__':
    # test_get_with_params()
    # get_json()
    # get_cookie()
    # set_cookie()
    # save_login_info()
    # get_auth()
    get_yushu_data()
