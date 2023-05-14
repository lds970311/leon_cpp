# coding:utf-8
# time: 2023/5/12
# author: evan
import os

from base import Base
from commons import error


class Admin(Base):
    def __init__(self, user_json: str, gift_json: str, username: str) -> None:
        super().__init__(user_json, gift_json)
        self.username = username
        self.__get_user()

    def __check(self):
        self.__get_user()
        if self.role != 'admin':
            raise Exception('permission')

    def __get_user(self):
        users = self.read_users()
        current_user = users.get(self.username)
        if current_user is None:
            raise error.UserNotFoundError(f"{self.username} 用户不存在！")
        if not current_user.get('active'):
            raise error.UserActiveError()
        if current_user.get('role') != 'admin':
            raise error.RoleError("你不是admin")
        self.user = current_user
        self.role = current_user.get('role')
        self.name = current_user.get('name')
        self.active = current_user.get('active')

    def add_user(self, username, role):
        self.__check()
        super().write_user(username=username, role=role)

    def update_user_active(self, username: str):
        self.__check()
        super().change_active(username)

    def update_user_role(self, username, role):
        self.__check()
        super().change_role(username, role)

    def add_gift(self, first_level, second_level, gift_name, gift_count):
        self.__check()
        super().write_gift(first_level, second_level, gift_name, gift_count)

    def delete_gift(self, first_level, second_level, gift_name):
        self.__check()
        super().delete_gift(first_level, second_level, gift_name)

    def update_gift(self, first_level: str, second_level: str, gift_name: str, gift_count: int = 1,
                    is_admin=False) -> bool:

        self.__check()
        return super().update_gift(first_level, second_level, gift_name, gift_count, True)


if __name__ == '__main__':
    gift_path = os.path.join(os.getcwd(), "storage/gift.json")
    user_path = os.path.join(os.getcwd(), "storage/user.json")
    admin = Admin(user_path, gift_path, 'leon')
    # admin.get_user()
    admin.add_gift('level1', 'level1', 'Xiaomo 13 Pro', 10)
