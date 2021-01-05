#encoding:utf-8
from matplotlib import pyplot as plt
import numpy as np
import cv2 as cv

file2 = "C:/Users/DC_JL/Desktop/pyt/2.jpg"

img = cv.imread(file2,0)
plt.imshow(img,cmap='gray',interpolation='bicubic')
# 隐藏x,y轴
plt.xticks([]),plt.yticks([])
plt.show()
