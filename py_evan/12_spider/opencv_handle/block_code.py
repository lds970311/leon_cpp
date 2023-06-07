# coding:utf-8
# time: 2023/6/6
# author: evan
# 滑块验证码的处理
import os

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from vcode_utils import headers, get_vcode
import cv2
import time
import requests


def get_block_code():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.liepin.com/")
    time.sleep(3)
    driver.implicitly_wait(5)

    # 切换密码登录
    driver.find_element_by_xpath('//*[@id="home-banner-login-container"]/div/div/div/div/div[2]/div/div[2]').click()

    # 输入用户名密码
    driver.find_element_by_xpath('//input[@id="login"]').send_keys('17673045972')
    driver.find_element_by_xpath('//input[@id="pwd"]').send_keys('ldk2298956224!')
    driver.find_element_by_xpath(
        '//*[@id="home-banner-login-container"]/div/div/div/div/div[4]/div/label/span[1]/input').click()

    # 点击登录
    driver.find_element_by_xpath(
        '//*[@id="home-banner-login-container"]/div/div/div/div/div[3]/div/form/button').click()

    time.sleep(3)

    driver.switch_to.frame("tcaptcha_iframe")
    while driver.current_url == "https://www.liepin.com/":
        # 点击刷新
        refresh_btn = driver.find_element_by_xpath('//*[@id="reload"]/div')
        refresh_btn.click()
        time.sleep(1)
        # 获取验证码
        img = driver.find_element_by_xpath('//img[@id="slideBg"]').get_attribute('src')
        block = driver.find_element_by_xpath('//img[@id="slideBlock"]').get_attribute('src')

        # 下载两个图
        res1 = requests.get(img, headers=headers)
        with open('../img/img.jpg', 'wb') as f:
            f.write(res1.content)

        res2 = requests.get(block, headers=headers)
        with open('../img/block.jpg', 'wb') as f:
            f.write(res2.content)

        time.sleep(1)

        distance = handle_image()
        drag_element = driver.find_element_by_xpath("//div[@id='tcaptcha_drag_thumb']")
        actions = ActionChains(driver)
        actions.pause(0.3).click_and_hold(drag_element).move_by_offset(distance, 0).release()
        actions.click(drag_element)
        actions.perform()
        delete_imgs()
        time.sleep(2)


def handle_image():
    back = cv2.imread("../img/block.jpg", flags=cv2.IMREAD_GRAYSCALE)
    img = cv2.imread("../img/img.jpg", flags=cv2.IMREAD_GRAYSCALE)

    print(back.shape)
    back = back[20:back.shape[0] - 20, 20:back.shape[0] - 20]
    thresh, back = cv2.threshold(back, 110, 255, cv2.THRESH_BINARY)
    thresh, img = cv2.threshold(img, 40, 255, cv2.THRESH_BINARY_INV)

    cv2.imwrite("../img/block2.jpg", back)
    cv2.imwrite("../img/img2.jpg", img)

    match = cv2.matchTemplate(back, img, cv2.TM_CCORR_NORMED)
    loc = cv2.minMaxLoc(match)[3]
    print(loc)
    distance = loc[0] * 341 // 680 - 37
    print(distance)
    return distance


def delete_imgs():
    folder_path = '../img'  # 图片文件夹路径

    # 获取文件夹中以 img 和 block 开头的文件
    files = [file for file in os.listdir(folder_path) if file.startswith(('img', 'block'))]
    print(files)
    for file in files:
        file_path = os.path.join(folder_path, file)
        os.remove(file_path)


if __name__ == '__main__':
    get_block_code()
# delete_imgs()
