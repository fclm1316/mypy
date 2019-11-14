#encoding:utf-8
import time
import unittest
from skl.dirver.test_driver import *
from selenium.webdriver.common.action_chains import ActionChains
@unittest.skip('跳过')
class LogIn(Web_Driver):
    u'''角色注册'''
    def test_002(self):
        self.driver.implicitly_wait(5)
        self.driver.find_element_by_xpath('//div[@id="root"]/section/aside/div/ul/li/div/span/span').click()
        self.driver.implicitly_wait(5)
        self.driver.find_element_by_xpath("//a[contains(@href, '#/role/list')]").click()
        for a in range(300,400):
            keys = '{0:s}{1:d}'.format('xzb',a)
            time.sleep(3)
            self.driver.find_element_by_xpath('//*[@id="root"]/section/section/main/div[1]/div[2]/div[2]/div[1]/span[1]/button[1]').click()
            self.driver.implicitly_wait(5)
            self.driver.find_element_by_xpath('//form/div/div[2]/div/span/input').send_keys(keys)
            self.driver.find_element_by_xpath("//div[@class='ant-modal-footer']/div/button[2]").click()

