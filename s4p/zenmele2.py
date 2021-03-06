#!/usr/bin/python3
# coding:utf-8
# 应该有更好的办法获得元素的值和属性，而不是一个一个获取
import sys
import xml.etree.ElementTree as ET

try:
    input_file = sys.argv[1]
    output_file = sys.argv[2]
except Exception:
    print("usg : {:s}  input_file  output_file ".format(sys.argv[0]))
    sys.exit()

tree = ET.parse(input_file)
root = tree.getroot()
# 定义新元素
new_root = ET.Element('nbrcs')
# 在新的根元素下产生Multi
new_Multi = ET.SubElement(new_root, 'Multi')
# 寻找Multi标签
for child in root:
    if str(child.tag) == 'Multi':
        for childs in child:
            # print(childs.tag,childs.attrib)
            # 获得需要的标签的值
            wznetid = childs.find('wznetid').text
            wzdate = childs.find('wzdate').text
            wzbatchno = childs.find('wzbatchno').text
            batchitemno = childs.find('batchitemno').text
            #    print(wznetid,wzdate,wzbatchno,childs.tag,childs.attrib)
            # 新xml的在new_Multi下
            new_detail = ET.SubElement(new_Multi, childs.tag, childs.attrib)
            # 元素坐在的位置，名称，属性
            new_wznetid = ET.SubElement(new_detail, 'wznetid')
            # 元素的值
            new_wznetid.text = wznetid
            new_wzdate = ET.SubElement(new_detail, 'wzdate')
            new_wzdate.text = wzdate
            new_wzbatchno = ET.SubElement(new_detail, 'wzbatchno')
            new_wzbatchno.text = wzbatchno
            new_batchitemno = ET.SubElement(new_detail, 'batchitemno')
            new_batchitemno.text = batchitemno
            new_payflag = ET.SubElement(new_detail, 'payflag')
            new_payflag.text = '1'
            new_dealflag = ET.SubElement(new_detail, 'dealflag')
            new_dealflag.text = '00'


# 可以定义一个函数，减少代码
def root_find(subelement):
    name = root.find(subelement)
    new_name = ET.SubElement(new_root, subelement)
    new_name.text = name.text


# lznetid = root.find('lznetid').text
# new_lzbetid = ET.SubElement(new_root,'lznetid')
# new_lzbetid.text = lznetid

# lzdate = root.find('lzdate').text
# new_lzdate = ET.SubElement(new_root,'lzdate')
# new_lzdate.text = lzdate
#
# lzbatchno = root.find('lzbatchno').text
# new_lzbatchno = ET.SubElement(new_root,'lzbatchno')
# new_lzbatchno.text = lzbatchno
#
# payflag = root.find('payflag').text
# new_payflag = ET.SubElement(new_root,'payflag')
# new_payflag.text = payflag
#
# anslimitdate = root.find('anslimitdate').text
# new_anslimitdate = ET.SubElement(new_root,'anslimitdate')
# new_anslimitdate.text = anslimitdate
#
# anslimitnettingno = root.find('anslimitnettingno').text
# new_anslimitnettingno = ET.SubElement(new_root,'anslimitnettingno')
# new_anslimitnettingno.text = anslimitnettingno
#
# total_cnt = root.find('total_cnt').text
# new_total_cnt = ET.SubElement(new_root,'total_cnt')
# new_total_cnt.text = total_cnt
#
# total_amt = root.find('total_amt').text
# new_total_amt = ET.SubElement(new_root,'total_amt')
# new_total_amt.text = total_amt
root_find('lznetid')
root_find('lzdate')
root_find('lzbatchno')
root_find('payflag')
root_find('anslimitdate')
root_find('anslimitnettingno')
root_find('total_cnt')
root_find('total_amt')
# 生成树
new_tree = ET.ElementTree(new_root)
# 树写文件头
new_tree.write(output_file, encoding='gb18030', xml_declaration=True)
# ET.dump(new_tree)
