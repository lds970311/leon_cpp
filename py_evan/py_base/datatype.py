# coding:utf-8
# time: 2023/5/7

def str_handle():
    m = max("abc")
    n = min("abc")

    b = "a" in "abc"

    print(m)
    print(n)
    print(b)


if __name__ == '__main__':
    num = 100
    f = 10.23
    name = "leon"

    print(type(num))
    print(type(f))
    print(type(name))

    str_handle()
