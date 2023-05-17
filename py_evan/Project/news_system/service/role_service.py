# coding:utf-8
# time: 2023/5/17
# author: evan
from Project.news_system.db.role_dao import RoleDao


class RoleService:
    __role_dao = RoleDao()

    def search_list(self):
        return self.__role_dao.search_list()
