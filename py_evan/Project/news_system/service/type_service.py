# coding:utf-8
# time: 2023/5/19
# author: evan
from Project.news_system.db.type_dao import TypeDao


class TypeService:
    __type_dao = TypeDao()

    def search_list(self):
        return self.__type_dao.search_list()
