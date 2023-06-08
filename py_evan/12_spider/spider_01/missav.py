# coding:utf-8
# time: 2023/6/7
# author: evan
import re
import time

from pymongo import MongoClient
from selenium import webdriver


class MissAvActress(object):
    def __init__(self):
        self.url = "https://missav.com/actresses?page=1"
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)
        self.client = MongoClient('localhost', 27017)
        self.client.admin.authenticate('admin', '19970311')

    def get_pages(self):
        self.driver.get(self.url)
        time.sleep(1)
        self.parse_actress()

    def parse_actress(self):
        # 滚动到页面底部
        self.driver.execute_script("window.scrollTo(0, 300);")
        # info_list = self.driver.find_elements_by_xpath(
        #     "//ul[@class='mx-auto grid grid-cols-2 gap-4 gap-y-8 sm:grid-cols-4 md:gap-6 lg:gap-8 lg:gap-y-12 xl:grid-cols-6 text-center']//li")
        # print(len(info_list))
        # for info in info_list:
        #     # 照片
        #     img_path = info.find_element_by_xpath("./div[@class='space-y-4']//img").get_attribute('src')
        #     actress_link = info.find_element_by_xpath(".//div[@class='space-y-2']/a").get_attribute('href')
        #     actress_name = info.find_element_by_xpath(".//div[@class='space-y-2']/a/h4").text
        #     video_num = info.find_element_by_xpath(".//div[@class='space-y-2']/a/p[1]").text.split(" ")[0]
        #     year = info.find_element_by_xpath(".//div[@class='space-y-2']/a/p[1]").text.split(" ")[0]
        #     data = {
        #         'name': actress_name,
        #         'avatar': img_path,
        #         'actress_movies': actress_link,
        #         'movie_num': int(video_num),
        #         'exceed_year': int(year)
        #     }
        #     print(data)

        next = self.driver.find_element_by_xpath("//a[@rel='next']")
        if next is not None:
            pattern = re.compile('\?page=(\d+)')
            current_page = pattern.findall(self.url)[0]
            next_page = int(current_page) + 1
            self.url = f"https://missav.com/actresses?page={next_page}"
            next.click()
            self.parse_actress()


def write_to_mongodb(self, data):
    self.client.spiders.actress.insert_one(data)


def __del__(self):
    self.driver.quit()


if __name__ == '__main__':
    actress = MissAvActress()
    actress.get_pages()
