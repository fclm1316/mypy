#!/usr/bin/python3
#coding:utf-8
import time
from 普惠金融.前置.html_ele import find_html_ele
from selenium.webdriver.common.keys import Keys
from 普惠金融.前置.driver_qz import Web_Driver
from 普惠金融.config import *
from selenium.webdriver import ActionChains
from selenium.webdriver.support.select import Select

class wanggongzi(find_html_ele):
    # def kaihu(self):
    #     time.sleep(2)
    #     self.driver.find_element_by_xpath('/html/body/section/div/div/div/div[2]/div/img').click()
    #     link1 = self.driver.find_element_by_xpath('/html/body/header/div[1]/div[1]/img[2]')
    #     ActionChains(self.driver).click(link1).perform()
    # #单位账户业务
    #     self.driver.implicitly_wait(4)
    #     time.sleep(3)
    #     self.driver.find_element_by_xpath('//*[@id="grail-aside"]/div/ul/li[1]/a').click()
    #     self.driver.implicitly_wait(4)
    #     self.driver.find_element_by_xpath('//*[@id="grail-aside"]/div/ul/li[1]/ul/li[2]/a').click()
    #     self.driver.implicitly_wait(2)
    #         #切换frame
    #     self.driver.switch_to_frame(self.driver.find_element_by_xpath('//*[@id="tab_核准制业务申报"]/iframe'))
    #     self.driver.find_element_by_id('data-add').click()

    def test_11_2(self):
        # self.kaihu()
        # time.sleep(2)
        super().show_tree()
        super().dwzh_hzz()
        super().change_iframe('核准制业务申报')
        super().data_add()
        super().first_businesstype('11')
        super().first_accountattr('2')
        # time.sleep(2)
        super().sure_yes()

        #账号
        super().accountno('11111')
        super().accountname('haha')
        time.sleep(10)
        # # self.driver.find_element_by_xpath('//*[@id="form-busi_10"]/div[9]/input').send_keys('110000000')
        # #账号名称
        # self.driver.find_element_by_xpath('//*[@id="form-busi_10"]/div[10]/input').send_keys('aaaaa')
        # #存款人名称
        # self.driver.find_element_by_xpath('//*[@id="form-busi_10"]/div[13]/input').send_keys('abcd')
        # #法定代表人或单位负责人姓名
        # self.driver.find_element_by_xpath('//*[@id="form-busi_10"]/div[15]/input').send_keys('abcd')
        # #法定代表人或单位负责人证件号码
        # self.driver.find_element_by_xpath('//*[@id="form-busi_10"]/div[17]/input').send_keys('aaaa')
        # #单位地址
        # self.driver.find_element_by_xpath('//*[@id="form-busi_10"]/div[23]/input').send_keys('dddddd')
        # #法定代表人或单位负责人电话
        # self.driver.find_element_by_xpath('//*[@id="form-busi_10"]/div[18]/input').send_keys('123')
        # #邮政编码：
        # self.driver.find_element_by_xpath('//*[@id="form-busi_10"]/div[25]/input').send_keys('310000')
        # #证明文件1种类：
        # self.driver.find_element_by_xpath('//*[@id="form-busi_10"]/div[26]/input').send_keys('1111')
        # #证明文件1编号：
        # self.driver.find_element_by_xpath('//*[@id="form-busi_10"]/div[27]/input').send_keys('11111')
        # Select(self.driver.find_element_by_name('depositorattr')).select_by_value('03')
        # Select(self.driver.find_element_by_id('upregioncode')).select_by_value('450100')
        # Select(self.driver.find_element_by_id('regioncode')).select_by_value('450101')
        # Select(self.driver.find_element_by_xpath('//*[@id="form-busi_10"]/div[14]/div/select')).select_by_value('C')
        # # time.sleep(2)
        # #上传
        # self.driver.find_element_by_class_name('layui-layer-btn2').click()
        # # time.sleep(2)
        # self.driver.find_element_by_xpath('//*[@id="get"]/td[1]/form/div[2]/input[1]').send_keys(file1)
        # self.driver.find_element_by_xpath('//*[@id="get"]/td[1]/form/div[2]/input[2]').send_keys(Keys.ENTER)
        # #
        # #确认
        # self.driver.find_element_by_xpath('//*[@id="layui-layer3"]/div[3]/a').click()
        # self.driver.implicitly_wait(2)
        # #提交
        # time.sleep(2)
        # self.driver.find_element_by_xpath('//*[@id="submit-pic"]').click()
        #
        # self.driver.implicitly_wait(2)
        # #上传后最后确定
        # self.driver.find_element_by_css_selector('#layui-layer5 > div.layui-layer-btn.layui-layer-btn- > a').click()
        #
        # self.driver.switch_to.default_content()

    # def test_11_3(self):
    #     self.kaihu()
    #     Select(self.driver.find_element_by_id('first-businesstype')).select_by_value('11')
    #     Select(self.driver.find_element_by_id('first-accountattr')).select_by_value('3')
    #     self.driver.find_element_by_link_text('确定').click()








if __name__ == "__main__":
    pass