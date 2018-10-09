#!/usr/bin/python3
#coding:utf-8
import sys
import os
import xml.etree.ElementTree as ET
input_file = sys.argv[1]
tree = ET.parse(input_file)
root = tree.getroot()
new_root = ET.Element('nbrcs')
new_Multi = ET.SubElement(new_root,'Multi')

for child in root:
    if str(child.tag) == 'Multi':
        for childs in child:
            #print(childs.tag,childs.attrib)
            wznetid = childs.find('wznetid').text
            wzdate = childs.find('wzdate').text
            wzbatchno = childs.find('wzbatchno').text
            batchitemno = childs.find('batchitemno').text
        #    print(wznetid,wzdate,wzbatchno,childs.tag,childs.attrib)
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
lznetid = root.find('lznetid').text
new_lzbetid = ET.SubElement(new_root,'lznetid')
new_lzbetid.text = lznetid

lzdate = root.find('lzdate').text
new_lzdate = ET.SubElement(new_root,'lzdate')
new_lzdate.text = lzdate

lzbatchno = root.find('lzbatchno').text
new_lzbatchno = ET.SubElement(new_root,'lzbatchno')
new_lzbatchno.text = lzbatchno

payflag = root.find('payflag').text
new_payflag = ET.SubElement(new_root,'payflag')
new_payflag.text = payflag

anslimitdate = root.find('anslimitdate').text
new_anslimitdate = ET.SubElement(new_root,'anslimitdate')
new_anslimitdate.text = anslimitdate

anslimitnettingno = root.find('anslimitnettingno').text
new_anslimitnettingno = ET.SubElement(new_root,'anslimitnettingno')
new_anslimitnettingno.text = anslimitnettingno

total_cnt = root.find('total_cnt').text
new_total_cnt = ET.SubElement(new_root,'total_cnt')
new_total_cnt.text = total_cnt

total_amt = root.find('total_amt').text
new_total_amt = ET.SubElement(new_root,'total_amt')
new_total_amt.text = total_amt

new_tree = ET.ElementTree(new_root)
new_tree.write("test.xml",encoding='gb18030',xml_declaration=True)
#ET.dump(new_tree)
