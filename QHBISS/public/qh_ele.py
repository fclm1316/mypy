#!/usr/bin/python3
#coding:utf-8
import time
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from public.driver import Web_Driver_qz
from public.configuer import *


class find_html_ele(Web_Driver_qz):
    def enter(self):
        self.driver.implicitly_wait(4)
        self.driver.find_element_by_xpath('/html/body/section/div/div/div/div/div[1]/img').click()

    def jcgngl(self):
        #基础功能管理
        self.driver.implicitly_wait(4)
        self.driver.find_element_by_xpath('//*[@id="grail-aside"]/div/ul/li[1]/a').click()

    def wdgl(self):
        #网点管理
        self.driver.implicitly_wait(4)
        self.driver.find_element_by_xpath('//*[@id="grail-aside"]/div/ul/li[1]/ul/li[1]/a').click()

    def change_iframe(self,name):
        #切换frame
        self.driver.implicitly_wait(4)
        self.driver.switch_to.frame(self.driver.find_element_by_xpath('//*[@id="tab_{0:s}"]/iframe'.format(name)))

    def change_iframe_times(self, times):
        self.driver.implicitly_wait(4)
        self.driver.switch_to.frame(self.driver.find_element_by_xpath('//*[@id="layui-layer-iframe{0:d}"]'.format(times)))

    def change_iframe_father(self):
        self.driver.implicitly_wait(4)
        self.driver.switch_to.parent_frame()


    def data_add(self):
        #新增
        self.driver.implicitly_wait(4)
        self.driver.find_element_by_xpath('//*[@id="baseBranchinfoForm"]/div[2]/div/div[1]/div[1]/div/div/button[1]').click()

    def data_add_branchCode(self, branchCode):
        #新增-机构代码
        self.driver.implicitly_wait(4)
        self.driver.find_element_by_name('branchCode').send_keys(branchCode)

    def data_add_branchName(self, branchName):
        #新增-银行机构名称
        self.driver.implicitly_wait(4)
        self.driver.find_element_by_name('branchName').send_keys(branchName)

    def data_add_finacialCode(self, number):
        #新增-金融机构编码
        self.driver.implicitly_wait(4)
        self.driver.find_element_by_name('finacialCode').send_keys(number)

    def data_add_belonBankCode(self,value):
        #所属参与者
        self.driver.implicitly_wait(4)
        Select(self.driver.find_element_by_id('belonBankCode')).select_by_value(value)

    def data_add_regionCode(self,regionCode):
        #地区编码
        self.driver.implicitly_wait(4)
        Select(self.driver.find_element_by_id('regionCode')).select_by_value(regionCode)

    def data_add_pbcCode(self,pbcCode):
        #归属人行
        self.driver.implicitly_wait(4)
        Select(self.driver.find_element_by_name('pbcCode')).select_by_value(pbcCode)

    def data_add_addr(self,addr):
        #地址
        self.driver.implicitly_wait(4)
        self.driver.find_element_by_name('addr').send_keys(addr)

    def data_add_contact(self,contact):
        #联系人
        self.driver.implicitly_wait(4)
        self.driver.find_element_by_name('contact').send_keys(contact)

    def data_add_contactPhone(self,contactPhone):
        #联系人
        self.driver.implicitly_wait(4)
        self.driver.find_element_by_name('contactPhone').send_keys(contactPhone)

    def data_add_enableDate(self,enableDate):
        #启用时间
        self.driver.implicitly_wait(4)
        self.driver.find_element_by_name('enableDate').send_keys(enableDate)
        self.driver.find_element_by_name('enableDate').click()

    def data_add_sure(self,times):
        self.driver.implicitly_wait(4)
        self.driver.find_element_by_xpath('//*[@id="layui-layer{0:d}"]/div[2]/div/div/div/button[1]'.format(times)).click()
