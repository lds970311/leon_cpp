# coding:utf-8
# time: 2023/5/17
from Project.news_system.db.news_dao import NewsDao


class NewsService:
    __news_dao = NewsDao()

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
