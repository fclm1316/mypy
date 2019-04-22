#!/usr/bin/python3
#coding:utf-8
import numbers
class Group:
    def __init__(self,group_name,company_name,staffs):
        self.group_name = group_name
        self.company_name = company_name
        self.staffs = staffs

    def __reversed__(self):
       self.staffs.reverse()

    def __getitem__(self, item):
        cls = type(self)
        if isinstance(item,slice):
            return cls(group_name=self.group_name,company_name=self.company_name,staffs=self.staffs[item])
        #判断是否整数
        elif isinstance(item,numbers.Integral):
            return cls(group_name=self.group_name,company_name=self.company_name,staffs=[self.staffs[item]])

    def __len__(self):
        return len(self.staffs)

    def __iter__(self):
        return iter(self.staffs)

    def __contains__(self, item):
        if item in self.staffs:
            return True
        else:
            return False

staffs = ['aa','bb','cc']
group = Group(company_name='aa',group_name='user',staffs=staffs)
sub_group = group[2]
print(sub_group)
print(len(group))
if "dd" in group:
    print("yes")
else:
    print("no")

for a in group:
    print(a)