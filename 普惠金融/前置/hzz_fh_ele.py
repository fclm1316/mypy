#!/usr/bin/python3
#coding:utf-8
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
import time
from 普惠金融.前置.driver_qz import Web_Driver2
from 普惠金融.config import *

class find_html_ele(Web_Driver2):
    def show_tree(self):
        self.driver.find_element_by_xpath('/html/body/section/div/div/div/div[2]/div/img').click()
        self.driver.implicitly_wait(4)
        time.sleep(2)
        link1 = self.driver.find_element_by_xpath('/html/body/header/div[1]/div[1]/img[2]')
        ActionChains(self.driver).click(link1).perform()

    def dwzh_hzz(self):
        #单位账户-备案制
        self.driver.implicitly_wait(4)
        # self.driver.find_element_by_xpath('//*[@id="grail-aside"]/div/ul/li[1]/a').click()
        self.driver.find_element_by_css_selector('#grail-aside > div > ul > li:nth-child(1) > a').click()
        self.driver.implicitly_wait(4)
        time.sleep(2)
        # self.driver.find_element_by_xpath('//*[@id="grail-aside"]/div/ul/li[1]/ul/li[2]/a').click()
        self.driver.find_element_by_css_selector('#grail-aside > div > ul > li:nth-child(1) > ul > li:nth-child(2) > a').click()

    def switch_default_iframe(self):
        #切回主frame
        self.driver.switch_to.default_content()
        time.sleep(1)

    def refresh(self):
        self.driver.refresh()

    def windows(self):
        return  self.driver.current_window_handle

    def all_windows(self):
        return self.driver.window_handles

    def change_windows(self,value):
        self.value = value
        self.driver.switch_to_window(value)



    def change_iframe(self,name):
        self.name = name
        # self.driver.switch_to_frame(self.driver.find_element_by_xpath('//*[@id="tab_准制业务申报"]/iframe'))
        self.driver.switch_to_frame(self.driver.find_element_by_xpath('//*[@id="tab_{0:s}"]/iframe'.format(name)))
        time.sleep(1)

    def fuhe(self):
        #复核按钮
        self.driver.find_element_by_css_selector('#aiarBusinessdealinfoTable > tbody > tr:nth-child(1) > td:nth-child(2) > a.data-check').click()

    def fuhe_tg(self):
        #复核通过
        self.driver.find_element_by_css_selector('body > section > div > b > b > div:nth-child(2) > button:nth-child(11)').click()

    def fuhe_sure(self):
        #复核通过按钮
        js = 'document.getElementsByClassName("layui-layer-btn0")[0].click()'
        self.driver.execute_script(js)

    def tuihui(self,text):
        #退回理由
        self.text = text
        self.driver.find_element_by_id('message').send_keys(text)

    def tuihui_tg(self):
        self.driver.find_element_by_css_selector('body > section > div > b > b > div:nth-child(2) > button:nth-child(12)').click()

    def close_frame(self,name):
        self.name = name
        self.driver.find_element_by_css_selector('#tab_tab_{0:s} > i'.format(name)).click()




if __name__ == "__main__":
    pass