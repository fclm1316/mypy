#!/usr/bin/python3
#coding:utf-8

from 普惠金融.前置.hzz_zj_ele import find_html_ele
from 普惠金融.config import *
import unittest

class hzz_data_add_21(find_html_ele):
    u'''账户核准制增加-21类型'''
    # @unittest.skip('跳过')
    def test_21_2(self):
        u'''21_2 类型测试'''
        time.sleep(2)
        super().show_tree()
        super().dwzh_hzz()
        super().change_iframe('核准制业务申报')
        super().data_add()
        super().first_businesstype('21')
        super().first_accountattr('2')
        super().sure_yes()
        #录入信息
        super().add_ele_21_22('accountno', '123123123123')
        super().add_ele_21_22('accountname', 'asdasdasd')
        super().add_ele_21_22('unitname', 'asdasd')
        super().add_ele_21_22('legalrepresenttative', 'asdasd')
        super().industrycategory_21('B')
        super().add_ele_21_22('lrcertno', '123123')
        super().add_ele_21_22('ownerphone', '123123')
        super().add_ele_21_22('addr', '231123123')
        super().upregioncode1_21('450100')
        super().regioncode1_21('450101')
        super().add_ele_21_22('zipcode', '123123')
        super().add_ele_21_22('certifyfilekind1', '123123')
        super().add_ele_21_22('certifyfileno1', '123123')
        super().change_ele_21_22('accountname', 'adshbbb')
        super().change_ele_21_22('legalrepresenttative', 'kkkklllll')
        # 上传
        super().click_sc()
        super().input_file()
        super().sure_upload()
        super().sure_comm()
        time.sleep(2)
        super().sure_final_upload()
        #返回主iframe
        super().switch_default_iframe()

    @unittest.skip('跳过')
    def test_21_3(self):
        u'''21_3 类型测试'''
        time.sleep(2)
        super().show_tree()
        super().dwzh_hzz()
        super().change_iframe('核准制业务申报')
        super().data_add()
        super().first_businesstype('21')
        super().first_accountattr('3')
        super().sure_yes()
        #录入信息
        super().add_ele_21_22('accountno', '123123123123')
        super().add_ele_21_22('accountname', 'asdasdasd')
        super().upregioncode1_21('450100')
        super().regioncode1_21('450101')
        super().add_ele_21_22('certifyfilekind1', '123123')
        super().add_ele_21_22('certifyfileno1', '123123')
        super().add_ele_21_22('acctpermitno', '12344')

        super().change_ele_21_22('accountname', 'adshbbb')
        # 上传
        super().click_sc()
        super().input_file()
        super().sure_upload()
        super().sure_comm()
        time.sleep(2)
        super().sure_final_upload()
        #返回主iframe
        super().switch_default_iframe()

    @unittest.skip('跳过')
    def test_21_4(self):
        u'''21_4 类型测试'''
        time.sleep(2)
        super().show_tree()
        super().dwzh_hzz()
        super().change_iframe('核准制业务申报')
        super().data_add()
        super().first_businesstype('21')
        super().first_accountattr('4')
        super().sure_yes()
        #录入信息
        super().add_ele_21_22('accountno', '123123123123')
        super().add_ele_21_22('accountname', 'asdasdasd')
        super().upregioncode1_21('450100')
        super().regioncode1_21('450101')
        super().add_ele_21_22('certifyfilekind1', '123123')
        super().add_ele_21_22('certifyfileno1', '123123')
        super().add_ele_21_22('acctpermitno', '12344')

        super().change_ele_21_22('accountname', 'adshbbb')
        # 上传
        super().click_sc()
        super().input_file()
        super().sure_upload()
        super().sure_comm()
        time.sleep(2)
        super().sure_final_upload()
        #返回主iframe
        super().switch_default_iframe()

    @unittest.skip('跳过')
    def test_21_7(self):
        u'''21_7 类型测试'''
        time.sleep(2)
        super().show_tree()
        super().dwzh_hzz()
        super().change_iframe('核准制业务申报')
        super().data_add()
        super().first_businesstype('21')
        super().first_accountattr('7')
        super().sure_yes()
        #录入信息
        super().add_ele_21_22('accountno', '123123123123')
        super().add_ele_21_22('accountname', 'asdasdasd')
        super().add_ele_21_22('unitname', '313123213')
        super().industrycategory_21('B')
        super().add_ele_21_22('legalrepresenttative', 'dsdsad')
        super().add_ele_21_22('lrcertno', '12323')
        super().add_ele_21_22('ownerphone', '33333')
        super().add_ele_21_22('addr', 'pppppp')
        super().upregioncode1_21('450100')
        super().regioncode1_21('450101')
        super().add_ele_21_22('zipcode', '999999')
        super().add_ele_21_22('certifyfilekind1', '123123')
        super().add_ele_21_22('certifyfileno1', '123123')

        super().change_ele_21_22('accountname', 'adshbbb')
        super().change_ele_21_22('legalrepresenttative', 'kkkklllll')
        # 上传
        super().click_sc()
        super().input_file()
        super().sure_upload()
        super().sure_comm()
        time.sleep(2)
        super().sure_final_upload()
        #返回主iframe
        super().switch_default_iframe()

    @unittest.skip('跳过')
    def test_21_8(self):
        u'''21_8 类型测试'''
        time.sleep(2)
        super().show_tree()
        super().dwzh_hzz()
        super().change_iframe('核准制业务申报')
        super().data_add()
        super().first_businesstype('21')
        super().first_accountattr('8')
        super().sure_yes()
        #录入信息
        super().add_ele_21_22('accountno', '123123123123')
        super().add_ele_21_22('accountname', 'asdasdasd')
        super().add_ele_21_22('unitname', '313123213')
        super().industrycategory_21('B')
        super().add_ele_21_22('legalrepresenttative', 'dsdsad')
        super().add_ele_21_22('lrcertno', '12323')
        super().add_ele_21_22('ownerphone', '33333')
        super().add_ele_21_22('addr', 'pppppp')
        super().upregioncode1_21('450100')
        super().regioncode1_21('450101')
        super().add_ele_21_22('zipcode', '999999')
        super().add_ele_21_22('certifyfilekind1', '123123')
        super().add_ele_21_22('certifyfileno1', '123123')

        super().change_ele_21_22('accountname', 'adshbbb')
        super().change_ele_21_22('legalrepresenttative', 'kkkklllll')
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