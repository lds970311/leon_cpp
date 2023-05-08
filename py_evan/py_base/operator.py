# coding:utf-8
# time: 2023/5/8
# python运算

def op():
    a = 1
    b = 2
    c = 3

    d = a + b + c
    d += c
    print(d)  # 9

    d -= a
    print(d)  # 8

    d *= b  # d = d * b
    print(d)  # 16

    # a /= b
    # print(a)

    a //= b
    print(a)  # 0

    c %= 3
    print(c)  # 0

    f = 10
    f **= 2
    print(f)  # 100

    list_01 = [1, 2, 3]
    print(list_01 * 2)  # [1, 2, 3, 1, 2, 3]
    tuple_01 = (1, 2, 3)  # (1, 2, 3, 1, 2, 3)
    print(tuple_01 * 2)
    print(tuple_01)

    dict_01 = {'name': 'dewei'}

    gb = 1
    b = gb * 1024 * 1024 * 1024
    print(b)


def compare_op():
    a = 1
    b = 2.2
    c = 0
    d = 18
    d_01 = 18
    e = -3
    f = 300
    f_01 = 300

    print(a == b)  # False
    print(a != b)  # True
    print(a < b)  # True
    print(a > e)  # True
    print(d >= b)  # True
    print(d >= d_01)  # True

    print(d == d_01)  # True
    print(d is d_01)  # True
    print('d id is:', id(d))  # d id is: 9793600
    print('d_01 id is:', id(d_01))  # d_01 id is: 9793600

    print(f == f_01)  # True
    print(f is f_01)  # True

    print(f is d)  # False
    print(id(f))  # 139831360059856
    print(id(d))  # 9793600

    print(f is not d)  # True


if __name__ == '__main__':
    # op()
    compare_op()
