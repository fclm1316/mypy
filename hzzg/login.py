#!/usr/bin/python3
# coding:utf-8
import time
from hzzg.cfg import *
from selenium import webdriver


class LogIn:
    def __init__(self, driver):
        self.driver = driver

    def login_1(self):
        '''
        登陆
        :return:
        '''
        self.driver.find_element_by_id('orgcode').send_keys(org)
        self.driver.find_element_by_id('username').send_keys(operid)
        self.driver.find_element_by_id('password').clear()
        self.driver.find_element_by_id('password').send_keys(operpwd)
        self.driver.find_element_by_id('submit').click()

    def chang_window(self):
        now_window = self.driver.current_window_handle
        self.driver.switch_to.window(now_window)

    def logout(self):
        self.driver.find_element_by_class_name('user-logout').click()
        time.sleep(1)
        self.chang_window()
        print("====")
        self.driver.find_element_by_class_name('layui-layer-btn0').click()
        self.driver.quit()


if __name__ == '__main__':
    driver = webdriver.Chrome()
    driver.get(url)
    aa = LogIn(driver)
    aa.login_1()
    time.sleep(1)
    print("-----")
    aa.logout()
