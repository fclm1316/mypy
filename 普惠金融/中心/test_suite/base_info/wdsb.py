#!/usr/bin/python3
#coding:utf-8
from 普惠金融.中心.test_driver import Web_Driver
from 普惠金融.中心.base_tree import Base_Tree
from 普惠金融.config import *
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
import time

class wdsb(Base_Tree):

    def test_0002(self):
        u'''网点申报_查询'''
        #网点申报
        super().to_wdsb()
        #根据网点编号查询
        self.driver.find_element_by_xpath('//*[@id="baseBranchreqinfoForm"]/div[1]/div/div[1]/div/input').send_keys('012345678912')
        #查询按钮
        self.driver.find_element_by_id('data-query').click()
        time.sleep(2)
        self.driver.find_element_by_id("data-reset").click()
        #根据网点名称查询
        self.driver.find_element_by_xpath('//*[@id="baseBranchreqinfoForm"]/div[1]/div/div[2]/div/input').send_keys('2222')
        self.driver.find_element_by_id('data-query').click()
        time.sleep(2)
        #根据日期
        self.driver.find_element_by_id("data-reset").click()
        self.driver.find_element_by_id('startdate').send_keys('2019-04-19',Keys.ENTER)
        self.driver.find_element_by_id('data-query').click()
        time.sleep(2)
    def test_0003(self):
        u'''新增'''
        super().to_wdsb()
        self.driver.find_element_by_id('data-add').click()
        self.driver.find_element_by_id('branchcode').send_keys(branchcode)
        self.driver.find_element_by_id('branchname').send_keys(branchname)
        self.driver.find_element_by_id('finacialcode').send_keys(finacialcode)
        self.driver.find_element_by_id('addr').send_keys(addr)
        self.driver.find_element_by_id('contact').send_keys(contact)
        self.driver.find_element_by_id('contactphone').send_keys(contactphone)
        self.driver.find_element_by_id('enabledate').send_keys(enabledate,Keys.ENTER)
        self.driver.find_element_by_id('disabledate').send_keys(disabledate,Keys.ENTER)
        self.driver.find_element_by_id('descript').send_keys(descript)
        # Select(self.driver.find_element_by_id('pbccode')).select_by_value()







if __name__ == "__main__":
    pass