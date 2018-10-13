#!/usr/bin/python3
#coding:utf-8
import sys
import xml.etree.ElementTree as ET

try:
    input_file = sys.argv[1]
    output_file = sys.argv[2]
except Exception :
    print("usg : {:s}  input_file  output_file ".format(sys.argv[0]))
    sys.exit()

tree = ET.parse(input_file)
root = tree.getroot()
new_root = ET.Element('nbrcs')
new_Multi = ET.SubElement(new_root,'Multi')
for child in root:
    if str(child.tag) == 'Multi':
        for childs in child:
            wznetid = childs.find('wznetid').text
            wzdate = childs.find('wzdate').text
            wzbatchno = childs.find('wzbatchno').text
            batchitemno = childs.find('batchitemno').text
            new_detail = ET.SubElement(new_Multi,childs.tag,childs.attrib)
            new_wznetid = ET.SubElement(new_detail,'wznetid')
            new_wznetid.text = wznetid
            new_wzdate = ET.SubElement(new_detail,'wzdate')
            new_wzdate.text = wzdate
            new_wzbatchno = ET.SubElement(new_detail,'wzbatchno')
            new_wzbatchno.text = wzbatchno
            new_batchitemno = ET.SubElement(new_detail,'batchitemno')
            new_batchitemno.text = batchitemno
            new_payflag = ET.SubElement(new_detail,'payflag')
            new_payflag.text = '1'
            new_dealflag = ET.SubElement(new_detail,'dealflag')
            new_dealflag.text = '00'
            new_brcode = ET.SubElement(new_detail, 'brcode')
            new_brname = ET.SubElement(new_detail, 'brname')
def root_find(subelement):
    name = root.find(subelement)
    new_name = ET.SubElement(new_root,subelement)
    new_name.text = name.text
root_find('lznetid')
root_find('lzdate')
root_find('lzbatchno')
root_find('payflag')
root_find('anslimitdate')
root_find('anslimitnettingno')
root_find('total_cnt')
root_find('total_amt')
new_tree = ET.ElementTree(new_root)
new_tree.write(output_file,encoding='gb18030',xml_declaration=True)
#ET.dump(new_tree)
