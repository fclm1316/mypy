#!/usr/bin/python3
#coding:utf-8
from selenium import webdriver
import time

browser = webdriver.Chrome()
url = "http://cn.bing.com"
browser.get(url)
    # el = browser.find_element_by_id("sb_from_q")
for i in range(10):
    try:
        el = browser.find_element_by_class_name("b_searchbox")
        if el.is_displayed():
            print("haha")
            break
    except:
        pass
        print('第 {} 次'.format(i) )
        time.sleep(1)
else:
    print("error or time out")

#隐式等待
# browser.implicitly_wait(5)
# browser.get(url)

