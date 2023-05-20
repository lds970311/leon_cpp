# coding:utf-8
# time: 2023/5/17
# author: evan
from Project.news_system.db.user_dao import UserDao


class UserService:
    __user_dao = UserDao()

    def login(self, username, password):
        return self.__user_dao.login(username, password)

    def get_user_role(self, username):
        return self.__user_dao.search_user_role(username)

    def insert(self, username, password, email, role_id):
        return self.__user_dao.insert_user(username, password, email, role_id)

    def search_count_page(self):
        return self.__user_dao.search_count_page()

    def search_list(self, page):
        return self.__user_dao.search_list(page)

    def delete_by_id(self, user_id):
        return self.__user_dao.delete_by_id(user_id)

    def update(self, user_id, username, password, email, role_id):
        return self.__user_dao.update(user_id, username, password, email, role_id)

    def search_userid(self, username):
        """
        查询用户id
        :param username:
        :return:
        """
        return self.__user_dao.search_userid(username)
