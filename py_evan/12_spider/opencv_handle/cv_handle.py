# coding:utf-8
# time: 2023/6/6
# author: evan
import cv2 as cv

img = cv.imread('../img/capture.png', flags=cv.IMREAD_GRAYSCALE)

cv.imshow("myImg", img)
cv.waitKey(0)
cv.destroyAllWindows()
