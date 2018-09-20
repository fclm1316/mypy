#!/usr/bin/python3
#coding:utf-8
import sys
import os
import glob
import difflib
import re
def read_file(filename):
    try:
        with open(filename, 'r') as f:
            return f.readlines()
    except IOError:
        print("ERROR: file :%s not found " % filename)
        sys.exit(1)
try:
    input_path1 = sys.argv[1]
    input_path2 = sys.argv[2]
    out_file = sys.argv[3]
except Exception as e:
    print("ERROR %s" % e)
    print("usg : %s dir dir out_file_name" % sys.argv[0])
    sys.exit()
diff_file_list =[]
for file_all_1 in glob.glob(os.path.join(input_path1,"*")):
    file_all_name = os.path.basename(file_all_1)
    #print(file_all_name)
    if os.path.exists(input_path2 + '/' + file_all_name ):
        file1_content = read_file(file_all_1)
        file2_content = read_file(input_path2 + '/' + file_all_name )
        d = difflib.Differ()
        diff = d.compare(file1_content,file2_content)
        pattern = re.compile('\+')
        diff_file = '\n'.join(list(diff))
        if pattern.search(diff_file):
            diff_file_txt = os.path.join(file_all_name + '.txt')
#            print(diff_file)
            with open(diff_file_txt,'w') as f :
                f.writelines(diff_file)
    else:
        diff_file_list.append(file_all_name)
with open (out_file,'w',newline='') as f:
    f.writelines(str(diff_file_list))
