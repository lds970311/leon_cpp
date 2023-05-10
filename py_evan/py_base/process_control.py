# coding:utf-8
# time: 2023/5/9

# python流程控制


def ifelse():
    number = 20

    if number > 10:
        print('number的值大于10')
    elif 5 < number <= 10:
        print('number的值在5和10之间')
    elif 0 < number <= 5:
        print('number的值是1～5')
    else:
        print('number的值是0或者负数')

    print('finish')

    users = [
        ('dewei', 33, 90),
        ('xiaomu', 10, 99),
        ('xiaoming', 18, 100)
    ]

    xiaoming = ['xiaoming', 19, 90]

    if users[0][0] == xiaoming[0]:
        xiaoming[0] = '%s_new' % xiaoming[0]
        users.append(xiaoming)
    elif users[1][0] == xiaoming[0]:
        xiaoming[0] = '%s_new' % xiaoming[0]
        users.append(xiaoming)
    elif users[2][0] == xiaoming[0]:
        xiaoming[0] = '%s_new' % xiaoming[0]
        users.append(xiaoming)
    else:
        users.append(xiaoming)

    print(users)

    users = {
        'dewei': {'age': 33, 'count': 90},
        'xiaomu': {'age': 10, 'count': 99},
        'xiaoming': {'age': 18, 'count': 100}
    }

    if xiaoming[0] in users:
        xiaoming[0] = '%s_new' % xiaoming[0]
    else:
        users[xiaoming[0]] = {'age': xiaoming[1], 'count': xiaoming[2]}
    print(users)


def iterable_for():
    l = ['dewei', 'xiaomu', 'xiaoman', 'xiaoming']
    for user in l:
        print(user)

    for item in range(5):
        print(item, end=" ")
    else:
        print("")

    for item in range(5, 0, -1):
        print(item)


def iterable_while():
    count = 0
    total = 0

    while count <= 100:
        total += count
        count += 1

        if count == 10:
            print('count 已经 到 10了')
        elif count == 50:
            print('count 已经到 50了')
        elif count == 99:
            print('count 马上就要100了！')

    print(total)

    users = ['dewei', 'xiaomu', 'xiaogang', 'xiaoming']
    index = 0

    while index < len(users):
        print(users[index])
        index += 1

    # while True:
    #     print('xx')


def iterable_handle():
    users = [
        {'username': 'dewei', 'age': 33, 'top': 174, 'sex': '男'},
        {'username': '小慕', 'age': 10, 'top': 175, 'sex': '男'},
        {'username': 'xiaoyun', 'age': 18, 'top': 165, 'sex': '女'},
        {'username': 'xiaogao', 'age': 18, 'top': 188, 'sex': '男'}
    ]

    man = []

    for user in users:
        if user.get('sex') == '女':
            continue
        man.append(user)
        print('%s 加入了帮忙的行列' % user.get('username'))

    print(man)

    l = range(100)

    for i in l:
        if i == 80:
            print('----')
            print('已经循环80次了，程序要退出啦')
        if i == 90:
            print('退出啦！')
            break
        print(i)
    else:
        print('循环正常退出了！')

    print('start hello!')


def nine_plus_nine():
    """
    99乘法表
    :return:
    """
    for i in range(1, 10):
        for j in range(1, i + 1):
            print(f'{i} * {j} = {i * j}', end='  ')
        print()
    print("*" * 100)

    # 方式2
    i = 1
    while i <= 9:
        j = 1
        while j <= i:
            print(f'{j} * {i} = {i * j}', end='  ')
            j += 1
        i += 1
        print()


if __name__ == '__main__':
    # iterable_handle()
    nine_plus_nine()
