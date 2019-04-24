#!/usr/bin/python3
#coding:utf-8

import unittest
from selenium import webdriver
from 普惠金融.config import *

class Web_Driver1(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

        web_url = url_qz
        self.driver.maximize_window()
        self.driver.get(web_url)
        self.driver.find_element_by_id('username').send_keys(id1)
        self.driver.find_element_by_id('password').send_keys(pwd)
        self.driver.find_element_by_id('org_name').send_keys(org)
        self.driver.find_element_by_id('submit').click()

    def tearDown(self):
        self.driver.quit()


class Web_Driver2(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

        web_url = url_qz
        self.driver.maximize_window()
        self.driver.get(web_url)
        self.driver.find_element_by_id('username').send_keys(id2)
        self.driver.find_element_by_id('password').send_keys(pwd)
        self.driver.find_element_by_id('org_name').send_keys(org)
        self.driver.find_element_by_id('submit').click()

    def tearDown(self):
        self.driver.quit()
