#!/usr/bin/python3
#coding:utf-8
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
import time
from 普惠金融.前置.driver_qz import Web_Driver
from 普惠金融.config import *


class find_html_ele(Web_Driver):
    def show_tree(self):
        self.driver.find_element_by_xpath('/html/body/section/div/div/div/div[2]/div/img').click()
        self.driver.implicitly_wait(4)
        link1 = self.driver.find_element_by_xpath('/html/body/header/div[1]/div[1]/img[2]')
        ActionChains(self.driver).click(link1).perform()
        time.sleep(2)

    def dwzh_hzz(self):
        #单位账户-备案制
        self.driver.implicitly_wait(4)
        self.driver.find_element_by_xpath('//*[@id="grail-aside"]/div/ul/li[1]/a').click()
        self.driver.implicitly_wait(4)
        self.driver.find_element_by_xpath('//*[@id="grail-aside"]/div/ul/li[1]/ul/li[2]/a').click()

    def change_iframe(self,name):
        self.name = name
        # self.driver.switch_to_frame(self.driver.find_element_by_xpath('//*[@id="tab_准制业务申报"]/iframe'))
        self.driver.switch_to_frame(self.driver.find_element_by_xpath('//*[@id="tab_{0:s}"]/iframe'.format(name)))
        time.sleep(1)

    def data_add(self):
        self.driver.find_element_by_id('data-add').click()

    def first_businesstype(self,number):
        #核准制业务类型
        self.number = number
        Select(self.driver.find_element_by_id('first-businesstype')).select_by_value(self.number)

    def first_accountattr(self,number):
        #账户性质
        self.number = number
        Select(self.driver.find_element_by_id('first-accountattr')).select_by_value(self.number)

    def sure_yes(self):
        self.driver.find_element_by_link_text('确定').click()

    def accountno(self,number):
        #账户
        self.number = number
        self.driver.find_element_by_css_selector('#form-busi_10 > div.busidiv.accountno > input').send_keys(number)

    def accountname(self,name):
        #账户名称
        self.name = name
        self.driver.find_element_by_css_selector('#form-busi_10 > div.busidiv.accountname > input').send_keys(name)

    def unitname(self,name):
        # #存款人名称
        self.name = name
        self.driver.find_element_by_css_selector('#form-busi_10 > div.busidiv.unitname > input').send_keys(name)

    def legalrepresenttative(self,name):
        # #法定代表人或单位负责人姓名
        self.name = name
        self.driver.find_element_by_css_selector('#form-busi_10 > div.busidiv.legalrepresenttative > input').send_keys(name)

    def lrcertno(self,number):
        # #法定代表人或单位负责人证件号码
        self.number = number
        self.driver.find_element_by_css_selector('#form-busi_10 > div.busidiv.lrcertno > input').send_keys(number)

    def addr(self,name):
        #地址
        self.name = name
        self.driver.find_element_by_css_selector('#form-busi_10 > div.busidiv.addr > input').send_keys(name)

    def ownerphone(self,number):
        # #法定代表人或单位负责人电话
        self.number = number
        self.driver.find_element_by_css_selector('#form-busi_10 > div.busidiv.ownerphone > input').send_keys(number)

    def zipcode(self,number):
        # #邮政编码：
        self.number = number
        self.driver.find_element_by_css_selector('#form-busi_10 > div.busidiv.zipcode > input').send_keys(number)

    def certifyfilekind1(self,name):
        # #证明文件1种类：
        self.name = name
        self.driver.find_element_by_css_selector('#form-busi_10 > div.busidiv.certifyfilekind1 > input').send_keys(name)

    def certifyfileno1(self,name):
        # #证明文件1编号：
        self.name = name
        self.driver.find_element_by_css_selector('#form-busi_10 > div.busidiv.certifyfileno1 > input').send_keys(name)

    def industrycategory(self,value):
        #行业类别
        #A-U
        self.value = value
        Select(self.driver.find_element_by_css_selector('#form-busi_10 > div.busidiv.industrycategory > div > select')).select_by_value(value)

    def depositorattr(self,value):
        #存款人类别
        #01-18
        self.value = value
        Select(self.driver.find_element_by_name('depositorattr')).select_by_value(value)

    def upregioncode(self,value):
        # 地区代码地市
        self.value = value
        Select(self.driver.find_element_by_id('upregioncode')).select_by_value(value)

    def regioncode(self,value):
        # 地区代码县市
        self.value = value
        Select(self.driver.find_element_by_id('regioncode')).select_by_value(value)

    def click_sc(self):
        # 上传
        self.driver.find_element_by_class_name('layui-layer-btn2').click()
        # time.sleep(2)

    def input_file(self):
        #放入文件
        self.driver.find_element_by_xpath('//*[@id="get"]/td[1]/form/div[2]/input[1]').send_keys(file1)
        self.driver.find_element_by_xpath('//*[@id="get"]/td[1]/form/div[2]/input[2]').send_keys(Keys.ENTER)
        # get > td:nth-child(1) > form > div:nth-child(8) > input.form-control

    def sure_upload(self):
        # 确认上传
        self.driver.find_element_by_xpath('//*[@id="layui-layer3"]/div[3]/a').click()
        # self.driver.implicitly_wait(2)

    def sure_comm(self):
        # 提交
        self.driver.find_element_by_xpath('//*[@id="submit-pic"]').click()

    def sure_final_upload(self):
        # #上传后最后确定
        self.driver.find_element_by_css_selector('#layui-layer5 > div.layui-layer-btn.layui-layer-btn- > a').click()

    def switch_default_iframe(self):
        #切回主frame
        self.driver.switch_to.default_content()
        time.sleep(1)

    def acctpermitno(self,number):
        #基本存款账户开户许可证号
        self.number = number
        self.driver.find_element_by_css_selector('#form-busi_10 > div.busidiv.acctpermitno > input').send_keys(number)

    def pbclicencennum(self,number):
        #备案制编号
        self.number = number
        self.driver.find_element_by_css_selector('#form-busi_10 > div.busidiv.pbclicencennum > input').send_keys(number)

    def accountvalidity(self,date):
        self.number = date
        self.driver.find_element_by_css_selector('#form-busi_10 > div.busidiv.accountvalidity > input').send_keys(date,Keys.ENTER)

