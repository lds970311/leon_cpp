# coding:utf-8
# time: 2023/5/10
# Python继承
from typing import Any


class Parent:

    def __init__(self, name) -> None:
        self.name = name

    def talk(self):
        return f'{self.name} is talking'

    def speak(self):
        return f'{self.name} is speaking'

    def running(self):
        return 'running1'


class Parent2:
    def __init__(self, age) -> None:
        self.age = age

    def running(self):
        return 'running2'

    def __setattr__(self, name: str, value: Any) -> None:
        """
        设置成员属性
        :param name: key
        :param value: 值
        :return: null
        """
        if name not in self.__dict__:
            self.__dict__[name] = value

    def __call__(self, *args, **kwargs):
        print(f'args is {kwargs}')  # args is {'type': 'call test'}


class Child(Parent, Parent2):

    def __init__(self, name) -> None:
        super().__init__(name)

    def play(self):
        print(super().talk())
        return f'{self.name} is playing'

    def talk(self):
        return f'child : {self.name} is talking'

    def __str__(self) -> str:
        return f'name: {self.name},age:{self.age}'

    def __getattr__(self, name: str) -> Any:
        print(f'{name} 不存在')


class Test:

    def __init__(self, attr='') -> None:
        super().__init__()
        self.__attr = attr

    def __getattr__(self, key):
        if self.__attr:
            key = '{}.{}'.format(self.__attr, key)
        else:
            key = key
        print(key)
        return Test(key)

    def __call__(self, *args, **kwargs):
        print(f'key is {self.__attr}')


if __name__ == '__main__':
    child = Child("evan")
    print(child.play())
    # # print(child.talk())   # evan is playing
    # # print(child.running())  # running1，左侧的父类函数优先使用
    print(
        Child.__mro__)  # (<class '__main__.Child'>, <class '__main__.Parent'>, <class '__main__.Parent2'>, <class 'object'>)
    print(child)
    # # child.hehe()  # play 不存在
    # child.talk()
    p2 = Parent2(10)
    p2.time = 3.0
    print(p2.time)  # 3.0
    p2(type="call test")  # args is {'type': 'call test'}

    t = Test()
    t.f.s.a()
