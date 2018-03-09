#!/usr/bin/env python3
#-*- coding:utf-8 -*-
import glob
import os
import shutil
ret = os.getcwd()
print('当前路径: {:s}'.format(str(ret)))
os.makedirs("./txt/exp1",mode=0o777)
print('创建多级文件夹 /txt/exp1 755 ')
os.mkdir("./txt/exp2",mode=0o777)
print('创建单级文件夹 /txt/exp2 755 ')
os.chdir("./txt/")
ret = os.getcwd()
print('当前路径: {:s}'.format(str(ret)))
shutil.move('exp1','exp3')
print('重命名 exp1 -- exp3    shutil.move')
shutil.copytree('exp3','exp1')
print('复制exp3 为 exp1      shutil.copytree')
#列出文件
print('列出文件：\n{0:s}'.format(str(os.listdir())))
#写入文件
with open('text.txt','w') as f1 :
    f1.write('111')
#列出文件
print('列出文件：\n{0:s}'.format(str(os.listdir())))
#读取文件
with open('text.txt','r') as f2:
    print('读取打印文件：\n{0:s}'.format(f2.read()))
with open('text.txt','a') as f3:
    f3.write('222')
with open('text.txt','r') as f4:
    print('读取打印文件1：\n{0:s}'.format(f4.read()))
with open('text.txt','a+') as f6:
    f6.write('\n333\n')
with open('text.txt','a+') as f5:
    f5.write('444')
with open('text.txt','r') as f4:
    print('读取打印文件2：\n{0:s}'.format(f4.read()))
with open('text.txt','r') as f5:
    print('读取打印文件3：')
    print(f5.readlines())
#插入一行
with open('text.txt','r',newline='') as f6:
    f_ojb = f6.readlines()
    f_ojb.insert(2,'new line\n')
    print(f_ojb)
    with open('new_text.txt','w') as new_f6:
        new_f6.writelines(f_ojb)
    with open('new_text.txt','r',newline='') as new_f6_1:
        print('---------------')
        print(new_f6_1.readlines())
        print('---------------')
#去掉 \n
with open('new_text.txt','r') as f7:
   for line in  f7.readlines():
       #.strip  .lstrip .rstrip
       line = line.strip('\n')
       print(line)
#next
files = glob.glob(os.path.join('../','Alice1*'))
for copy_file in files:
    print(copy_file)
    copy_name = os.path.basename(copy_file)
    print(copy_name)
    shutil.copyfile(copy_file,copy_name)



#print('ls')
#os.system('ls')
#os.chdir("../")
#shutil.rmtree('txt')









