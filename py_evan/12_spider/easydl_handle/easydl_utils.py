# coding:utf-8
# time: 2023/6/6
# author: evan


from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time
import requests
from easydl_test import get_recognized_postition


def get_vcode_jpg():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://passport.jd.com/uc/login")

    select = driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div[1]/div/div[3]/a')
    select.click()

    username = driver.find_element(By.XPATH, '//*[@id="loginname"]')
    ActionChains(driver).pause(0.5).click(username).send_keys("15020287777").perform()

    password = driver.find_element(By.XPATH, '//*[@id="nloginpwd"]')
    ActionChains(driver).pause(0.5).click(password).send_keys("wsh07301432").perform()

    submit = driver.find_element(By.XPATH, '//*[@id="loginsubmit"]')
    submit.click()

    for i in range(30):
        time.sleep(1)
        img = driver.find_element(By.XPATH, '/html/body/div[4]/div/div/div/div[1]/div[2]/div[1]/img')
        img.screenshot("../img3/{}.jpg".format(i))
        time.sleep(0.5)
        refresh = driver.find_element(By.XPATH, '/html/body/div[4]/div/div/div/div[1]/div[1]/div[2]')
        refresh.click()

    time.sleep(3)
    driver.quit()


def get_douban_vcode():
    driver = webdriver.Chrome()
    driver.get("https://www.douban.com/")
    time.sleep(2)

    frame = driver.find_element(By.XPATH, '//*[@id="anony-reg-new"]/div/div[1]/iframe')
    driver.switch_to.frame(frame)
    time.sleep(0.5)

    select = driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/ul[1]/li[2]')
    select.click()

    username = driver.find_element(By.XPATH, '//*[@id="username"]')
    ActionChains(driver).pause(0.5).click(username).send_keys("15020287777").perform()

    password = driver.find_element(By.XPATH, '//*[@id="password"]')
    ActionChains(driver).pause(0.5).click(password).send_keys("wsh07301432").perform()

    submit = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[1]/div[5]/a')
    submit.click()

    time.sleep(2)
    driver.switch_to.frame("tcaptcha_iframe_dy")

    img = driver.find_element(By.XPATH, '//*[@id="slideBg"]')
    img.screenshot('../img3/captcha.png')

    time.sleep(3)
    driver.quit()


if __name__ == '__main__':
    #  get_recognized_postition("../img3/2.jpg")
    get_douban_vcode()
