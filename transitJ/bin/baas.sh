#!/bin/bash
#app 192.3.239.110/111
#
baas_app_path="czbBaaS"
baas_app_path_contract="${baas_app_path}/czbBaaS-contract/app"
baas_app_path_sdk="${baas_app_path}/czbBaaS-sdk/app"
baas_app_path_tomcat="tomcat"
baas_start="source .bash_profile;cd ${baas_app_path_contract};sh startup.sh;cd;cd ${baas_app_path_sdk};sh startup.sh;cd;cd ${baas_app_path_tomcat}/bin;sleep 5;sh startup.sh"
baas_stop="source .bash_profile;cd ${baas_app_path_contract};sh shutdown.sh;cd;cd ${baas_app_path_sdk};sh shutdown.sh;cd;cd ${baas_app_path_tomcat}/bin;sh shutdown.sh"
baas_file="baas_all.tgz"
baas_file_contract="${baas_app_path_contract}/czbBaaS-contract.jar"
baas_file_sdk="${baas_app_path_sdk}/czbBaaS-sdk.jar"
baas_file_tomcat="${baas_app_path_tomcat}/webapps/czbbaas"
baas_tgz="tar zcf /tmp/${baas_file} ${baas_file_contract} ${baas_file_sdk} ${baas_file_tomcat}"
baas_zxf="tar zxf /tmp/${baas_file} -C /home/baasp"


echo "=============打包验证环境tgz包============="
$HOME/trans.py BAAS_var cmd  "${baas_tgz}"

echo "=============获取验证环境tgz包============="
$HOME/trans.py BAAS_var get /tmp/${baas_file}  $HOME/tmp/${baas_file}

echo "=============传输tgz包至压测环境============="
$HOME/trans.py BAAS_lpt put $HOME/tmp/${baas_file}  /tmp/

echo "=============停止压测环境服务============="
$HOME/trans.py BAAS_lpt cmd  "${baas_stop}"

echo "=============解压压测环境tar包============="
$HOME/trans.py BAAS_lpt cmd  "${baas_zxf}"

echo "=============启动压测环境服务============="
$HOME/trans.py BAAS_lpt cmd  "${baas_start}"
