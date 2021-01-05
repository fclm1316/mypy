#encoding:utf-8
from skimage.measure import compare_ssim
from skimage.metrics import structural_similarity
import imutils
import cv2

file2 = "C:/Users/DC_JL/Desktop/pyt/2.jpg"
file3 = "C:/Users/DC_JL/Desktop/pyt/3.jpg"
file4 = "C:/Users/DC_JL/Desktop/pyt/4.jpg"

imageA = cv2.imread(file2)
imageB = cv2.imread(file3)
#加载两张图片并转换为灰度
grayA = cv2.cvtColor(imageA,cv2.COLOR_BGR2GRAY)
grayB = cv2.cvtColor(imageB,cv2.COLOR_BGR2GRAY)

#(score,diff) = compare_ssim(grayA,grayB,full=True)
#查找不同，相同
(score,diff) = structural_similarity(grayA,grayB,full=True)
diff = (diff * 255).astype("uint8")
# print("SSIM: {}".format(score))


thresh = cv2.threshold(diff,0,255,cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]
#查找轮廓
cnts = cv2.findContours(thresh.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
# cnts = cnts[0] if imutils.is_cv2() else cnts[1]
# print(cnts[0])
# print(cnts[1])
for c in cnts[0]:
    #print(cv2.boundingRect(c))
    x,y,w,h = cv2.boundingRect(c)
    #对角线,左上,右下，rgb颜色,线宽度
    cv2.rectangle(imageA,(x,y),(x+w,y+h),(0,0,255),2)
    # cv2.rectangle(imageB,(x,y),(x+w,y+h),(0,0,255),2)

# cv2.imshow("Modified",imageA)
cv2.imwrite(file4,imageA)
# cv2.waitKey(0)
