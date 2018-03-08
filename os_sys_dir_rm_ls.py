#!/usr/bin/env python3
#-*- coding:gbk -*-
import sys
import os
import shutil
ret = os.getcwd()
print('当前路径: {:s}'.format(str(ret)))
os.makedirs("./txt/exp1",mode=0o755)
print('创建多级文件夹 /txt/exp1 755 ')
os.mkdir("./txt/exp2",mode=0o755)
print('创建单级文件夹 /txt/exp2 755 ')
os.chdir("./txt/")
ret = os.getcwd()
print('当前路径: {:s}'.format(str(ret)))
shutil.move('exp1','exp3')
print('重命名 exp1 -- exp3    shutil.move')
shutil.copytree('exp3','exp1')
print('复制exp3 为 exp1      shutil.copytree')
#fp = open('text.txt',w)
#11111111111111
#print('ls')
#os.system('ls')
os.chdir("../")
shutil.rmtree('txt')









