#!/usr/bin/python3
# coding:utf-8
import sys
import os
import xml.etree.ElementTree as ET

try:
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    output_file2 = sys.argv[3]
except Exception:
    print("usg : {:s}  input_file  output_file  output_xml ".format(sys.argv[0]))
    sys.exit()
# 使用命令
cmd = './demo'
# 解析
tree = ET.parse(input_file)
root = tree.getroot()
# 创建新元素
new_root = ET.Element('nbrcs')
# 子元素
new_Multi = ET.SubElement(new_root, 'Multi')


# 查找元素，生成子元素
def root_find2(sub_path, subelement):
    name = root.find(subelement)
    new_name = ET.SubElement(sub_path, subelement)
    new_name.text = name.text


root_find2(new_root, 'lznetid')
root_find2(new_root, 'lzdate')
root_find2(new_root, 'lzbatchno')
root_find2(new_root, 'payflag')
root_find2(new_root, 'anslimitdate')
root_find2(new_root, 'anslimitnettingno')
root_find2(new_root, 'total_cnt')
root_find2(new_root, 'total_amt')
# 查找子元素
for child in root:
    if str(child.tag) == 'Multi':
        for childs in child:
            # 使用函数
            wznetid = childs.find('wznetid').text
            wzdate = childs.find('wzdate').text
            wzbatchno = childs.find('wzbatchno').text
            batchitemno = childs.find('batchitemno').text
            new_detail = ET.SubElement(new_Multi, childs.tag, childs.attrib)
            new_wznetid = ET.SubElement(new_detail, 'wznetid')
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
            new_brcode = ET.SubElement(new_detail, 'brcode')
            new_brname = ET.SubElement(new_detail, 'brname')
# 生成树
new_tree = ET.ElementTree(new_root)
# 写数
new_tree.write(output_file, encoding='gb18030', xml_declaration=True)
# #ET.dump(new_tree)
# 第二个xml
new_root2 = ET.Element('nbrcs')
root_find2(new_root2, 'lznetid')
root_find2(new_root2, 'lzdate')
root_find2(new_root2, 'lzbatchno')
root_find2(new_root2, 'payflag')
# 生成新元素
new_msflag2 = ET.SubElement(new_root2, 'msflag')
new_msflag2.text = '0'
new_dealflag2 = ET.SubElement(new_root2, 'dealflag')
new_dealflag2.text = '37'
new_bacode2 = ET.SubElement(new_root2, 'bacode')
new_brname2 = ET.SubElement(new_root2, 'brname')
new_file2 = ET.SubElement(new_root2, 'file')
new_filename = ET.SubElement(new_file2, 'filename')
# new_filename.text = output_file
new_filename.text = os.path.basename(output_file)
new_filecheck = ET.SubElement(new_file2, 'filecheck')
# 调用demo
new_filecheck.text = os.popen("{0:s} {1:s}".format(cmd, output_file)).read()
new_filetype = ET.SubElement(new_file2, 'filetype')
new_filetype.text = '03'
new_tree2 = ET.ElementTree(new_root2)
new_tree2.write(output_file2, encoding='gb18030', xml_declaration=True)
