# coding:utf-8
# time: 2023/5/9

class Person:
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age
        self.__weight = 60  # 私有属性

    def get_msg(self):
        print(self.name, self.age)

    # 私有方法
    def __lose_weight(self):
        self.__weight -= 10


if __name__ == '__main__':
    person = Person('leon', 40)
    person.get_msg()  # leon 40
    print(dir(person))
