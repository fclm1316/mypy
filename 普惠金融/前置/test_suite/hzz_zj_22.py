#!/usr/bin/python3
#coding:utf-8

from 普惠金融.前置.hzz_zj_ele import find_html_ele
from 普惠金融.config import *
import unittest

class hzz_data_add_22(find_html_ele):
    u'''账户核准制增加-22类型'''
    # @unittest.skip('跳过')
    def test_22_2(self):
        u'''22_2 类型测试'''
        time.sleep(2)
        super().show_tree()
        super().dwzh_hzz()
        super().change_iframe('核准制业务申报')
        super().data_add()
        super().first_businesstype('22')
        super().first_accountattr('2')
        super().sure_yes()
        #录入信息
        super().add_ele_21_22('accountno', test_number)
        super().add_ele_21_22('accountname', test_text)
        super().add_ele_21_22('unitname', test_text)
        super().add_ele_21_22('legalrepresenttative', test_text)
        super().industrycategory_21('B')
        super().add_ele_21_22('lrcertno', test_number)
        super().add_ele_21_22('ownerphone', test_number)
        super().add_ele_21_22('addr', test_number)
        super().upregioncode1_21('450100')
        super().regioncode1_21('450101')
        super().add_ele_21_22('zipcode', test_number)
        super().add_ele_21_22('certifyfilekind1', test_number)
        super().add_ele_21_22('certifyfileno1', test_number)

        super().change_ele_21_22('addr', 'adshbbb')
        # 上传
        super().click_sc()
        super().input_file()
        super().sure_upload()
        super().sure_comm()
        # super().sure_final_upload()
        #返回主iframe
        super().switch_default_iframe()

    # @unittest.skip('跳过')
    def test_22_3(self):
        u'''21_3 类型测试'''
        time.sleep(2)
        super().show_tree()
        super().dwzh_hzz()
        super().change_iframe('核准制业务申报')
        super().data_add()
        super().first_businesstype('22')
        super().first_accountattr('3')
        super().sure_yes()
        #录入信息
        super().add_ele_21_22('accountno', test_number)
        super().add_ele_21_22('accountname', test_text)
        super().upregioncode1_21('450100')
        super().regioncode1_21('450101')
        super().add_ele_21_22('certifyfilekind1', test_number)
        super().add_ele_21_22('certifyfileno1', test_number)
        super().add_ele_21_22('acctpermitno', test_number)

        super().change_ele_21_22('acctpermitno', test_text)
        # 上传
        super().click_sc()
        super().input_file()
        super().sure_upload()
        super().sure_comm()
        # super().sure_final_upload()
        #返回主iframe
        super().switch_default_iframe()

    # @unittest.skip('跳过')
    def test_22_4(self):
        u'''22_4 类型测试'''
        time.sleep(2)
        super().show_tree()
        super().dwzh_hzz()
        super().change_iframe('核准制业务申报')
        super().data_add()
        super().first_businesstype('22')
        super().first_accountattr('4')
        super().sure_yes()
        #录入信息
        super().add_ele_21_22('accountno', test_number)
        super().add_ele_21_22('accountname', test_text)
        super().upregioncode1_21('450100')
        super().regioncode1_21('450101')
        super().add_ele_21_22('certifyfilekind1', test_number)
        super().add_ele_21_22('certifyfileno1', test_number)
        super().add_ele_21_22('acctpermitno', test_number)

        super().change_ele_21_22('acctpermitno', 'adshbbb')
        # 上传
        super().click_sc()
        super().input_file()
        super().sure_upload()
        super().sure_comm()
        # super().sure_final_upload()
        #返回主iframe
        super().switch_default_iframe()

    # @unittest.skip('跳过')
    def test_22_6(self):
        u'''22_6 类型测试'''
        time.sleep(2)
        super().show_tree()
        super().dwzh_hzz()
        super().change_iframe('核准制业务申报')
        super().data_add()
        super().first_businesstype('22')
        super().first_accountattr('6')
        super().sure_yes()
        #录入信息
        super().add_ele_21_22('pbclicencennum',test_number)
        super().add_ele_21_22('accountno', test_number)
        super().add_ele_21_22('accountname', test_text)
        super().upregioncode1_21('450100')
        super().regioncode1_21('450101')
        super().add_ele_21_22('certifyfilekind1', test_number)
        super().add_ele_21_22('certifyfileno1', test_number)
        super().add_ele_21_22('acctpermitno',test_number)
        super().accountvalidity_22('2020-01-01')

        super().change_ele_21_22('addr', test_text)
        # 上传
        super().click_sc()
        super().input_file()
        super().sure_upload()
        super().sure_comm()
        # super().sure_final_upload()
        #返回主iframe
        super().switch_default_iframe()


    # @unittest.skip('跳过')
    def test_22_7(self):
        u'''22_7 类型测试'''
        time.sleep(2)
        super().show_tree()
        super().dwzh_hzz()
        super().change_iframe('核准制业务申报')
        super().data_add()
        super().first_businesstype('22')
        super().first_accountattr('7')
        super().sure_yes()
        #录入信息
        super().add_ele_21_22('accountno', test_number)
        super().add_ele_21_22('accountname', test_text)
        super().add_ele_21_22('unitname', test_number)
        super().industrycategory_21('B')
        super().add_ele_21_22('legalrepresenttative', test_number)
        super().add_ele_21_22('lrcertno', test_number)
        super().add_ele_21_22('ownerphone', test_number)
        super().add_ele_21_22('addr', test_text)
        super().upregioncode1_21('450100')
        super().regioncode1_21('450101')
        super().add_ele_21_22('zipcode', test_number)
        super().add_ele_21_22('certifyfilekind1', test_number)
        super().add_ele_21_22('certifyfileno1', test_number)

        super().change_ele_21_22('addr', 'adshbbb')
        # 上传
        super().click_sc()
        super().input_file()
        super().sure_upload()
        super().sure_comm()
        # super().sure_final_upload()
        #返回主iframe
        super().switch_default_iframe()

    # @unittest.skip('跳过')
    def test_22_8(self):
        u'''22_8 类型测试'''
        time.sleep(2)
        super().show_tree()
        super().dwzh_hzz()
        super().change_iframe('核准制业务申报')
        super().data_add()
        super().first_businesstype('22')
        super().first_accountattr('8')
        super().sure_yes()
        #录入信息
        super().add_ele_21_22('accountno', test_number)
        super().add_ele_21_22('accountname', test_text)
        super().add_ele_21_22('unitname', test_number)
        super().industrycategory_21('B')
        super().add_ele_21_22('legalrepresenttative', test_text)
        super().add_ele_21_22('lrcertno', test_number)
        super().add_ele_21_22('ownerphone', test_number)
        super().add_ele_21_22('addr', test_text)
        super().upregioncode1_21('450100')
        super().regioncode1_21('450101')
        super().add_ele_21_22('zipcode', test_number)
        super().add_ele_21_22('certifyfilekind1', test_number)
        super().add_ele_21_22('certifyfileno1', test_number)

        super().change_ele_21_22('addr', 'kkkklllll')
        # 上传
        super().click_sc()
        super().input_file()
        super().sure_upload()
        super().sure_comm()
        # super().sure_final_upload()
        #返回主iframe
        super().switch_default_iframe()









if __name__ == "__main__":
    pass