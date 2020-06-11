#!/usr/bin/python3
# coding:utf-8
import os
import sys
from datetime import date
from ftplib import FTP
import tarfile

BackUpLpath = './'
BackUpRpath = '/tmp'
# BackUpIp = sys.argv[1]
# BackUpUser = sys.argv[2]
# BackUpPwd = sys.argv[3]
# BackUpIp = ''
# BackUpUser = ''
# BackUpPwd = ''
DownLoadPath = './new'
CURDATE = date.today().strftime('%Y%m%d')
tar_file = '%s%s.tar.gz' % (BackUpLpath, CURDATE)


# ftp.cwd(pathname)                 #设置FTP当前操作的路径
# ftp.dir()                         #显示目录下所有目录信息
# ftp.nlst()                        #获取目录下的文件
# ftp.mkd(pathname)                 #新建远程目录
# ftp.pwd()                         #返回当前所在位置
# ftp.rmd(dirname)                  #删除远程目录
# ftp.delete(filename)              #删除远程文件
# ftp.rename(fromname, toname)#将fromname修改名称为toname。
def ftp_backup(host, username, passwd):
    ftp = FTP()
    try:  # 尝试连接服务器
        ftp.connect(host, 21)
        try:  # 尝试登录
            ftp.login(username, passwd)
            # print(ftp.getwelcome())
            # 设置缓存
            bufsize = 1024
            # 二进制方式读取文件
            with open(tar_file, 'rb') as fp:
                # 更换服务器目录
                ftp.cwd(BackUpRpath)
                # 上传文件。STOR 后面是文件名称
                ftp.storbinary('STOR %s' % (tar_file), fp, bufsize)
        # except ftplib.error_perm: #登录失败
        except:  # 登录失败
            print('login error')
    except TimeoutError:  # 连接失败,超时。socket....
        print('time out')
    ftp.quit()
    # ftp.close()


def ftp_download(host, username, passwd):
    ftp = FTP()
    try:  # 尝试连接服务器
        ftp.connect(host, 21)
        try:  # 尝试登录
            ftp.login(username, passwd)
            # print(ftp.getwelcome())
            # 设置缓存
            bufsize = 1024
            # 二进制方式读取文件
            with open(tar_file, 'wb') as fp:
                # os.chdir(DownLoadPath)
                # 更换服务器目录
                ftp.cwd(BackUpRpath)
                # 下载文件。 RETR 后面是文件名称。fp.write 写入文件
                ftp.retrbinary('RETR %s' % (tar_file), fp.write, bufsize)
        # except ftplib.error_perm: #登录失败
        except:  # 登录失败
            print('login error')
    except TimeoutError:  # 连接失败,超时。socket....
        print('time out')
    ftp.quit()


# 获得路径下的所有文件,可换成匹配glob
def ftp_up():
    for root, dir, files in os.walk(BackUpLpath):
        # 创建一个压缩文件w:bz2,w:xz
        tar = tarfile.open(tar_file, 'w:gz')
        # 获得文件
        for file in files:
            # 文件路径
            fullpath = os.path.join(root, file)
            # 丢入tar中
            tar.add(fullpath)
        tar.close()
    if os.path.exists(tar_file):
        ftp_backup(BackUpIp, BackUpUser, BackUpPwd)


def ftp_down():
    # 更换下载路径
    os.chdir(DownLoadPath)
    # 下载文件
    ftp_download(BackUpIp, BackUpUser, BackUpPwd)
    # 读取gz文件
    tar = tarfile.open(tar_file, 'r:gz')
    # 获得tar包中的文件
    file_names = tar.getnames()
    for file_name in file_names:
        # 将获得的文件解开，这里可以筛选解压的文件
        tar.extract(file_name, './')
    tar.close()


if len(sys.argv) != 4:
    print(('{0:s}  backupip  user pwd').format(sys.argv[0]))
    sys.exit()
else:
    BackUpIp = sys.argv[1]
    BackUpUser = sys.argv[2]
    BackUpPwd = sys.argv[3]

ftp_up()
# ftp_down()
