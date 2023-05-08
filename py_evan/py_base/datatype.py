# coding:utf-8
# time: 2023/5/7

def str_handle():
    m = max("abc")
    n = min("abc")

    b = "a" in "abc"

    print(m)
    print(n)
    print(b)


def list_handle():
    none_list = [None, None, None]

    print(none_list)
    print(bool(none_list))
    print(len(none_list))
    print([])
    print(bool([]))

    max_list = [1, 3.14]
    print(max_list)
    print(max(max_list))
    print(min(max_list))

    id_address = id(max_list)
    print(id_address)


def tuple_handle():
    tuple_test = (1, 2, 3)
    print(tuple_test)
    print(type(tuple_test))

    tuple_01 = ()
    print(type(tuple_01))

    print(bool((1,)))  # True
    print(len(tuple_01))  # 0

    max_count = max(tuple_test)
    print(max_count)  # 3
    min_count = min(tuple_test)
    print(min_count)  # 1


def dict_handle():
    user_info = {'name': 'leon同学', 'age': 10, 'top': '180cm'}

    result = 'name' in user_info  # True
    print(result)

    result = 'hope' in user_info
    print(result)  # False
    result = 'hope' not in user_info
    print(result)  # True

    count = len(user_info)
    print(count)  # 3

    result_bool = bool(user_info)
    print(result_bool)  # True
    empty_dict = {}
    print(bool(empty_dict))  # False
    print('name' in user_info)  # True


if __name__ == '__main__':
    num = 100
    f = 10.23
    name = "leon"
    is_empt = False
    b = None

    print(type(num))
    print(type(f))
    print(type(name))
    print(type(is_empt))  # <class 'bool'>

    # str_handle()
    # list_handle()
    # tuple_handle()
    dict_handle()
