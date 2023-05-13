# coding:utf-8
# time: 2023/5/12
# author: evan
import json
import os
import time
from typing import Any

from commons import error
from commons import utils
from commons.constants import ROLES, FIRST_LEVAL


class Base:
    def __init__(self, user_json: str, gift_json: str) -> None:
        self.user_json = user_json
        self.gift_json = gift_json
        self.__check_user_json()
        self.__check_gift_json()
        self.__init_gifts()

    def __check_user_json(self):
        utils.check_file(self.user_json)

    def __check_gift_json(self):
        utils.check_file(self.gift_json)

    def read_users(self, time_to_str=False):
        with open(self.user_json, "r") as f:
            data = json.loads(f.read())
            if time_to_str:
                for k, v in data.items():
                    v['create_time'] = utils.timestamp2string(v['create_time'])
                    v['update_time'] = utils.timestamp2string(v['update_time'])
                    data[k] = v
        return data

    def __read_gifts(self):
        with open(self.gift_json, 'r') as f:
            data = json.loads(f.read())
        return data

    def __init_gifts(self):
        data = {
            'level1': {
                'level1': {},
                'level2': {},
                'level3': {}
            },
            'level2': {
                'level1': {},
                'level2': {},
                'level3': {}

            },
            'level3': {
                'level1': {},
                'level2': {},
                'level3': {}

            },
            'level4': {
                'level1': {},
                'level2': {},
                'level3': {}
            },
        }
        gifts = self.__read_gifts()
        if len(gifts) != 0:
            return
        json_data = json.dumps(data)
        with open(self.gift_json, 'w') as f:
            f.write(json_data)

    def __save_data(self, data, path):
        with open(path, 'w') as f:
            f.write(data)

    def write_gift(self, first_level, second_level, gift_name, gift_count):
        if first_level not in FIRST_LEVAL or second_level not in FIRST_LEVAL:
            raise error.LevelError("礼物等级不符合要求，格式：level1/level2")

        if gift_count <= 0:
            raise ValueError("gift_count应该大于等于1")

        gitfs = self.__read_gifts()
        first_pool = gitfs[first_level]
        second_pool = first_pool[second_level]
        if gift_name in second_pool:
            second_pool[gift_name]['count'] += gift_count
        else:
            gitfs[first_level][second_level][gift_name] = {
                'name': gift_name,
                'count': gift_count
            }
        gift_data = json.dumps(gitfs)
        self.__save_data(gift_data, self.gift_json)

    def update_gift(self, first_level: str, second_level: str, gift_name: str, gift_count: int = 1) -> bool:
        if first_level not in FIRST_LEVAL or second_level not in FIRST_LEVAL:
            raise error.LevelError("礼物等级不符合要求，格式：level1/level2")
        gifts = self.__read_gifts()
        first_pool = gifts[first_level]
        second_pool = first_pool[second_level]
        if gift_name not in second_pool:
            return False
        if second_pool[gift_name]['count'] - gift_count < 0:
            return False
        second_pool[gift_name]['count'] -= gift_count
        self.__save_data(json.dumps(gifts), self.gift_json)
        return True

    def delete_gift(self, first_level: str, second_level: str, gift_name: str) -> Any:
        if first_level not in FIRST_LEVAL or second_level not in FIRST_LEVAL:
            raise error.LevelError("礼物等级不符合要求，格式：level1/level2")
        gifts = self.__read_gifts()
        first_pool = gifts[first_level]
        second_pool = first_pool[second_level]
        if gift_name not in second_pool:
            return False
        del_data = second_pool.pop(gift_name)
        self.__save_data(json.dumps(gifts), self.gift_json)
        return del_data

    def write_user(self, **user):
        if 'username' not in user:
            raise ValueError('missing username')
        if 'role' not in user:
            raise ValueError('missing role')
        user['active'] = True
        user['create_time'] = utils.timestamp2string(time.time())
        user['update_time'] = utils.timestamp2string(time.time())
        user['gifts'] = []

        usrs = self.read_users()
        if user['username'] in usrs:
            raise error.UserExistsError(f"{user['username']} 已经存在")

        usrs.update(
            {user['username']: user}
        )

        json_user = json.dumps(usrs)
        self.__save_data(json_user, self.user_json)

    def change_role(self, username: str, role: str) -> bool:
        users = self.__read_users()
        m_user = users.get(username)
        if not m_user:
            return False
        if role not in ROLES:
            raise error.RoleError(f'{role} 名称不合法！')
        m_user['role'] = role
        m_user['update_time'] = utils.timestamp2string(time.time())
        users[username] = m_user
        json_data = json.dumps(users)
        self.__save_data(json_data, self.user_json)
        return True

    def change_active(self, username: str) -> bool:
        users = self.__read_users()
        user = users.get(username)
        if not user:
            return False

        user['active'] = not user['active']
        user['update_time'] = utils.timestamp2string(time.time())
        users[username] = user
        json_data = json.dumps(users)
        self.__save_data(json_data, self.user_json)
        return True

    def delete_user(self, username: str):
        users = self.__read_users()
        user = users.get(username)
        if not user:
            return False
        deleted_user = users.pop(username)
        json_data = json.dumps(users)
        self.__save_data(json_data, self.user_json)
        return deleted_user


if __name__ == '__main__':
    gift_path = os.path.join(os.getcwd(), "./storage/gift.json")
    user_path = os.path.join(os.getcwd(), "./storage/user.json")
    base = Base(user_path, gift_path)
    # base.write_user(username='leon', role='admin')
    # print(base.change_role('leon', 'normal'))
    # print(base.change_active('leon'))
    # print(base.delete_user('leon'))
    # base.write_gift('level1', 'level1', 'iPhone 14 Pro Max', 1)
    # base.write_gift('level1', 'level2', 'iPhone 14 Pro', 2)
    # base.write_gift('level1', 'level3', 'iPhone 14', 3)
    # base.write_gift('level2', 'level1', 'iPhone 13 Pro', 4)
    # base.update_gift('level1', 'level2', 'iPhone 14 Pro')
    base.delete_gift('level2', 'level2', "iPhone 12 Pro")
