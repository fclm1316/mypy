#!/bin/bash
#services       192.3.239.110/111
#
afrp_path="/home/admin/afrp"
afrp_start="source .bash_profile;cd ${afrp_path};sh start.sh afrp-service.jar"
afrp_stop="source .bash_profile;cd ${afrp_path};sh stop.sh afrp-service.jar"
afrp_file="afrp-service.tgz"
afrp_tgz="cd ${afrp_path};tar zcf /tmp/${afrp_file} afrp-service.jar"
afrp_zxf="tar zxf /tmp/${afrp_file} -C ${afrp_path}"


echo "=============打包验证环境tgz包============="
$HOME/trans.py afrp_var cmd  "${afrp_tgz}"

echo "=============获取验证环境tgz包============="
$HOME/trans.py afrp_var get /tmp/${afrp_file}  $HOME/tmp/${afrp_file}

echo "=============传输tgz包至压测环境============="
$HOME/trans.py afrp_lpt put $HOME/tmp/${afrp_file}  /tmp/

echo "=============停止压测环境服务============="
$HOME/trans.py afrp_lpt cmd  "${afrp_stop}"

echo "=============解压压测环境tar包============="
$HOME/trans.py afrp_lpt cmd  "${afrp_zxf}"

echo "=============启动压测环境服务============="
$HOME/trans.py afrp_lpt cmd  "${afrp_start}"
