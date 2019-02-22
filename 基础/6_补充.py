#!/usr/bin/python3
#coding:utf-8
list_1 = ['超人','蝙蝠侠','神奇女侠','闪电侠','绿灯侠','海王','钢骨']
list_2 = ['钢铁侠','美国队长','绿巨人','雷神','鹰眼','黑寡妇']
#一次增加多个
list_2.extend(['星爵','蚁人','绿巨人'])
print(list_2)
#默认最后一个
list_1.pop()
print(list_1)
list_1.pop(0)
print(list_1)
#列表去重
list_4 = set(list_2)
print(list_4)
