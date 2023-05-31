# coding:utf-8
# time: 2023/5/30
# author: evan
import os

import requests

from proxy_config import proxies, headers

# target_url = "https://dev.kdlapi.com/testproxy"
url = 'https://www.hao123.com'

# 使用隧道域名发送请求
response = requests.get(url, proxies=proxies, headers=headers)


def write_resp(path: str, data):
    with open(path, 'w') as f:
        f.write(data)


if __name__ == '__main__':

    # 获取页面内容
    if response.status_code == 200:
        # print(response.text)  # 请勿使用keep-alive复用连接(会导致隧道不能切换IP)
        path = os.path.join(os.path.dirname(__file__), 'hao123.html')
        write_resp(path, response.text)
