# coding:utf-8
# time: 2023/5/17
from Project.news_system.db.news_dao import NewsDao
from Project.news_system.db.redis_dao import RedisNewsDao


class NewsService:
    __news_dao = NewsDao()
    __redis_dao = RedisNewsDao()

    def search_unreview_list(self, page):
        return self.__news_dao.search_unreview_list(page)

    def search_unreview_count_page(self):
        return self.__news_dao.search_unreview_count_page()

    def update_unreview_news(self, news_id):
        return self.__news_dao.update_unreview_news(news_id)

        # 查询新闻列表

    def search_list(self, page):
        result = self.__news_dao.search_list(page)
        return result

        # 查询新闻总页数

    def search_count_page(self):
        count_page = self.__news_dao.search_count_page()
        return count_page

        # 删除新闻

    def delete_by_id(self, id):
        self.__news_dao.delete_by_id(id)

    def insert(self, title, editor_id, type_id, content_id, is_top):
        self.__news_dao.insert(title, editor_id, type_id, content_id, is_top)

    def search_cache(self, news_id):
        """
        查询缓存记录
        :param news_id:
        :return:
        """
        return self.__news_dao.search_cache(news_id)

    def cache_news(self, id, title, username, type, content, is_top, create_time):
        self.__redis_dao.insert(id, title, username, type, content, is_top, create_time)

    def delete_cache(self, id):
        """
        删除缓存的新闻
        :param id:
        :return:
        """
        self.__redis_dao.delete_cache(self, id)

    def search_by_id(self, news_id):
        return self.__news_dao.search_by_id(news_id)

    def update(self, news_id, new_title, type_id, content_id, new_is_top):
        """
        更新新闻
        :param news_id:
        :param new_title:
        :param type_id:
        :param content_id:
        :param new_is_top:
        :return:
        """
        self.__news_dao.update_news(news_id, new_title, type_id, content_id, new_is_top)
        self.delete_cache(news_id)
