#!/usr/bin/python3
#coding:utf-8
from bs4 import BeautifulSoup
import re
#无法解析<?xml version="1.0" encoding="GB18030"?>
# soup = BeautifulSoup(open('FH0001.xml',encoding='gb18030'),'xml')
# print(soup.extra)
with open('FH0001.xml',encoding='gb18030') as xml_file:
    # 打开文件,定义BeautifulSoup
    soup = BeautifulSoup(xml_file,'xml')
    #格式化输出
    # soup.prettify()
    #直接使用soup.record_num获得标签所有内容
    print(soup.record_num)
    print("=====================")
    #获得标签 inputname 的值
    print(soup.inputname.get_text())
    #string 无法获得包含多个子节点
    print(soup.inputname.string)
    print(soup.extra.string)
    #修改string内容
    soup.inputname.string.replace_with('other_inputname')
    print(soup.inputname.string)
    print("=====================")
    #修改了标签名
    soup.ex_tab.name = "other_ex_tab"
    print(soup.other_ex_tab.name)
    soup.other_ex_tab.name = "ex_tab"
    print(soup.ex_tab.name)
    print("=====================")
    #获得标签的属性,字典格式
    print(soup.fiscmemo.attrs)
    #获得other的属性
    print(soup.fiscmemo['other'])
    #直接修改属性值
    soup.fiscmemo['ID'] = 5
    print(soup.fiscmemo['ID'])
    print("=====================")
    #获得所有的fiscmemo的 other的属性
    for no in soup.find_all('fiscmemo'):
        print(no.get('other'),no.get('ID'))
    print("=====================")
    #以列表的形式获得标签下的内容
    print(soup.fiscmemo.contents)
    print("---------------------")
    #获得父节点
    print(soup.fiscmemo.parent)
    print("---------------------")
    for parent in soup.fiscmemo.parents:
        if parent is None:
            print(parent)
        else:
            print(parent.name)
    print("---------------------")
    #获得子节点
    for child in soup.extra.children:
        print(child)
    print("+++++++++++++++++++++")
    for child in soup.extra.descendants:
        print(child)

    for tag in soup.find_all(re.compile("op")):
        print(tag.name)


    print("&&&&&&&&&&&&&&&&&&&&&")
    #find_all  name
    print(soup.find_all('scode'))
    #find_all  keyword
    print(soup.find_all(other='other'))
    print(soup.find_all(other=re.compile("othe")))
    #find_all  attrs
    print(soup.find_all(attrs={"ID":"2"}))
    #css搜索,class python保留字段, 使用class_
    #find_all string
    print('############################')
    print(soup.find_all(string='text_old_itemno'))
    print(soup.find_all(string=['text_old_itemno','text_listdtl','text_listamount']))
    #find_all limit 限制返回数量
    print(soup.find_all('fiscmemo',limit=2))
    print('############################')
    #find_all 查找在nbrcs下的子节点，并不找孙子节点
    print(soup.nbrcs.find_all('fiscmemo',recursive=False))
    print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
    #css select选择器
    #通过标签组成查找
    print(soup.select("extra multi fiscmemo taxcounts"))
    #找到某个标签下的直接子标签
    print(soup.select("extra > multi > fiscmemo > moneycounts") )
    #找到兄弟节点
    print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
    #修改标签名，增加属性，删除属性
    soup_nbrcs = soup.nbrcs
    soup_nbrcs.name = 'woshishe'
    soup_nbrcs['id'] = 1
    print(soup_nbrcs)
    print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
    print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
    del soup_nbrcs['id']
    print(soup_nbrcs)
    print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
    #修改string值
    print(soup.listamount)
    soup.listamount.string = 'haha'
    print(soup.listamount)
    soup.listamount.append('ku')
    print(soup.listamount)
    print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
    #构造一个新的标签
    tag = soup.record_num
    print(tag)
    new_tag = soup.new_tag("a",href="http://bing.com")
    new_tag.string = "zeml"
    tag.append(new_tag)
    print(tag)
    tag.insert(1,'taimeil')
    print(tag.contents)
    print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
    tag_i = soup.new_tag('i')
    tag_i.string = "i love you"
    # soup.record_num.a.insert_before(tag_i)
    soup.record_num.a.string.insert_before(tag_i)
    print(soup.record_num)
    #清空标签内容
    soup.record_num.i.clear()
    print(soup.record_num)
    #删除节点
    soup.record_num.i.decompose()
    print(soup.record_num)
    #replace_with() 替换标签及内容
    new_tag = soup.new_tag('b')
    new_tag.string = 'i LOVE u'
    new_tag.attrs={'ID':2}
    soup.record_num.a.replace_with(new_tag)
    print(soup.record_num)
    #包装 解包
    print('!!!!!!!!!!!!!!!!!!!!')
    soup.record_num.b.string.wrap(soup.new_tag('c'))
    print(soup.record_num)
    soup.record_num.b.wrap(soup.new_tag('d'))
    print(soup.record_num)
    soup.record_num.c.unwrap()
    print(soup.record_num)
    #格式化输出
    print(soup.record_num.prettify())
    print(str(soup.record_num))
    print('::::::::::::::::::::::::::::')
    #获得所有文本
    print(soup.get_text("|"))
    print([text for text in soup.stripped_strings])
    with open('new_xml.xml','w') as f:
        f.write(str(soup))
        f.close()





