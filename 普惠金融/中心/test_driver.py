#!/usr/bin/python3
#coding:utf-8

import unittest
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from 普惠金融.config import *

class Web_Driver(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        web_url = url_zx
        self.driver.get(web_url)
        self.driver.find_element_by_id('username').send_keys(username)
        self.driver.find_element_by_id('password').send_keys(passwd)
        self.driver.find_element_by_id('submit').click()

    def tearDown(self):
        # self.driver.find_element_by_xpath('/html/body/header/div[2]/div/div/a/i').click()
        self.driver.quit()


