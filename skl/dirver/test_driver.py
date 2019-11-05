#encoding:utf-8
import unittest
from selenium import webdriver
from skl.conf.cfg import *

class Web_Driver(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        web_url = url
        # self.driver.maximize_window()
        self.driver.get(web_url)
        self.driver.implicitly_wait(5)
        self.driver.find_element_by_id('username').send_keys(name)
        self.driver.find_element_by_id('password').send_keys(pwd)
        self.driver.find_element_by_xpath('//*[@id="root"]/div/div[1]/div[2]/div/div/form/button').click()

    def tearDown(self):
        self.driver.quit()