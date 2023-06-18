# coding:utf-8
# time: 2023/6/17
# author: evan
import hashlib
import random

import requests

arr = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "a", "b", "c", "d", "e", "f"]
nonce = ""
for i in range(9):
    rand = random.randint(0, 15)
    nonce += arr[rand]

h = "/xdnphb/main/v1/weibo_day/rank?AppKey=joker&end=2023-04-14&rank_name=个人认证&rank_name_group=&start=2023-04-14&nonce=" + nonce
xyz = hashlib.md5(h.encode()).hexdigest()

url = "https://www.newrank.cn/xdnphb/main/v1/weibo_day/rank"
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36"
}
data = {
    "end": "2023-04-14",
    "rank_name": "个人认证",
    "rank_name_group": "",
    "start": "2023-04-14",
    "nonce": nonce,
    "xyz": xyz
}
res = requests.post(url, headers=headers, data=data)
print(res.text)
