#encoding:utf-8
import numpy as np
import cv2 as cv

#0 1 来表示哪个摄像头
cap = cv.VideoCapture(0,cv.CAP_DSHOW)
# cap = cv.VideoCapture('a.avi')
#判断摄像头是否初始化
if not cap.isOpened():
    print("Cannot open camera")
    exit()
#设置窗口大小
print(cap.get(cv.CAP_PROP_FRAME_HEIGHT))
print(cap.get(cv.CAP_PROP_FRAME_WIDTH))
cap.set(cv.CAP_PROP_FRAME_WIDTH, 320)
cap.set(cv.CAP_PROP_FRAME_HEIGHT, 240)
print(cap.get(cv.CAP_PROP_FRAME_HEIGHT))
print(cap.get(cv.CAP_PROP_FRAME_WIDTH))

while True:
    #逐帧捕获
    ret,farme = cap.read()
    #判断是否捕获到
    if not ret:
        print("Can't receive frame .exiting...")
        break
    gray = cv.cvtColor(farme, cv.COLOR_BGR2GRAY)
    cv.imshow('farme', gray)
    if cv.waitKey(1) == ord('q'):
        break
#释放摄像头
cap.release()
#关闭窗口
cv.destroyAllWindows()
