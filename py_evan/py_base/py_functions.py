# coding:utf-8
# time: 2023/5/9
# Python函数的定义与使用

my_name = 'leon'


def add(a, b, c=5):
    return a + b + c


def test_args(*args, **kwargs):
    print(args, type(args))  # () <class 'tuple'>
    print(kwargs, type(kwargs))  # {} <class 'dict'>


def arg_type(name: str, age: int = 20, *args: int, **kwargs: str):
    print(name, age)


def change_name():
    # 修改全局变量
    global my_name
    my_name = 'evan'


# 递归函数
def get_sum(num):
    if num == 1:
        return 1
    return num + get_sum(num - 1)


def biarysearch(start, end, array, target):
    if start > end:
        return -1
    mid = (start + end) / 2
    mid = int(mid)
    if array[mid] == target:
        return mid
    if target > array[mid]:
        return biarysearch(mid + 1, end, array, target)
    if target < array[mid]:
        return biarysearch(start, mid - 1, array, target)


def lambda_test():
    f1 = lambda: 1
    print(f1())

    f2 = lambda x, y: x ** y
    print(f2(3, 4))  # 81

    users = [
        {'name': 'dewei'},
        {'name': 'xiaomu'},
        {'name': 'asan'}
    ]
    users.sort(key=lambda x: x['name'])
    print(users)


if __name__ == '__main__':
    # print(add(b=3, a=2))
    test_args(1, 2, 3, name='leon', height=190)
    change_name()
    print(my_name)  # evan
    print(get_sum(100))  # 5050

    arr = [1, 2, 3, 4, 5, 6, 7]
    i = biarysearch(0, len(arr) - 1, arr, 30)
    print(i)

    lambda_test()
