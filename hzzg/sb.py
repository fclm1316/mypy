#!/usr/bin/python3
# coding:utf-8
from selenium.webdriver.common.keys import Keys

from hzzg.login import *
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select


class ShengBao:
    def __init__(self, driver):
        self.driver = driver

    def shengbao(self):
        '''
        申报头
        '''
        aa = LogIn(self.driver)
        aa.login_1()
        # 鼠标事件，进入申报菜单
        link1 = self.driver.find_element_by_xpath('//*[@id="grail-aside"]/div/div/div[1]')
        ActionChains(self.driver).move_to_element(link1).perform()
        link2 = self.driver.find_element_by_xpath('//*[@id="grail-aside"]/div/div/div[1]/div/ul/li/a')
        ActionChains(self.driver).click(link2).perform()
        # 切换frame
        # self.driver.switch_to.frame(driver.find_element_by_xpath('//*[@frameborder="0"]'))

    def value12(self):
        #
        self.shengbao()
        # 鼠标事件，进入申报菜单
        for text in ckrlb:
            link1 = self.driver.find_element_by_xpath('//*[@id="grail-aside"]/div/div/div[1]')
            ActionChains(self.driver).move_to_element(link1).perform()
            link2 = self.driver.find_element_by_xpath('//*[@id="grail-aside"]/div/div/div[1]/div/ul/li/a')
            ActionChains(self.driver).click(link2).perform()
            # 增加操作
            self.driver.switch_to.frame(0)
            # time.sleep(1)
            self.driver.implicitly_wait(1)
            self.driver.find_element_by_id('data-add').click()

            # 选择待核准类型 12
            Select(self.driver.find_element_by_name('first-businesstype')).select_by_value('12')
            self.driver.find_element_by_link_text('确定').click()
            # 没有id 好难定位啊,真丑
            # 存款人类别
            Select(
                self.driver.find_element_by_xpath('//*[@id="form-busi_12"]/div[3]/div[2]/div/select')).select_by_value(
                text)
            # for zz in zjzl:
            # 证件种类
            Select(
                self.driver.find_element_by_xpath('//*[@id="form-busi_12"]/div[5]/div[2]/div/select')).select_by_value(
                '02004')
            # 行业类别
            Select(
                self.driver.find_element_by_xpath('//*[@id="form-busi_12"]/div[6]/div[2]/div/select')).select_by_value(
                'H')
            # 负责人种类
            Select(
                self.driver.find_element_by_xpath('//*[@id="form-busi_12"]/div[7]/div[2]/div/select')).select_by_value(
                '01003')
            # 地区代码
            Select(
                self.driver.find_element_by_xpath('//*[@id="form-busi_12"]/div[9]/div[1]/div/select')).select_by_value(
                '330000')
            # 账户
            self.driver.find_element_by_xpath('//*[@id="form-busi_12"]/div[4]/div[1]/input').send_keys(input_id)
            # 账户名称
            self.driver.find_element_by_xpath('//*[@id="form-busi_12"]/div[4]/div[2]/input').send_keys(input_str)
            # 存款人名称
            self.driver.find_element_by_xpath('//*[@id="form-busi_12"]/div[5]/div[1]/input').send_keys(input_str)
            # 证件号码
            self.driver.find_element_by_xpath('//*[@id="form-busi_12"]/div[6]/div[1]/input').send_keys(input_id)
            # 单位负责人姓名
            self.driver.find_element_by_xpath('//*[@id="form-busi_12"]/div[7]/div[1]/input').send_keys(input_str)
            # 负责人证件号码
            self.driver.find_element_by_xpath('//*[@id="form-busi_12"]/div[8]/div[1]/input').send_keys(input_id)
            # 负责人电话
            self.driver.find_element_by_xpath('//*[@id="form-busi_12"]/div[8]/div[2]/input').send_keys(input_id)
            # 地址
            self.driver.find_element_by_xpath('//*[@id="form-busi_12"]/div[13]/div[1]/input').send_keys(input_str)

            # 保存
            # self.driver.find_element_by_class_name('layui-layer-btn0').click()
            self.driver.implicitly_wait(1)
            # 上传影像
            self.driver.find_element_by_class_name('layui-layer-btn2').click()
            self.driver.implicitly_wait(1)
            # self.driver.switch_to.frame(self.driver.find_element_by_xpath('//*[@id="grail-content"]/iframe'))
            # 增加文件项目
            # self.driver.find_element_by_xpath('//*[@id="add-pic"]').click()
            # self.driver.find_element_by_xpath('//*[@id="add-pic"]').click()
            # 上传文件1
            self.driver.find_element_by_xpath('//*[@id="get"]/td[1]/form/div[2]/input[1]').send_keys(file1)
            # 发送回车，诡异,不能点击
            self.driver.find_element_by_xpath('//*[@id="get"]/td[1]/form/div[2]/input[2]').send_keys(Keys.ENTER)
            self.driver.implicitly_wait(1)
            # ActionChains(self.driver).click(link3).perform()
            self.driver.find_element_by_xpath('//*[@id="layui-layer3"]/div[3]/a').click()
            # 上传文件2
            # 上传文件2
            self.driver.implicitly_wait(1)

            # 提交
            self.driver.find_element_by_xpath('//*[@id="submit-pic"]').click()
            # 提交确认
            self.driver.find_element_by_xpath('//*[@id="layui-layer4"]/div[3]/a[1]').click()

            # self.driver.switch_to.parent_frame()
            # 返回主frame
            self.driver.switch_to.default_content()

        # self.driver.switch_to.frame(0)
        # self.driver.switch_to.parent_frame()
        # self.driver.find_element_by_id('data-add').click()


if __name__ == '__main__':
    driver = webdriver.Chrome()
    driver.get(url)
    driver.maximize_window()
    aa = ShengBao(driver)
    aa.value12()
    driver.quit()
