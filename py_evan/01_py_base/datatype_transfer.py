# coding:utf-8
# time: 2023/5/9

# 数据类型转换

def transfer():
    num = 123
    str1 = str(num)
    print(str1)

    str2 = "l e o n"
    str_arr = str2.split(" ")
    print(str_arr)  # ['l', 'e', 'o', 'n']

    chs = ['a', 'b', 'c']
    str3 = '.'.join(chs)
    print(str3)


def byte2str():
    b = b'my name is leon'
    print(type(b))  # <class 'bytes'>
    print(b)
    print(dir(b))

    str = b.decode('utf-8')
    print(str)

    time__encode = "time".encode('utf8')
    print(type(time__encode), time__encode)  # <class 'bytes'> b'time'


def list_tuple_set():
    a = [1, 2, 3]
    b = (1, 2, 3)
    c = {1, 2, 3}

    print(tuple(a), set(c))
    print(type(tuple(a)), type(set(c)))  # <class 'tuple'> <class 'set'>
    print(tuple(a) == b)  # True
    print(set(a) == c)  # True

    print(list(b), set(b))
    print(list(c), tuple(c))

    print(list(a))

    print(str(a), type(str(a)))  # '[1, 2, 3]'
    print(str(b), type(str(b)))
    print(str(c), type(str(c)))

    print(list(str(a)))
    print(tuple(str(b)))
    print(set(str(c)))

    _a = str(a)
    _b = list(_a)
    print(_b)


if __name__ == '__main__':
    # transfer()
    # byte2str()
    list_tuple_set()
