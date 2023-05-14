# coding:utf-8
# time: 2023/5/12
# author: evan
import json
import os
import random

from Project.gift.commons import error
from base import Base


class User(Base):
    def __init__(self, username, user_json, gift_json):
        self.username = username
        super().__init__(user_json, gift_json)
        self.get_user()
        self.gift_random = list(range(1, 101))

    def get_user(self):
        users = super().read_users()
        if self.username not in users:
            raise error.UserNotFoundError(f"{self.username} 用户不存在！")

        current_user = users.get(self.username)

        if not current_user.get('active'):
            raise error.UserActiveError()

        if current_user.get('role') != 'normal':
            raise error.RoleError("role must be normal!")

        self.user = current_user
        self.role = current_user.get('role')
        self.name = current_user.get('name')
        self.active = current_user.get('active')
        self.create_time = current_user.get('create_time')

    def choice_gift(self):
        self.get_user()

        # level1 get
        first_level, second_level = None, None
        level_one_count = random.choice(self.gift_random)
        if 1 <= level_one_count <= 50:
            first_level = 'level1'
        elif 51 <= level_one_count <= 80:
            first_level = 'level2'
        elif 81 <= level_one_count < 95:
            first_level = 'level3'
        elif level_one_count >= 95:
            first_level = 'level4'
        else:
            raise error.CountError('level_one_count need 0~100')

        gifts = self._Base__read_gifts()
        level_one = gifts.get(first_level)

        level_two_count = random.choice(self.gift_random)

        if 1 <= level_two_count <= 80:
            second_level = 'level1'
        elif 81 <= level_two_count < 95:
            second_level = 'level2'
        elif 95 <= level_two_count < 100:
            second_level = 'level3'
        else:
            raise error.CountError('level_two_count need 0~100')

        level_two = level_one.get(second_level)
        if len(level_two) == 0:
            print('哦可惜 您没有中奖')
            return

        gift_names = []
        for k, _ in level_two.items():
            gift_names.append(k)

        gift_name = random.choice(gift_names)
        gift_info = level_two.get(gift_name)
        if gift_info.get('count') <= 0:
            print('哦可惜 您没有中奖')
            return
        self.update_gift(first_level, second_level, gift_name)
        self.user['gifts'].append(gift_name)
        self.update()
        print('恭喜您 获得 %s 奖品' % gift_name)

    def update(self):
        users = self.read_users()
        users[self.username] = self.user

        self._Base__save_data(json.dumps(users), self.user_json)

    def get_gifts(self):
        gifts = self.get_all_gifts()
        gift_lists = []
        for level1, level1_pool in gifts.items():
            for level2, level2_pool in level1_pool.items():
                for name, val in level2_pool.items():
                    gift_lists.append(name)

        print(gift_lists)
        return gift_lists


if __name__ == '__main__':
    gift_path = os.path.join(os.getcwd(), "storage/gift.json")
    user_path = os.path.join(os.getcwd(), "storage/user.json")
    user = User('Ada', user_path, gift_path, )
    # print(user.create_time)
    user.choice_gift()
