#!/bin/bash
#var ip 10.0.244.41/42
#
target_start='sh /home/weaver/Resin/bin/startresin.sh'
target_stop='sh /home/weaver/Resin/bin/stopresin.sh'

tar_zcvf_dir1='cd /home/weaver/ecology/WEB-INF/;tar zcf /tmp/OA_lpt_dir1.tgz lib/'
tar_zcvf_dir2='cd /home/weaver/Resin/;tar zcf /tmp/OA_lpt_dir2.tgz lib/'

tar_zxvf_file1='tar zxf /tmp/OA_lpt_dir1.tgz -C /home/weaver/ecology/WEB-INF/'
tar_zxvf_file2='tar zxf /tmp/OA_lpt_dir2.tgz -C /home/weaver/Resin/'


echo "=============打包验证环境tgz包============="
$HOME/trans.py OA_var cmd  "${tar_zcvf_dir1}"
$HOME/trans.py OA_var cmd  "${tar_zcvf_dir2}"

echo "=============获取验证环境tgz包============="
$HOME/trans.py OA_var get /tmp/OA_lpt_dir1.tgz  $HOME/tmp/OA_lpt_dir2.tgz
$HOME/trans.py OA_var get /tmp/OA_lpt_dir2.tgz  $HOME/tmp/OA_lpt_dir2.tgz

echo "=============传输tgz包至压测环境============="
$HOME/trans.py OA_lpt put $HOME/tmp/OA_lpt_dir1.tgz  /tmp/
$HOME/trans.py OA_lpt put $HOME/tmp/OA_lpt_dir2.tgz  /tmp/

echo "=============停止压测环境服务============="
$HOME/trans.py OA_lpt cmd  "${target_stop}"

echo "=============解压压测环境tar包============="
$HOME/trans.py OA_lpt cmd  "${tar_zxvf_file1}"
$HOME/trans.py OA_lpt cmd  "${tar_zxvf_file2}"


echo "=============启动压测环境服务============="
$HOME/trans.py OA_lpt cmd  "${target_start}"
