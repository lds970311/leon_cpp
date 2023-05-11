# coding:utf-8
# time: 2023/5/10
# python异常处理


def upper(data):
    new_str = ''
    try:
        new_str = data.upper()
    except AttributeError as e:
        print('error occurs {}'.format(e))
        new_str = data
    return new_str


def test5():
    try:
        print('1try')
        return 'try'
    except Exception as e:
        print('e')
    finally:
        print('2finally')
        return 'finally'


# 自定义异常
class InputNameError(Exception):

    def __init__(self, msg) -> None:
        self.msg = msg


def input_name(name):
    if name == 'leon':
        raise InputNameError('名称输入错误')
    else:
        print(name)


if __name__ == '__main__':
    print(upper(1))
    print('=====')
    result = test5()
    print(result)  # finally

    input_name('leon')  # __main__.InputNameError: 名称输入错误
