#!/usr/bin/python3
#coding:utf-8

from 普惠金融.前置.hzz_fh_ele import find_html_ele
from 普惠金融.config import *
import unittest

class hzz_data_fh(find_html_ele):
    u'''复核通过'''
    @unittest.skip('跳过')
    def test_01(self):
        time.sleep(2)
        for a in range(10):
            super().show_tree()
            super().dwzh_hzz()
            super().change_iframe('核准制业务复核')
            super().fuhe()
            super().fuhe_tg()
            time.sleep(3)
            super().fuhe_sure()

            time.sleep(5)

    def test_02(self):
        u'''复核不通过'''
        super().show_tree()
        super().dwzh_hzz()
        super().change_iframe('核准制业务复核')
        for a in range(50):
            super().fuhe()
            super().tuihui('退回了')
            super().tuihui_tg()
            time.sleep(1)
            super().fuhe_sure()









if __name__ == "__main__":
    pass