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

    def __get_user(self):
        users = self.read_users()
        current_user = users.get(self.username)
        if current_user is None:
            raise error.UserNotFoundError(f"{self.username} 用户不存在！")
        if not current_user.get('active'):
            raise error.UserActiveError()
        self.user = current_user
        self.role = current_user.get('role')
        self.name = current_user.get('name')
        self.active = current_user.get('active')

    def add_user(self, username, role):
        if self.role != 'admin':
            raise Exception('permission')
        super().write_user(username=username, role=role)


if __name__ == '__main__':
    gift_path = os.path.join(os.getcwd(), "./storage/gift.json")
    user_path = os.path.join(os.getcwd(), "./storage/user.json")
    admin = Admin(user_path, gift_path, 'leon')
    # admin.get_user()
    admin.add_user('evan', 'admin')
