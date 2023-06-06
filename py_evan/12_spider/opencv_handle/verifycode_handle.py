# coding:utf-8
# time: 2023/6/6
# author: evan
# 验证码识别

from selenium import webdriver

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("http://my.cqvip.com/login")
