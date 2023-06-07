# coding:utf-8
# time: 2023/6/6
# author: evan
# 验证码识别
import time

import cv2
from selenium import webdriver
from selenium.webdriver.common.by import By

from vcode_utils import get_vcode


def get_capture():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("http://my.cqvip.com/login")
    time.sleep(3)
    driver.implicitly_wait(5)

    input_msg(driver)
    while driver.current_url == "http://my.cqvip.com/login":
        input_msg(driver)


def input_msg(driver):
    img_src = driver.find_element(By.XPATH, '//img[@id="verifycode"]')
    path = "../img/capture.jpg"
    new_path = "../img/capture2.jpg"
    img_src.screenshot(path)
    handle_capture(path, new_path)
    code = get_vcode(path)
    # 输入
    driver.find_element_by_xpath("//input[@id='txtLoginUserName']").send_keys('17673045972')
    driver.find_element_by_xpath("//input[@id='txtLoginPass']").send_keys('ldk2298956224')
    driver.find_element_by_xpath("//input[@id='validatecode']").send_keys(code)
    # 登录
    driver.find_element_by_xpath("//button[@id='btnAccountLogin']").click()
    time.sleep(1)


def handle_capture(path, new_path):
    img = cv2.imread(path)
    thresh, img = cv2.threshold(img, 155, 255, cv2.THRESH_BINARY)
    cv2.imwrite(new_path, img)


if __name__ == '__main__':
    get_capture()
