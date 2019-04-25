#!/usr/bin/python3
#coding:utf-8

from 普惠金融.前置.hzz_zj_ele import find_html_ele
from 普惠金融.config import *
import unittest

class hzz_data_add_74(find_html_ele):
    u'''账户核准制增加74类型'''
    # @unittest.skip('跳过')
    def test_74(self):
        u'''74 类型测试'''
        time.sleep(2)
        super().show_tree()
        super().dwzh_hzz()
        super().change_iframe('核准制业务申报')
        super().data_add()
        super().first_businesstype('74')
        super().sure_yes()
        #录入信息
        super().add_ele_50_71_72_73_74('accountno', test_number)
        super().add_ele_50_71_72_73_74('accountname', test_text)
        super().accountvalidity_74('2020-01-01')
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