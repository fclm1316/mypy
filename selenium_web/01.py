#!/usr/bin/python3
#coding:utf-8
from selenium import  webdriver

browser = webdriver.Chrome()

browser.get('https://cn.bing.com/')
browser.maximize_window()
# print(browser.page_source)
