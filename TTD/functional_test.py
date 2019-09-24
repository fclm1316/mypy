#!/usr/bin/python3
#coding:utf-8
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
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
        # self.fail('Finish the test')
        #判断网页的标题和头部都包含“To-Do”
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do',header_text)
        #查找元素id_new_item
        inputbox = self.browser.find_element_by_id('id_new_item')
        #元素的属性placeholder 是否等于 Enter a to-do item
        self.assertEqual(inputbox.get_attribute('placeholder'),'Enter a to-do item')
        #输入框键入内容
        inputbox.send_keys('Buy peacock feathers')
        #输入回车
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)

        #查找中的查找
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        #是否含有
        self.assertTrue(any(row.text == '1: Buy peacock feathers' for row in rows),
                        "New to-do item did not apper in table")
        self.fail('Finsh the test')


if __name__ == "__main__":
    #调用测试类的main，忽略警告
    unittest.main(warnings='ignore')
