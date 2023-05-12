# coding:utf-8
# time: 2023/5/11
# author: evan
# Python高阶函数


import base64
import hashlib
import time

base_sign = 'muke'


def custom():
    a_timestamp = int(time.time())
    _token = '%s%s' % (base_sign, a_timestamp)
    hashobj = hashlib.sha1(_token.encode('utf-8'))
    a_token = hashobj.hexdigest()
    return a_token, a_timestamp


def b_service_check(token, timestamp):
    _token = '%s%s' % (base_sign, timestamp)
    b_token = hashlib.sha1(_token.encode('utf-8')).hexdigest()
    if token == b_token:
        return True
    else:
        return False


replace_one = '%'
replace_two = '$'


def encode(data: str or bytes) -> str:
    if isinstance(data, str):
        data = data.encode('utf-8')
    elif isinstance(data, bytes):
        data = data
    else:
        raise TypeError('data need bytes or str')

    _data = base64.encodebytes(data).decode('utf-8')
    print(_data)
    _data = _data.replace('a', replace_one).replace('2', replace_two)
    return _data


def decode(data: bytes) -> str:
    if not isinstance(data, bytes):
        raise TypeError('data need bytes')
    replace_one_b = replace_one.encode('utf-8')
    replace_two_b = replace_two.encode('utf-8')
    data = data.replace(replace_one_b, b'a').replace(replace_two_b, b'2')
    return base64.decodebytes(data).decode('utf-8')


if __name__ == '__main__':
    '''
        need_help_token, timestamp = custom()
        time.sleep(1)
        result = b_service_check(need_help_token, int(time.time()))
        if result:
            print('a合法，b服务可以进行帮助')
        else:
            print('a不合法，b不可进行帮助')
    '''

    result = encode('hello xiaomu')
    print(result)
    new_result = decode(result.encode('utf-8'))
    print(new_result)
