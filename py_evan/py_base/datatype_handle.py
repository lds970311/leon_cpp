# coding:utf-8
# time: 2023/5/8

# 字符串，列表，元祖，字典的操作


def str1():
    name = 'xiao mu'
    info = 'hello 小慕'
    _info = '小慕 hello'
    number_str = '1314'

    new_name = name.capitalize()
    new_info = info.capitalize()
    _new_info = _info.capitalize()
    new_number_str = number_str.capitalize()

    print(new_name, name)
    print(new_info, info)
    print(_new_info)
    print(new_number_str)


def str2():
    message_en = 'How do you do? Xiaomu'
    message_ch = '你好呀, XiaoMu'
    message_mix = '你好呀，Xiaomu, 今天是星期3！'

    message_en_lower = message_en.lower()
    message_en_casefold = message_en.casefold()

    message_ch_lower = message_ch.lower()
    message_ch_casefold = message_ch.casefold()

    message_mix_lower = message_mix.lower()
    message_mix_casefold = message_mix.casefold()

    print(message_en_lower, message_en_casefold, message_en)
    print(message_ch_lower, message_ch_casefold)
    print(message_mix_lower, message_mix_casefold)

    empty = ''
    empty_lower = empty.lower()
    empty_casefold = empty.casefold()

    print('.' + empty_lower + '.', '.' + empty_casefold + '.')


def str3():
    s = "abc"
    res = s.zfill(10)
    print(res)  # 0000000abc

    s2 = "aabbccdddd"
    count = s2.count("d")
    print(count)  # 4


def str4():
    s = "what day is today"
    startswith = s.startswith("s")
    endswith = s.endswith("y")

    print(startswith, endswith)

    find = s.find('day')
    index = s.index("is")
    print(find, index)

    s2 = ' hello py '
    print(s2.strip())  # hello py

    s = s.replace('t', 'a', 2)
    print(s)
    print(s.isspace())  # False


def list1():
    lst = [1, 2]
    lst.append(3)
    print(lst)
    lst.insert(1, 4)
    print(lst)
    cnt = lst.count(1)
    print(cnt)  # 1
    lst.remove(1)
    print(lst)  # [4, 2, 3]
    lst.reverse()
    print(lst)  # [3, 2, 4]
    lst.sort()
    print(lst)  # [2, 3, 4]
    lst.clear()
    # print(lst) # []
    lit2 = lst.copy()
    print(id(lst), id(lit2))  # 140503809507648 140503809510016
    lit2.extend((7, 8, 9))
    print(lit2)  # [7, 8, 9


def list_index():
    """
        列表的索引
    :return:
    """
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(len(numbers) - 1)
    print(numbers[9])
    print(id(numbers))
    print('获取列表完整数据：', numbers[:])
    print('另一种获取完整列表的方法：', numbers[0:])
    print('第三种获取列表的方法：', numbers[0:-1])
    print('列表的反序:', numbers[::-1])
    print('列表的反项获取', numbers[-3:-1])
    print('步长获取切片:', numbers[0: 8: 2])
    print('切片生成空列表', numbers[0: 0])
    new_numbers = numbers[: 4]
    print(new_numbers)

    numbers[3] = 'code'
    print(numbers)
    numbers[2: 5] = ['a', 'b', 'c']
    print(numbers)

    item = numbers.pop(4)
    print(item, numbers, len(numbers))

    del numbers[4]
    print(numbers)

    tuple_test = (1, 2, 3)
    del tuple_test


def str_index():
    s1 = "time to live"
    res = s1[:-1]
    print(res)
    # s1[0] = 'a' # str' object does not support item assignment
    print(res)
    target = s1[s1.find("to"):]
    print(target)


def dict_update():
    user = {'username': 'dewei', 'age': 33}
    xiaomu = {'username': '小慕', 'age': 10, 'top': 175, 'sex': '男'}
    user.update(xiaomu)
    print(user)

    value = user.setdefault('username', 'xiaoyun')
    value = user.setdefault('birthday', '2020-1-1')
    print(user, value)


def dict_handle():
    project = {'id': 1, 'project_name': 'ipad', 'price': 2200, 'count': 30}
    keys = project.keys()
    print(type(keys))  # <class 'dict_keys'>
    # 获取value
    project_name = project.get('project_name')
    price = project['price']
    print(f'{project_name}, {price}')  # ipad, 2200
    project.pop('count')
    print(project)
    pro = project.copy()
    print(pro)
    pop = pro.popitem()
    print(pop)  # ('price', 2200)
    vals = pro.values()
    print(f'vals={vals},type={type(vals)}')  # vals=dict_values([1, 'ipad']),type=<class 'dict_values'>
    items = pro.items()
    print(
        f'items={items},type={type(items)}')  # items=dict_items([('id', 1), ('project_name', 'ipad')]),type=<class 'dict_items'>


def set_handle():
    s = {1, 2, 3}

    # 向集合中添加一个元素
    s.add(4)

    # 向集合中添加多个元素
    s.update([5, 6, 7])
    print(s)  # {1, 2, 3, 4, 5, 6, 7}
    # 从集合中删除一个元素
    s.remove(4)

    # 从集合中删除多个元素
    s.discard(3)
    print(s)  # {1, 2, 5, 6, 7}


def set_handle2():
    s1 = {1, 2, 3, 4}
    s2 = {3, 4, 5, 6}
    difference = s1.difference(s2)  # {1, 2}
    print(difference)
    intersection = s1.intersection(s2)
    union = s1.union(s2)
    print(intersection)  # {3, 4}
    print(union)  # {1, 2, 3, 4, 5, 6}
    isdisjoint = s1.isdisjoint(s2)
    print(isdisjoint)  # False


if __name__ == '__main__':
    # str4()
    # list1()
    # list_index()
    # str_index()
    # dict_update()
    # dict_handle()
    # set_handle()
    set_handle2()
