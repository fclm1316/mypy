#!/usr/bin/python3
#coding:utf-8
#多选框，定位一组元素
from selenium import webdriver
import os,time

dirver = webdriver.Chrome()
file_path = 'file:///' + os.path.abspath('checkbox.html')
dirver.get(file_path)
#选择页面上所有的 tag name 为 input 的元素
inputs = dirver.find_elements_by_tag_name('input')

for i in inputs:
    if i.get_attribute('type') == 'checkbox':
        i.click()
        time.sleep(1)

#通过Xpath 找到 type=checkbox元素
checkboxes = dirver.find_elements_by_xpath('//input[@type="checkbox"]')
#通过CSS找到 type=checkbox 元素
checkboxes2 = dirver.find_elements_by_css_selector('input[type=checkbox]')
for checkbox in  checkboxes:
    checkbox.click()
    time.sleep(1)

#获得个数
print(len(checkboxes))
#pop()弹出第一个 pop(2) pop(4) pop(-1)
checkboxes3 = dirver.find_elements_by_css_selector('input[type=checkbox]').pop().click()




dirver.quit()


