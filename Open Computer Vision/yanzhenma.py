#encoding:utf-8
# File: yanzhenma.py
# Author:fbi
# Time: 20/12/29
import cv2 as cv
import pytesseract
from PIL import Image
import numpy as np

def recognize_text2(image):
    # 边缘保留滤波  去噪
    blur = cv.pyrMeanShiftFiltering(image, sp=8, sr=60)
    # cv.imshow('dst', blur)
    # 灰度图像
    gray = cv.cvtColor(blur, cv.COLOR_BGR2GRAY)
    # 二值化
    ret, binary = cv.threshold(gray, 0, 255, cv.THRESH_BINARY_INV | cv.THRESH_OTSU)
    print(f'二值化自适应阈值：{ret}')
    cv.imshow('binary', binary)
    kernel = 1/16*np.array([[1,2,1],[2,4,2],[1,2,1]])
    bin2 = cv.filter2D(binary,-1,kernel)
    ret, bin3 = cv.threshold(bin2, 0, 255, cv.THRESH_BINARY_INV | cv.THRESH_OTSU)

    cv.bitwise_not(bin3, bin3)
    cv.imshow('binary-image', bin3)
    # 识别
    test_message = Image.fromarray(bin3)
    text = pytesseract.image_to_string(test_message)
    print(f'识别结果：{text}')


file = 'C:/Users/DC_JL/Desktop/20200810125725937.png'
src = cv.imread(file)
cv.imshow('input img',src)
recognize_text2(src)
cv.waitKey(0)
cv.destroyAllWindows()
