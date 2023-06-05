# coding:utf-8
# time: 2023/6/4
# author: evan

import cv2 as cv


def read_img():
    img = cv.imread("../img/bg_grayscale.jpg", flags=cv.IMREAD_COLOR)
    cv.imshow("mypng", img)

    cv.waitKey(0)
    cv.destoryAllWindows()


if __name__ == '__main__':
    read_img()
