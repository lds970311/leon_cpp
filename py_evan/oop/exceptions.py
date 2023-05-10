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


if __name__ == '__main__':
    print(upper(1))
