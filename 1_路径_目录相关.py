#!/usr/bin/env python3
import sys
import glob
import os
#获得输入参数
input_path = sys.argv[1]
ret = sys.argv
#获得脚本的名称
print('脚本名称是：{0:s}'.format(ret[0]))
#获得脚本的第一个参数
print('当前输入的参数是：{0:s}'.format(ret[1]))
#获得脚本的个数
print('当前输入的参数是：{0:d}'.format(len(ret)))
#获得全部文件
for file_path in glob.glob(os.path.join(input_path,'*.txt')):
	exists = os.path.exists(file_path)
	print('当前文件是否存在: {0:s}'.format(str(exists)))
	link = os.path.islink(file_path)
	print('当前文件是否链接: {0:s}'.format(str(link)))
	mount = os.path.ismount(file_path)
	print('当前文件是否挂载点: {0:s}'.format(str(mount)))
	isabs = os.path.isabs(file_path)
	print('当前文件是否绝对路径: {0:s}'.format(str(isabs)))
	isdir = os.path.isdir(file_path)
	print('当前文件是否是目录: {0:s}'.format(str(isdir)))
	size = os.path.getsize(file_path)
	print('当前文件大小: {0:d}'.format(size))
	print('当前路径 ：{0:s}'.format(file_path))
	abs_path = os.path.abspath(file_path)
	print('绝对路径 ：{0:s}'.format(abs_path))
	base_name = os.path.basename(file_path)
	print('文件名称 ：{0:s}'.format(base_name))
	dir_name = os.path.dirname(file_path)
	print('打印路径名称 ： {0:s}'.format(dir_name))



