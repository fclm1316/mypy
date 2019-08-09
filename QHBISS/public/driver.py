#!/usr/bin/python3
#coding:utf-8
import time
import unittest
from selenium import webdriver
from public.configuer import *

class Web_Driver_qz(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

        web_url = url_qz
        self.driver.maximize_window()
        self.driver.get(web_url)
        self.driver.find_element_by_id('username').send_keys(username)
        self.driver.find_element_by_id('password').send_keys(passwd)

        # self.driver.find_element_by_id('org_name').send_keys(org)
        self.driver.find_element_by_id('submit').click()

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    pass