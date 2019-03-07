#!/usr/bin/python3
#coding:utf-8
from  selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium_web.mycfg import *
import time

def login(dirver):
    #登陆操作
    dirver.find_element_by_xpath('//*[@id="qquin"]').send_keys(aaname)
    dirver.find_element_by_xpath('//*[@id="pp"]').send_keys(aapwd)
    dirver.find_element_by_xpath('//*[@id="js_input_area"]/div[6]/a/input').click()
    login_name = dirver.find_element_by_xpath('//*[@id="useralias"]').text
    if login_name == Login_Name:
        print("登陆成功")

def logout(dirver):
    pass

def Send_mail(dirver,to_addr,to_title,to_text):
    login(dirver)
    #进入收件箱
    dirver.find_element_by_xpath('//*[@id="composebtn"]').click()
    # time.sleep(3)
    #frameset frame iframe
    # 可以传入id、name、index[0,1,2]以及selenium的WebElement对象
    # 传入整型即判断为index ,str字符串 判定 id name
    # dirver.switch_to.frame(id)
    # driver.switch_to.frame(reference) 切入frame
    # driver.switch_to.parent_frame()   返回父frame
    # driver.switch_to.default_content() 返回主frame
    #切入frame收件人
    dirver.switch_to.frame("mainFrame")
    #联系人，发送键盘 回车键
    dirver.find_element_by_xpath('//*[@id="toAreaCtrl"]/div[2]/input').send_keys(to_addr,Keys.ENTER)
    #输入主题
    dirver.find_element_by_xpath('//*[@id="subject"]').send_keys(to_title)
    #iframe 的id name 不可定位，使用套嵌查找iframe
    dirver.switch_to.frame(dirver.find_element_by_class_name('QMEditorIfrmEditArea'))
    #键入邮件内容
    dirver.find_element_by_xpath('/html/body').send_keys(to_text)
    #返回父frame
    dirver.switch_to.parent_frame()
    # 发送
    dirver.find_element_by_xpath('//*[@id="toolbar"]/div/input[1]').click()

    dirver.quit()

if __name__ == '__main__':
    browser = webdriver.Chrome()
    browser.get(url)
    Send_mail(browser,addr,title,text)
















# right_chlick = browser.find_element_by_id("xx")
#传入浏览器驱动。右键，传入元素定位。提交
# ActionChains(browser).context_click(right_chlick).perform()
#移动鼠标
# above = browser.find_element_by_xpath('//*[@id="folder_1"]')
# ActionChains(browser).move_to_element(above).perform()
#鼠标双机
# double_chlick = browser.find_element_by_id("xx")
# ActionChains(browser).double_click(double_chlick).perform()
#拖放
# source = browser.find_element_by_id("xx")
# taget =  browser.find_element_by_id("xxx")
# ActionChains(browser).drag_and_drop(source,taget).perform()

# send_keys(Keys.BACK_SPACE)        删除
# send_keys(Keys.SPACE)             空格
# send_keys(Keys.TAB)               制表Tab
# send_keys(Keys.ESCAPE)            退回Esc
# send_keys(Keys.ENTER)             回车
# send_keys(Keys.CONTROL,'a')       Ctrl + a 全选
# send_keys(Keys.F1)                键盘F1

