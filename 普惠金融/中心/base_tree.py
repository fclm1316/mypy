#!/usr/bin/python3
#coding:utf-8
import time

from selenium.webdriver import ActionChains

from 普惠金融.中心.test_driver import Web_Driver



class Base_Tree(Web_Driver):

    def base(self):
        #基础功能
        self.driver.find_element_by_xpath('/html/body/section/div/div/div/div[1]/div/img').click()
        link1 = self.driver.find_element_by_xpath('/html/body/header/div[1]/div[1]/img[2]')
        ActionChains(self.driver).click(link1).perform()
        time.sleep(2)
    def show_tree(self):
        #基本功能管理
        self.base()
        link2 = self.driver.find_element_by_xpath('//*[@id="grail-aside"]/div/ul/li[1]/a')
        ActionChains(self.driver).click(link2).perform()
        time.sleep(2)
    def to_wdsb(self):
        #网点申报
        self.show_tree()
        link3 = self.driver.find_element_by_xpath('//*[@id="grail-aside"]/div/ul/li[1]/ul/li[1]/a')
        ActionChains(self.driver).click(link3).perform()
        time.sleep(1)
        self.driver.switch_to_frame(self.driver.find_element_by_xpath('//*[@id="tab_网点申报"]/iframe'))










if __name__ == "__main__":
    pass