# coding:utf-8
# time: 2023/5/11
# author: evan
# python常用函数

import random


class Test(object):
    a = 1
    b = 2

    def __init__(self):
        self.a = self.a
        self.b = self.b


test = Test()
print(test.a)
result = vars(test)  #
print(result)  # {'a': 1, 'b': 2}

print(hasattr(test, 'a'))  # True
print(hasattr(list, 'appends'))  # False

setattr(test, 'c', 3)
print(test.c)
print(vars(test))  # {'a': 1, 'b': 2, 'c': 3}

# setattr(list, 'c', 1)
if hasattr(list, 'appends'):
    print(getattr(list, 'appends'))
else:
    print('不能存在')

a = ['', None, True, 0]
print(any(a))


# all - > and
# any - > or

def random_test():
    a = random.random()
    print(a)  # 0.8507873701094374
    b = random.randint(1, 100)
    print(b)  # 8
    item = random.choice(['a', 'b', 'c'])
    print(item)  # c
    item2 = random.sample((7, 8, 9), 2)
    print(item2)  # [9, 8]


if __name__ == '__main__':
    print('-' * 100)
    random_test()
