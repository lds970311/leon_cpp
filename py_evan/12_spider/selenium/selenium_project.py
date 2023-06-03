# coding:utf-8
# time: 2023/6/2
# author: evan

from pymongo import MongoClient
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait


class LinSpider:
    def __init__(self):
        self.url = "http://sleeve.talelin.com/#/login"
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)
        self.client = MongoClient("localhost", 27017)
        self.client.admin.authenticate('admin', '19970311')

    def login(self):
        self.driver.get(self.url)
        try:
            login_btn = self.driver.find_element_by_xpath("//button[@class='submit-btn']")
            login_btn.click()
        except NoSuchElementException as e:
            print(e)

        ele = WebDriverWait(self.driver, 5, 0.5).until(lambda x: x.find_element_by_class_name("lin-info-left"))
        if ele:
            print('登录成功')
            return True
        else:
            print('登录失败')
            return False

    def click_menu(self):
        self.driver.find_element_by_xpath(
            "//li[@class='subMenuContent el-submenu'][1]/div[@class='el-submenu__title']/span").click()
        self.driver.find_element_by_link_text("订单列表").click()

    def get_data(self, count):
        rows = self.driver.find_elements_by_xpath("//tr[contains(@class,'el-table')]")
        for row in rows:
            order_info = {
                "id": row.find_element_by_xpath("./td[1]").text,
                "order_id": row.find_element_by_xpath("./td[2]").text,
                "order_num": row.find_element_by_xpath("./td[3]").text,
                "price": row.find_element_by_xpath("./td[4]").text,
                "state": row.find_element_by_xpath("./td[5]").text,
            }
            if order_info['id'] != "":
                self.write_to_mongo(order_info)

        if count > 0:
            # 下一页
            self.driver.find_element_by_xpath("//button[@class='btn-next']").click()
            self.get_data(count - 1)

    def write_to_mongo(self, order_info):
        self.client.spiders.order.insert_one(order_info)


if __name__ == '__main__':
    s = LinSpider()
    s.login()
    s.click_menu()
    s.get_data(100)
