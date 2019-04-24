#!/usr/bin/python3
#coding:utf-8
import time
from 普惠金融.前置.hzz_zj_ele import find_html_ele
from 普惠金融.config import *
import unittest

class hzz_data_add_11(find_html_ele):
    u'''账户核准制增加-11类型'''
    # @unittest.skip('跳过')
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
        super().accountno_11('11111')
        super().accountname_11('haha')
        super().unitname_11('aaaa')
        super().legalrepresenttative_11('12344')
        super().lrcertno_11('jjjjj')
        super().addr_11('123jjjj')
        super().ownerphone_11('111122')
        super().zipcode_11('12134')
        super().certifyfilekind1_11('asdv')
        super().certifyfileno1_11('advv')
        super().industrycategory_11('B')
        super().depositorattr_11('02')
        super().upregioncode_11('450100')
        super().regioncode_11('450101')
        # 上传
        super().click_sc()
        super().input_file()
        super().sure_upload()
        super().sure_comm()
        # super().sure_final_upload()
        #返回主iframe
        super().switch_default_iframe()
        time.sleep(2)

    @unittest.skip('跳过')
    def test_11_3(self):
        u'''11_3 类型测试'''
        #菜单
        super().show_tree()
        super().dwzh_hzz()
        super().change_iframe('核准制业务申报')
        super().data_add()
        super().first_businesstype('11')
        super().first_accountattr('3')
        super().sure_yes()
        #录入
        super().accountno_11('233333')
        super().accountname_11('aaaaa')
        super().upregioncode_11('450100')
        super().regioncode_11('450101')
        super().certifyfilekind1_11('aaaaa')
        super().certifyfileno1_11('dddd')
        super().acctpermitno_11('12345')
        #上传
        super().click_sc()
        super().input_file()
        super().sure_upload()
        super().sure_comm()
        # super().sure_final_upload()
        #返回主iframe
        super().switch_default_iframe()
        time.sleep(2)

    @unittest.skip('跳过')
    def test_11_4(self):
        u'''11_4 类型测试'''
        #菜单
        super().show_tree()
        super().dwzh_hzz()
        super().change_iframe('核准制业务申报')
        super().data_add()
        super().first_businesstype('11')
        super().first_accountattr('4')
        super().sure_yes()
        #录入
        super().accountno_11('233333')
        super().accountname_11('aaaaa')
        super().upregioncode_11('450100')
        super().regioncode_11('450101')
        super().certifyfilekind1_11('aaaaa')
        super().certifyfileno1_11('dddd')
        super().acctpermitno_11('12345')
        #上传
        super().click_sc()
        super().input_file()
        super().sure_upload()
        super().sure_comm()
        # super().sure_final_upload()
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
        super().pbclicencennum_11('11234')
        super().accountno_11('11111')
        super().accountname_11('haha')
        super().certifyfilekind1_11('asdv')
        super().certifyfileno1_11('advv')
        super().upregioncode_11('450100')
        super().regioncode_11('450101')
        super().acctpermitno_11('239888')
        super().accountvalidity_11('2020-04-01')
        # 上传
        super().click_sc()
        super().input_file()
        super().sure_upload()
        super().sure_comm()
        # super().sure_final_upload()
        #返回主iframe
        super().switch_default_iframe()
        time.sleep(2)


    @unittest.skip('跳过')
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
        super().accountno_11('11111')
        super().accountname_11('haha')
        super().unitname_11('asdasd')
        super().industrycategory_11('B')
        super().legalrepresenttative_11('asd')
        super().lrcertno_11('12345')
        super().ownerphone_11('12345')
        super().addr_11('kkkkkk')
        super().upregioncode_11('450100')
        super().regioncode_11('450101')
        super().zipcode_11('123456')
        super().certifyfilekind1_11('asdv')
        super().certifyfileno1_11('advv')
        # 上传
        super().click_sc()
        super().input_file()
        super().sure_upload()
        super().sure_comm()
        # super().sure_final_upload()
        #返回主iframe
        super().switch_default_iframe()
        time.sleep(2)

    @unittest.skip('跳过')
    def test_11_8(self):
        u'''11_8 类型测试'''
        time.sleep(2)
        super().show_tree()
        super().dwzh_hzz()
        super().change_iframe('核准制业务申报')
        super().data_add()
        super().first_businesstype('11')
        super().first_accountattr('8')
        super().sure_yes()
        #录入信息
        super().accountno_11('11111')
        super().accountname_11('haha')
        super().unitname_11('asdasd')
        super().industrycategory_11('B')
        super().legalrepresenttative_11('asd')
        super().lrcertno_11('12345')
        super().ownerphone_11('12345')
        super().addr_11('kkkkkk')
        super().upregioncode_11('450100')
        super().regioncode_11('450101')
        super().zipcode_11('123456')
        super().certifyfilekind1_11('asdv')
        super().certifyfileno1_11('advv')
        # 上传
        super().click_sc()
        super().input_file()
        super().sure_upload()
        super().sure_comm()
        # super().sure_final_upload()
        #返回主iframe
        super().switch_default_iframe()
        time.sleep(2)






if __name__ == "__main__":
    pass