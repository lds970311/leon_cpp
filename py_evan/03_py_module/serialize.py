# coding:utf-8
# time: 2023/5/11
# author: evan
# python序列化

import json


def serailize_handle():
    a = 10
    b = "hello python"
    c = (1, 5, 7, 4)
    d = {'name': 'leon', 'age': 30}

    print(json.dumps(a))
    print(json.dumps(b))
    print(json.dumps(c))
    print(json.dumps(d))


def deserialize_handle():
    a = '[1,2,3,4]'
    loads = json.loads(a)
    print(type(loads))  # <class 'list'>


if __name__ == '__main__':
    # serailize_handle()
    deserialize_handle()
