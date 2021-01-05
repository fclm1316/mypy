#!/bin/bash
#jjbxsrv        203.3.235.20/203.3.237.58
#jflow          203.3.237.46
#ssp:jjbxssp    203.3.235.19
#tpp:jjbxtpp    203.3.235.19
#
jjbsvr_path="/home/jjbxsrv/apache-tomcat-8.0.48"
jjbxsrv_start="source .bash_profile;cd ${jjbsvr_path}/bin;sh startup.sh"
jjbxsrv_stop="source .bash_profile;cd ${jjbsvr_path}/bin;sh shutdown.sh;pkill -9 java"
jjbxsvr_war="${jjbsvr_path}/webapps/"
jjbxsvr_file="webapp.tgz"
jjbxsvr_tgz="cd ${jjbxsvr_war}/;tar zcf /tmp/${jjbxsvr_file} webapp"
jjbxsvr_zxf="tar zxf /tmp/${jjbxsvr_file} -C ${jjbxsvr_war}"


jflowsrv_path="/home/jflowsrv/apache-tomcat-8.0.48"
jflowsrv_start="source .bash_profile;cd ${jflowsrv_path}/bin;sh startup.sh"
jflowsrv_stop="cd ${jflowsrv_path}/bin;sh shutdown.sh"
jflowsrv_tar="${jflowsrv_path}/webapps/"
jflowsrv_file="jflow-web.tgz"
jflowsrv_zcf="cd ${jflowsrv_tar}/;tar zcf /tmp/${jflowsrv_file} jflow-web"
jflowsrv_zxf="tar zxf /tmp/${jflowsrv_file} -C ${jflowsrv_tar}"

jjbxssp_path="/home/jjbxssp"
jjbxssp_start="source .bash_profile;sh startup.sh"
jjbxssp_stop="sh ${jjbxssp_path}/shutdown.sh"
jjbxssp_file="jjbx-ssp-boot.tgz"
jjbxssp_zcf="ls -t jjbx-ssp-boot-*|head -n1|xargs tar zcf /tmp/${jjbxssp_file}"
jjbxssp_zxf="tar zxf /tmp/${jjbxssp_file} -C ${jjbxssp_path}"


jjbxtpp_path="/home/jjbxtpp"
jjbxtpp_start="source .bash_profile;sh startup.sh"
jjbxtpp_stop="sh ${jjbxtpp_path}/shutdown.sh"
jjbxtpp_file="jjbx-tpp-boot.tgz"
jjbxtpp_zcf="ls -t jjbx-tpp-boot-*|head -n1|xargs tar zcf /tmp/${jjbxtpp_file}"
jjbxtpp_zxf="tar zxf /tmp/${jjbxtpp_file} -C ${jjbxtpp_path}"


echo "=============打包验证环境tgz包============="
$HOME/trans.py jjbxsrv_var cmd  "${jjbxsvr_tgz}"
$HOME/trans.py jflow_var cmd  "${jflowsrv_zcf}"
$HOME/trans.py jjbxssp_var cmd  "${jjbxssp_zcf}"
$HOME/trans.py jjbxtpp_var cmd  "${jjbxtpp_zcf}"

echo "=============获取验证环境tgz包============="
$HOME/trans.py jjbxsrv_var get /tmp/${jjbxsvr_file}  $HOME/tmp/${jjbxsvr_file}
$HOME/trans.py jflow_var get /tmp/${jflowsrv_file} $HOME/tmp/${jflowsrv_file}
$HOME/trans.py jjbxssp_var get  /tmp/${jjbxssp_file} $HOME/tmp/${jjbxssp_file}
$HOME/trans.py jjbxtpp_var get /tmp/${jjbxtpp_file} $HOME/tmp/${jjbxtpp_file}

echo "=============传输tgz包至压测环境============="
$HOME/trans.py jjbxsrv1_lpt put $HOME/tmp/${jjbxsvr_file}  /tmp/
$HOME/trans.py jjbxsrv2_lpt put $HOME/tmp/${jjbxsvr_file}  /tmp/
$HOME/trans.py jflow_lpt put $HOME/tmp/${jflowsrv_file} /tmp/
$HOME/trans.py jjbxssp_lpt put  $HOME/tmp/${jjbxssp_file} /tmp/
$HOME/trans.py jjbxtpp_lpt put $HOME/tmp/${jjbxtpp_file} /tmp/

echo "=============停止压测环境服务============="
$HOME/trans.py jjbxsrv1_lpt cmd  "${jjbxsrv_stop}"
echo "=============kill java============="
$HOME/trans.py jjbxsrv2_lpt cmd  "${jjbxsrv_stop}"
echo "=============kill java============="
$HOME/trans.py jflow_lpt cmd  "${jflowsrv_stop}"
$HOME/trans.py jjbxssp_lpt cmd  "${jjbxssp_stop}"
$HOME/trans.py jjbxtpp_lpt cmd  "${jjbxtpp_stop}"

echo "=============解压压测环境tar包============="
$HOME/trans.py jjbxsrv1_lpt cmd  "${jjbxsvr_zxf}"
$HOME/trans.py jjbxsrv2_lpt cmd  "${jjbxsvr_zxf}"
$HOME/trans.py jflow_lpt cmd  "${jflowsrv_zxf}"
$HOME/trans.py jjbxssp_lpt cmd  "${jjbxssp_zxf}"
$HOME/trans.py jjbxtpp_lpt cmd  "${jjbxtpp_zxf}"

echo "=============启动压测环境服务============="
$HOME/trans.py jjbxsrv1_lpt cmd  "${jjbxsrv_start}"
$HOME/trans.py jjbxsrv2_lpt cmd  "${jjbxsrv_start}"
$HOME/trans.py jflow_lpt cmd  "${jflowsrv_start}"
$HOME/trans.py jjbxssp_lpt cmd  "${jjbxssp_start}"
$HOME/trans.py jjbxtpp_lpt cmd  "${jjbxtpp_start}"
