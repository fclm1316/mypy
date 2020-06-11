#!/usr/bin/python3
# coding:utf-8
import sys
import re
import os
import xml.etree.ElementTree as ET

input_file = sys.argv[1]
new_xml = 'new_xml.xml'
new_txt = 'new_txt.txt'


def del_exists(file_name):
    '''

    :param file_name:
    :return:
    '''
    if os.path.exists(file_name):
        os.remove(file_name)


del_exists(new_xml)
del_exists(new_txt)
# if os.path.exists(new_xml):
#     os.remove(new_xml)
# if os.path.exists(new_txt):
#     os.remove(new_txt)
with open(input_file, 'r', newline='') as r_file:
    with open(new_xml, 'w', newline='') as w_xml:
        # 读取文件后匹配内容
        pattern = re.compile(r'<file>|<filename.*|<filecheck.*|<filetype.*|</file.*', re.I)
        # 写头
        w_xml.writelines('<nbrcs>' + '\n')
        for line in r_file:
            if pattern.search(line):
                # print(line)
                # 匹配写入
                w_xml.writelines(line)
        # 写尾
        w_xml.writelines('</nbrcs>')
tree = ET.parse('new_xml.xml')
root = tree.getroot()
for child in root:
    #    print(child.tag)
    # 获得元素的值，find 只能查找到第一个值，findall迭代查找
    myType = child.find('filetype').text
    # 可通过切片获得
    #    name = child[2].text
    if myType == '02':
        check = child.find('filecheck').text
        name = child.find('filename').text
        new_line = ''.join(name + ' ' + check + ' ' + myType + '\n')
        with open(new_txt, 'a', newline='') as w_txt:
            #   print(new_line)
            w_txt.writelines(new_line)
