# coding:utf-8
# time: 2023/6/8
# author: evan

import base64
import time

import js2py
import requests

from proxy_config import proxies


def get_response():
    data = {
        'scode': '000001-SZE',
        'sdate': '2022-06-08',
        'edate': '2023-06-08',
        'ctype': "0"
    }

    jsExec = js2py.EvalJs()

    with open('./index.js', 'r') as f:
        content = f.read()

    jsExec.execute(content)

    def get_enc_key():
        timestamp = int(time.time())
        res_code = base64.b64encode(str(timestamp).encode('utf-8')).decode()
        print(res_code)
        return res_code

    headers = {
        'Referer': 'http://webapi.cninfo.com.cn/',
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
        "Accept-EncKey": get_enc_key()
    }

    print(headers)
    response = requests.post("http://webapi.cninfo.com.cn/api/sysapi/p_sysapi1008", data=data, headers=headers,
                             proxies=proxies)
    print(response.json())


if __name__ == '__main__':
    get_response()
