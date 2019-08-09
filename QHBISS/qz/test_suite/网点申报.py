#!/usr/bin/python3
#coding:utf-8
from public.qh_ele import find_html_ele
import time
from public.configuer import bank_list

class gdgl(find_html_ele):
    u'''网点管理'''
    def test_0002(self):
        super().enter()
        super().jcgngl()
        time.sleep(2)
        super().wdgl()
        super().change_iframe('网点管理')
        for i in bank_list[::-1]:
            super().data_add()
            t = 1
            super().change_iframe_times(t)
            org_number = str(int(i) + 10000 )
            #银行机构代码
            super().data_add_branchCode(org_number)
            #银行名称
            super().data_add_branchName('自动化测试机构')
            #金融机构编码
            super().data_add_finacialCode('9988776655')
            #参与者
            super().data_add_belonBankCode(i)
            #归属人行
            super().data_add_pbcCode('')
            #启用日期
            super().data_add_enableDate('2019-08-01')
            super().change_iframe_father()
            super().data_add_sure(t)
            t = t + 2
            time.sleep(1)





if __name__ == "__main__":
    pass