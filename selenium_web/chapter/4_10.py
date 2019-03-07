#!/usr/bin/python3
#coding:utf-8
#多窗口切换


from selenium import webdriver

dirver = webdriver.Chrome()
#等待相应
dirver.implicitly_wait(10)
dirver.get("http://www.baidu.com")

#获得搜索窗口的句柄
sreach_windows = dirver.current_window_handle

dirver.find_element_by_link_text('登录').click()
dirver.find_element_by_link_text("立即注册").click()
#获得所有句柄
all_handles = dirver.window_handles

#判断句柄,如果多个句柄，定义多个变量获得句柄
for handle in all_handles:
    if handle == sreach_windows:
        dirver.switch_to.window(handle)
        dirver.find_element_by_id('kw').send_keys("selenium")


for handle in all_handles:
    if handle != sreach_windows:
       dirver.find_element_by_name('account').send_keys('username')


