#!/usr/bin/python3
#coding:utf-8
import unittest
from selenium import webdriver
from hzzg.cfg import *
from selenium.webdriver.common.action_chains import ActionChains
import HTMLTestReportCN

class Web_Driver(unittest.TestCase):
    #初始化
    def setUp(self):
        #定义驱动
        self.driver = webdriver.Chrome()
        #定义url
        web_url = url
        self.driver.get(web_url)
        #登陆操作
        self.driver.find_element_by_id('orgcode').send_keys(org)
        self.driver.find_element_by_id('username').send_keys(operid)
        self.driver.find_element_by_id('password').clear()
        self.driver.find_element_by_id('password').send_keys(operpwd)
        self.driver.find_element_by_id('submit').click()

    #退出
    def tearDown(self):
        #切回主farme
        self.driver.switch_to.default_content()
        #点击退出
        self.driver.find_element_by_class_name('user-logout').click()
        #切换窗口
        now_window = self.driver.current_window_handle
        self.driver.switch_to.window(now_window)
        #退出确认
        self.driver.find_element_by_class_name('layui-layer-btn0').click()
        self.driver.quit()


# class DoTest(Web_Driver):
#     u''' 登陆测试-点击菜单 '''
#     def test_1(self):
#         u''' 登陆测试1 '''
        # 点击
        # link1 = self.driver.find_element_by_xpath('//*[@id="grail-aside"]/div/div/div[1]')
        # ActionChains(self.driver).move_to_element(link1).perform()
        # link2 = self.driver.find_element_by_xpath('//*[@id="grail-aside"]/div/div/div[1]/div/ul/li/a')
        # ActionChains(self.driver).click(link2).perform()
        # pass

# if __name__ == "__main__":
#     test_unit = unittest.TestSuite()
#     test_unit.addTest(DoTest('test_1'))
#
#     with open('./test_demo.html','wb') as fp:
#         runner = HTMLTestReportCN.HTMLTestRunner(stream=fp,title='自动化测试报告',
#                                                  verbosity=2,
#                                                  description='测试用例-登陆')
#         runner.run(test_unit)
