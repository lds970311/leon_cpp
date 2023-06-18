# coding:utf-8
# time: 2023/6/17
# author: evan


import base64
import json
import time

import requests
from Crypto.Cipher import PKCS1_v1_5 as PKCS1_cipher
from Crypto.PublicKey import RSA

from proxy_config import proxies


def encrypt(plaintext, public_key):
    plaintext = plaintext.encode()
    cipher = PKCS1_cipher.new(public_key)
    ciphertext = cipher.encrypt(plaintext)
    ciphertext = base64.b64encode(ciphertext).decode()
    return ciphertext


public_key = """-----BEGIN PUBLIC KEY-----
MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQCeiLxP4ZavN8qhI+x+whAiFpGWpY9y1AHSQC86qEMBVnmqC8vdZAfxxuQWeQaeMWG07lXhXegTjZ5wn9pHnjg15wbjRGSTfwuZxSFW6sS3GYlrg40ckqAagzIjkE+5OLPsdjVYQyhLfKxj/79oOfjl/lV3rQnk/SSczHW0PEyUbQIDAQAB
-----END PUBLIC KEY-----"""

public_key = RSA.importKey(public_key)

mobile = encrypt("15020287777", public_key)
pwd = encrypt("wsh07301432", public_key)
url = "https://gateway.36kr.com/api/mus/login/byMobilePassword"
data = {
    "krtoken": "",
    "param": {
        "countryCode": "86",
        "mobileNo": mobile,
        "password": pwd
    },
    "partner_id": "web",
    "timestamp": int(time.time() * 1000)
}
data = json.dumps(data)
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36",
    "referer": "https://36kr.com/",
    "Content-Type": "application/json"
}
response = requests.post(url, headers=headers, proxies=proxies, data=data)
print(response.json())
