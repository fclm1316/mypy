#!/usr/bin/python3
#coding:utf-8
from selenium import webdriver
import unittest
#继承测试类
class NewvisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome()

    def tearDown(self):
        self.browser.quit()


    def test_can_self_a_list_and_retrieve_it_later(self):
        self.browser.get('http://localhost:8000')
        #断言
        self.assertIn('To-Do',self.browser.title)
        self.fail('Finish the test')

if __name__ == "__main__":
    #调用测试类的main，忽略警告
    unittest.main(warnings='ignore')
