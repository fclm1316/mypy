#!/usr/bin/python3
#coding:utf-8
import time
from 普惠金融.前置.html_ele import find_html_ele
from 普惠金融.config import *
import unittest

class hzz_data_add(find_html_ele):
    u'''账户核准制增加'''
    @unittest.skip('跳过')
    def test_11_2(self):
        u'''11_2 类型测试'''
        time.sleep(2)
        super().show_tree()
        super().dwzh_hzz()
        super().change_iframe('核准制业务申报')
        super().data_add()
        super().first_businesstype('11')
        super().first_accountattr('2')
        super().sure_yes()
        #录入信息
        super().accountno('11111')
        super().accountname('haha')
        super().unitname('aaaa')
        super().legalrepresenttative('12344')
        super().lrcertno('jjjjj')
        super().addr('123jjjj')
        super().ownerphone('111122')
        super().zipcode('12134')
        super().certifyfilekind1('asdv')
        super().certifyfileno1('advv')
        super().industrycategory('B')
        super().depositorattr('02')
        super().upregioncode('450100')
        super().regioncode('450101')
        # 上传
        super().click_sc()
        super().input_file()
        super().sure_upload()
        super().sure_comm()
        super().sure_final_upload()
        #返回主iframe
        super().switch_default_iframe()
        time.sleep(2)

    @unittest.skip('跳过')
    def test_11_3(self):
        u'''11_3测试'''
        #菜单
        super().show_tree()
        super().dwzh_hzz()
        super().change_iframe('核准制业务申报')
        super().data_add()
        super().first_businesstype('11')
        super().first_accountattr('3')
        super().sure_yes()
        #录入
        super().accountno('233333')
        super().accountname('aaaaa')
        super().upregioncode('450100')
        super().regioncode('450101')
        super().certifyfilekind1('aaaaa')
        super().certifyfileno1('dddd')
        super().acctpermitno('12345')
        #上传
        super().click_sc()
        super().input_file()
        super().sure_upload()
        super().sure_comm()
        super().sure_final_upload()
        #返回主iframe
        super().switch_default_iframe()
        time.sleep(2)

    @unittest.skip('跳过')
    def test_11_4(self):
        u'''11_4测试'''
        #菜单
        super().show_tree()
        super().dwzh_hzz()
        super().change_iframe('核准制业务申报')
        super().data_add()
        super().first_businesstype('11')
        super().first_accountattr('4')
        super().sure_yes()
        #录入
        super().accountno('233333')
        super().accountname('aaaaa')
        super().upregioncode('450100')
        super().regioncode('450101')
        super().certifyfilekind1('aaaaa')
        super().certifyfileno1('dddd')
        super().acctpermitno('12345')
        #上传
        super().click_sc()
        super().input_file()
        super().sure_upload()
        super().sure_comm()
        super().sure_final_upload()
        #返回主iframe
        super().switch_default_iframe()
        time.sleep(2)

    @unittest.skip('跳过')
    def test_11_6(self):
        u'''11_6 类型测试'''
        time.sleep(2)
        super().show_tree()
        super().dwzh_hzz()
        super().change_iframe('核准制业务申报')
        super().data_add()
        super().first_businesstype('11')
        super().first_accountattr('6')
        super().sure_yes()
        #录入信息
        super().pbclicencennum('11234')
        super().accountno('11111')
        super().accountname('haha')
        super().certifyfilekind1('asdv')
        super().certifyfileno1('advv')
        super().upregioncode('450100')
        super().regioncode('450101')
        super().acctpermitno('239888')
        super().accountvalidity('2020-04-01')
        # 上传
        super().click_sc()
        super().input_file()
        super().sure_upload()
        super().sure_comm()
        super().sure_final_upload()
        #返回主iframe
        super().switch_default_iframe()
        time.sleep(2)


    # @unittest.skip('跳过')
    def test_11_7(self):
        u'''11_7 类型测试'''
        time.sleep(2)
        super().show_tree()
        super().dwzh_hzz()
        super().change_iframe('核准制业务申报')
        super().data_add()
        super().first_businesstype('11')
        super().first_accountattr('7')
        super().sure_yes()
        #录入信息
        super().accountno('11111')
        super().accountname('haha')
        super().unitname('asdasd')
        super().industrycategory('B')
        super().legalrepresenttative('asd')
        super().lrcertno('12345')
        super().ownerphone('12345')
        super().addr('kkkkkk')
        super().upregioncode('450100')
        super().regioncode('450101')
        super().zipcode('123456')
        super().certifyfilekind1('asdv')
        super().certifyfileno1('advv')
        # 上传
        super().click_sc()
        super().input_file()
        super().sure_upload()
        super().sure_comm()
        super().sure_final_upload()
        #返回主iframe
        super().switch_default_iframe()
        time.sleep(2)

    # @unittest.skip('跳过')
    def test_11_8(self):
        u'''11_8 类型测试'''
        time.sleep(2)
        super().show_tree()
        super().dwzh_hzz()
        super().change_iframe('核准制业务申报')
        super().data_add()
        super().first_businesstype('11')
        super().first_accountattr('7')
        super().sure_yes()
        #录入信息
        super().accountno('11111')
        super().accountname('haha')
        super().unitname('asdasd')
        super().industrycategory('B')
        super().legalrepresenttative('asd')
        super().lrcertno('12345')
        super().ownerphone('12345')
        super().addr('kkkkkk')
        super().upregioncode('450100')
        super().regioncode('450101')
        super().zipcode('123456')
        super().certifyfilekind1('asdv')
        super().certifyfileno1('advv')
        # 上传
        super().click_sc()
        super().input_file()
        super().sure_upload()
        super().sure_comm()
        super().sure_final_upload()
        #返回主iframe
        super().switch_default_iframe()
        time.sleep(2)






if __name__ == "__main__":
    pass