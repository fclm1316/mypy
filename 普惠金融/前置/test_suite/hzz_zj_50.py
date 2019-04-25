#!/usr/bin/python3
#coding:utf-8

from 普惠金融.前置.hzz_zj_ele import find_html_ele
from 普惠金融.config import *
import unittest

class hzz_data_add_50(find_html_ele):
    u'''账户核准制增加-50类型'''
    # @unittest.skip('跳过')
    def test_50_2(self):
        u'''50_2 类型测试'''
        time.sleep(2)
        super().show_tree()
        super().dwzh_hzz()
        super().change_iframe('核准制业务申报')
        super().data_add()
        super().first_businesstype('50')
        super().first_accountattr('2')
        super().sure_yes()
        #录入信息
        super().add_ele_50_71_72_73_74('accountno', test_number)
        super().add_ele_50_71_72_73_74('accountname', test_text)
        super().industrycategory_50_71('B')
        super().upregioncode_50('450100')
        super().regioncode_50('450101')
        # 上传
        super().click_sc()
        super().input_file()
        super().sure_upload()
        super().sure_comm()
        time.sleep(2)
        super().sure_final_upload()
        #返回主iframe
        super().switch_default_iframe()

    # @unittest.skip('跳过')
    def test_50_3(self):
        u'''50_3 类型测试'''
        time.sleep(2)
        super().show_tree()
        super().dwzh_hzz()
        super().change_iframe('核准制业务申报')
        super().data_add()
        super().first_businesstype('50')
        super().first_accountattr('3')
        super().sure_yes()
        #录入信息
        super().add_ele_50_71_72_73_74('accountno', test_number)
        super().add_ele_50_71_72_73_74('accountname', test_text)
        super().industrycategory_50_71('B')
        super().upregioncode_50('450100')
        super().regioncode_50('450101')
        # 上传
        super().click_sc()
        super().input_file()
        super().sure_upload()
        super().sure_comm()
        time.sleep(2)
        super().sure_final_upload()
        #返回主iframe
        super().switch_default_iframe()

    # @unittest.skip('跳过')
    def test_50_4(self):
        u'''50_4 类型测试'''
        time.sleep(2)
        super().show_tree()
        super().dwzh_hzz()
        super().change_iframe('核准制业务申报')
        super().data_add()
        super().first_businesstype('50')
        super().first_accountattr('4')
        super().sure_yes()
        #录入信息
        super().add_ele_50_71_72_73_74('accountno', test_number)
        super().add_ele_50_71_72_73_74('accountname', test_text)
        super().industrycategory_50_71('B')
        super().upregioncode_50('450100')
        super().regioncode_50('450101')
        # 上传
        super().click_sc()
        super().input_file()
        super().sure_upload()
        super().sure_comm()
        time.sleep(2)
        super().sure_final_upload()
        #返回主iframe
        super().switch_default_iframe()

    # @unittest.skip('跳过')
    def test_50_6(self):
        u'''50_6 类型测试'''
        time.sleep(2)
        super().show_tree()
        super().dwzh_hzz()
        super().change_iframe('核准制业务申报')
        super().data_add()
        super().first_businesstype('50')
        super().first_accountattr('6')
        super().sure_yes()
        #录入信息
        super().add_ele_50_71_72_73_74('accountno', test_number)
        super().add_ele_50_71_72_73_74('accountname', test_text)
        super().industrycategory_50_71('B')
        super().upregioncode_50('450100')
        super().regioncode_50('450101')
        # 上传
        super().click_sc()
        super().input_file()
        super().sure_upload()
        super().sure_comm()
        time.sleep(2)
        super().sure_final_upload()
        #返回主iframe
        super().switch_default_iframe()

    # @unittest.skip('跳过')
    def test_50_7(self):
        u'''50_7 类型测试'''
        time.sleep(2)
        super().show_tree()
        super().dwzh_hzz()
        super().change_iframe('核准制业务申报')
        super().data_add()
        super().first_businesstype('50')
        super().first_accountattr('7')
        super().sure_yes()
        #录入信息
        super().add_ele_50_71_72_73_74('accountno', test_number)
        super().add_ele_50_71_72_73_74('accountname', test_text)
        super().industrycategory_50_71('B')
        super().upregioncode_50('450100')
        super().regioncode_50('450101')
        # 上传
        super().click_sc()
        super().input_file()
        super().sure_upload()
        super().sure_comm()
        time.sleep(2)
        super().sure_final_upload()
        #返回主iframe
        super().switch_default_iframe()

    # @unittest.skip('跳过')
    def test_50_8(self):
        u'''50_8 类型测试'''
        time.sleep(2)
        super().show_tree()
        super().dwzh_hzz()
        super().change_iframe('核准制业务申报')
        super().data_add()
        super().first_businesstype('50')
        super().first_accountattr('8')
        super().sure_yes()
        #录入信息
        super().add_ele_50_71_72_73_74('accountno', test_number)
        super().add_ele_50_71_72_73_74('accountname', test_text)
        super().industrycategory_50_71('B')
        super().upregioncode_50('450100')
        super().regioncode_50('450101')
        # 上传
        super().click_sc()
        super().input_file()
        super().sure_upload()
        super().sure_comm()
        time.sleep(2)
        super().sure_final_upload()
        #返回主iframe
        super().switch_default_iframe()









if __name__ == "__main__":
    pass