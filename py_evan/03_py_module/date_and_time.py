# coding:utf-8
# time: 2023/5/10
# author: evan
# python日起和时间

import time
from datetime import datetime
from datetime import timedelta


def handle_date():
    print(datetime.now())  # 2023-05-10 20:55:44.632015
    before_one_day = timedelta(days=1)
    yesterday = datetime.now() - before_one_day
    strftime = yesterday.strftime('%Y-%m-%d %H:%M:%S')
    print(strftime)  # 2023-05-09 21:31:12
    date = datetime.strptime(strftime, '%Y-%m-%d %H:%M:%S')
    print(type(date))  # <class 'datetime.datetime'>


def handle_time():
    print(time.time())  # 1683726490.5835736
    local_time = time.localtime(time.time())
    print(
        local_time)  # time.struct_time(tm_year=2023, tm_mon=5, tm_mday=10, tm_hour=21, tm_min=49, tm_sec=0, tm_wday=2, tm_yday=130, tm_isdst=0)

    time_str = time.strftime("%H:%M:%S", local_time)
    print(time_str)  # 21:59:53


def time_calc(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"函数 {func.__name__} 执行时间为 {end - start:.6f} 秒")
        return result

    return wrapper


@time_calc
def my_func():
    time.sleep(1)


if __name__ == '__main__':
    handle_date()
    print("-" * 100)
    handle_time()

    my_func()  # 函数 my_func 执行时间为 1.002109 秒
