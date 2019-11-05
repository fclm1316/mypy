#encoding:utf-8
import time
from skl.dirver.test_driver import *
from selenium.webdriver.common.action_chains import ActionChains
class LogIn(Web_Driver):
    u'''用户注册'''
    def test_001(self):
        self.driver.implicitly_wait(5)
        self.driver.find_element_by_xpath('//div[@id="root"]/section/aside/div/ul/li/div/span/span').click()
        self.driver.implicitly_wait(5)
        self.driver.find_element_by_xpath("//a[contains(@href, '#/user/list')]").click()
        for a in range(100,200):
            keys = '{0:s}{1:d}'.format('xzb',a)
            time.sleep(3)
            self.driver.find_element_by_xpath('//*[@id="root"]/section/section/main/div[1]/div/div[2]/section/section/main/div[2]/div[1]/button[1]').click()
            # time.sleep(5)
            # self.driver.find_element_by_xpath('//*[@id="root"]/section/section/main/div[1]/div/div[2]/section/section/main/div[2]/div[1]/button[1]').click()
            self.driver.find_element_by_xpath('//div/div/div/div[2]/div/span/input').send_keys(keys)
            self.driver.find_element_by_xpath('//div[2]/div/div[2]/div/span/input').send_keys('test')
            self.driver.implicitly_wait(5)
            self.driver.find_element_by_xpath('//div[4]/div/div[2]/div/span/input').send_keys('12345678')
            self.driver.find_element_by_xpath('//div[5]/div/div[2]/div/span/input').send_keys('12345678910')
            self.driver.find_element_by_xpath('//div[7]/div/div[2]/div/span/input').send_keys('123@123.com')
            self.driver.implicitly_wait(5)
            self.driver.find_element_by_xpath("//div[3]/div/div[2]/div/span/span/span/span").click()
            time.sleep(2)
            self.driver.find_element_by_xpath("//div[@id='rc-tree-select-list_2']/ul/li/span[2]/span").click()
            self.driver.implicitly_wait(5)
            self.driver.find_element_by_xpath("//div[@class='ant-modal-footer']/button[2]").click()
            # time.sleep(40)

