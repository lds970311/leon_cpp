# coding:utf-8
# time: 2023/6/1
# author: evan
import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


def test():
    driver = webdriver.Chrome()
    driver.maximize_window()
    time.sleep(2)
    driver.quit()


def search_in_baidu():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get('https://www.baidu.com')
    input = driver.find_element_by_xpath("//input[@id='kw']")
    input.send_keys('java')
    btn = driver.find_element_by_xpath("//input[@id='su']")
    btn.click()
    time.sleep(10)


def mouse_handle():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get('https://www.baidu.com')
    chains = ActionChains(driver)
    element = driver.find_element_by_link_text('设置')
    # 显示等待
    WebDriverWait(element, 5, 0.5).until(EC.presence_of_element_located(By.ID, 'kw'))
    chains.move_to_element(element)
    chains.perform()
    time.sleep(3)
    driver.quit()


if __name__ == '__main__':
    # search_in_baidu()
    mouse_handle()
