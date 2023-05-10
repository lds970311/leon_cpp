# coding:utf-8
# time: 2023/5/10
# Python装饰器

# 装饰器函数
def check_str(cb):
    def inner(*args, **kwargs):
        res = cb(*args, **kwargs)
        if res == 'ok':
            return f'result is {res}'
        else:
            return f'res is failed {res}'

    return inner


# 被处理函数
@check_str
def test(s):
    return s


class ClsDecorator:
    __name = 'leon'

    @classmethod
    def add(cls, a, b):
        return a + b

    @staticmethod
    def sub(a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    @property
    def height(self):
        return 180

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value


if __name__ == '__main__':
    res = test('ok')
    print(res)  # result is ok

    print(ClsDecorator.add(1, 2))  # result is ok
    print(ClsDecorator.sub(5, 4))  # 1
    dec = ClsDecorator()

    print(dec.name)  # leon
    dec.name = 'hehe'
    print(dec.name)  # hehe
