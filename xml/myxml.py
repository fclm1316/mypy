#!/usr/bin/python3
#coding:utf-8
import xml.etree.ElementTree as ET
import os
import re
import sys
import os
import xml.etree.cElementTree as ET
input_file = sys.argv[1]
pattern = re.compile(r'<UFTP>.*</UFTP>',re.I)
#input_file_new = str(os.path.basename(input_file).split('.')[0] + '_new.000')
input_file_new = str(os.path.abspath(input_file).split('.')[0] +  '_new.000')
print(input_file_new)
with open(input_file,'r',newline='') as file:
    with open(input_file_new,'a',newline='') as wirt_file:
    #lines = enumerate(file)
    #for i,j in lines:
    #    if not j.startswith('####') and len(j)>2:
    #        if pattern.search(j):
    #           print(j)
        for line in file:
            if pattern.search(line):
                wirt_file.writelines(line)
            # else:
            #     if not line.startswith('####') and not line.startswith('<?xml'):
            #         print(line)
