#!/usr/bin/python3
#coding:utf-8
#弹窗处理  警告窗  提示窗
import time

from selenium import webdriver
from  selenium.webdriver.common.action_chains import ActionChains

dirver = webdriver.Chrome()
dirver.implicitly_wait(10)
dirver.get('http://www.baidu.com')


#移动鼠标
link = dirver.find_element_by_link_text('设置')
#悬停
ActionChains(dirver).move_to_element(link).perform()

# 打开搜索设置
dirver.find_element_by_link_text('搜索设置').click()

#保存
dirver.find_element_by_class_name('prefpanelgo').click()
time.sleep(2)

#接受警告窗口
dirver.switch_to.alert.accept()


