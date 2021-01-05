#encoding:utf-8
# File: 003.py
# Author:fbi
# Time: 20/11/6
import numpy as np
import cv2 as cv
cap = cv.VideoCapture(0,cv.CAP_DSHOW)
# 定义编码
fourcc = cv.VideoWriter_fourcc(*'XVID')
# 文件名 视频编解码器 fps 大小
out = cv.VideoWriter('output.avi',fourcc,20.0,(640,480))

while cap.isOpened():
    ret,frame = cap.read()
    if not ret:
        print("Can't receive frame .exiting...")
        break
#flip 反转:0 x轴翻转，上下。1 y轴翻转,左右。-1 xy同时翻转 180°
    frame = cv.flip(frame,0)
    out.write(frame)
    cv.imshow('frame',frame)

    if cv.waitKey(1) == ord('q'):
        break

cap.release()
out.release()
cv.destroyAllWindows()

