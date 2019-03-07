#!/usr/bin/python3
#coding:utf-8
#设置等待
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# File "C:\python\lib\site-packages\selenium\webdriver\support\wait.py",
# line 80, in until raise TimeoutException(message, screen, stacktrace)
# 通过报错信息 查看源码  引入 timeout
from selenium.common.exceptions import TimeoutException

browser = webdriver.Chrome()
url = "http://cn.bing.com"
browser.get(url)
try:
# WebDirverWait(dirver,timeout,poll_frequency) 配合 unitl()
#   expected_conditions() 类 提供预判断 , 元素是否被加载
#       title_is    判断当前页面的标题是否与预期相等 <selenium2自动化测试实战基于python> 97页
    element = WebDriverWait(browser,5,0.5).until(EC.presence_of_element_located((By.ID,'sb_from_q')))
#   通过until()方法(返回Ture；not_until()返回False) ， 加匿名函数 查找页面中的 搜索框 是否看的见is_displayed()
    # element = WebDriverWait(browser,5,0.5).until(lambda x: x.find_element_by_id("sb_form_q").is_displayed())
    print(element)
except TimeoutException :
    print("连接 {} 超时".format(url))
    browser.quit()


