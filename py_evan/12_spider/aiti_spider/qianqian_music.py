# coding:utf-8
# time: 2023/6/8
# author: evan
import hashlib
import time

import requests

from proxy_config import proxies


def get_music():
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36",
        "Referer": "https://music.91q.com/player"
    }
    tsid = "T10063773662"
    appid = "16073360"
    ts = int(time.time())
    secret = "0b50b02fd0d73a9c4c8c3a781c30845f"
    sign = f"TSID=T10063773662&appid=16073360&timestamp={ts}" + secret
    sign = hashlib.md5(sign.encode()).hexdigest()

    url = "https://music.91q.com/v1/song/tracklink?sign={}&appid={}&TSID={}&timestamp={}".format(sign, appid, tsid, ts)
    response = requests.get(url, headers=headers, proxies=proxies)
    print(response.json())


if __name__ == '__main__':
    get_music()
