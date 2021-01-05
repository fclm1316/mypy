#!/bin/bash
#203.3.237.187/188
#
target_start="cd /home/tsywmsp/cabi/;sh startup.sh"
target_stop="cd /home/tsywmsp/cabi/;sh shutdown.sh"

file_path="/home/tsywmsp/cabi/"
tar_file="CABI_lpt_dir1.tgz"
#target_tar="cabi-service-impl-*.jar"

tar_zcvf_dir1="cd ${file_path};ls -t cabi-service-impl-*|head -n1|xargs tar zcf /tmp/${tar_file}"

tar_zxvf_file1="tar zxf /tmp/${tar_file} -C ${file_path}"


echo "=============打包验证环境tgz包============="
$HOME/trans.py CABI_var cmd  "${tar_zcvf_dir1}"

echo "=============获取验证环境tgz包============="
$HOME/trans.py CABI_var get /tmp/${tar_file}  $HOME/tmp/${tar_file}

echo "=============传输tgz包至压测环境============="
$HOME/trans.py CABI_lpt put $HOME/tmp/${tar_file}  /tmp/

echo "=============停止压测环境服务============="
$HOME/trans.py CABI_lpt cmd  "${target_stop}"

echo "=============解压压测环境tar包============="
$HOME/trans.py CABI_lpt cmd  "${tar_zxvf_file1}"

echo "=============启动压测环境服务============="
$HOME/trans.py CABI_lpt cmd  "${target_start}"
