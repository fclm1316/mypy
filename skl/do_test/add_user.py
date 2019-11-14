#encoding:utf-8
import time
from datetime import date
import random
from skl.dirver.test_driver import *
from selenium.webdriver.common.action_chains import ActionChains
class LogIn(Web_Driver):
    u'''用户注册'''
    def test_001(self):
        self.driver.implicitly_wait(5)
        self.driver.find_element_by_xpath('//div[@id="root"]/section/aside/div/ul/li/div/span/span').click()
        self.driver.implicitly_wait(5)
        self.driver.find_element_by_xpath("//a[contains(@href, '#/user/list')]").click()
        for a in range(200):
            # time_date = date.today().strftime('%Y%m%d')
            # time_date = date.today().strftime('%m%d')
            # time_time = time.strftime('%H%M%S')
            # xzb = ''.join(time_date+time_time+str(a))
            #随机获取数字，chr将十进制的数字按照ASCII表转换成字母，ord()则相反
            abcd_random1 = chr(random.randint(65,90))
            abcd_random2 = chr(random.randint(65,90)).lower()
            time_now = ''.join(abcd_random1+abcd_random2+str(int(time.time())))
            keys = '{0:s}'.format(str(time_now))
            time.sleep(4)
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

