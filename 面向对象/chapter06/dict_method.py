#!/usr/bin/python3
#coding:utf-8
a = {"aa1":{"bb1":"cc1"},
     "aa2":{"bb2":"cc2"}
     }
# a.clear()
#浅拷贝,影响到了a
# new_dict = a.copy()
# new_dict["aa1"]["bb1"] =["cc4"]
# print(a)
# print(new_dict)
#深拷贝
import copy
new_dict = copy.deepcopy(a)
new_dict["aa1"]["bb1"] = ["cc4"]
print(new_dict)
print(a)

#fromkeys
new_list =["aa","bb"]
new_list = dict.fromkeys(new_list,{"aa":"vv"})

#get() 获得值

#設置默认值
new_dict.setdefault('dd','oo')
print(new_dict)

new_dict.update({"kk":"ss"})
new_dict.update(aa1="ll",bb1="00")
new_dict.update([('aa2','bnn2')])
new_dict.update((('aa2','bnn2'),('bb2','uu')))
print(new_dict)
