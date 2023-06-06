# coding:utf-8
# time: 2023/6/6
# author: evan
import base64

import requests

headers = {
    'Content-Type': 'application/json',
    'Accept': 'application/json',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36'
}

api_key = "yH0hDgm2w7hwgI9P5WmE2LwK"
secret_key = "1pBj9AlSFboCfNZ0WSDzs0uUH9DcLk7O"


def get_token():
    url = f"https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id={api_key}&client_secret={secret_key}"
    payload = ""
    response = requests.request("POST", url, headers=headers, data=payload)
    return response.json()['access_token']


def get_vcode(path):
    '''
    通用文字识别（高精度版）
    '''

    request_url = "https://aip.baidubce.com/rest/2.0/ocr/v1/accurate_basic"
    # 二进制方式打开图片文件
    f = open(path, 'rb')
    img = base64.b64encode(f.read())

    params = {"image": img}
    access_token = get_token()
    request_url = request_url + "?access_token=" + access_token
    headers = {'content-type': 'application/x-www-form-urlencoded'}
    response = requests.post(request_url, data=params, headers=headers)
    if response:
        print(response.json())

    return response.json()['words_result'][0]['words']


if __name__ == '__main__':
    print(get_vcode('../img/03.jpg'))
