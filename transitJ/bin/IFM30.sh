#!/bin/bash
#192.3.237.187/188
#
wsadmin_path="/opt/IBM/WebSphere/AppServer/profiles/app6/bin/wsadmin.sh"
Name="${wsadmin_path} -lang jython -f /tmp/was_export.py ALS6 /tmp/ALS6_lpt.ear"
appName="hostchannel_war ifmbatch_war ifmcounter_war ifmmanage_war ifmonline_war wbschannel_war"

export_var=''




echo "=============打包验证环境tgz包============="
for i in $appName
do
    echo "${wsadmin_path} -lang jython -f /tmp/was_export.py $i /tmp/${i}_lpt.ear"
done


echo "=============获取验证环境tgz包============="

echo "=============传输tgz包至压测环境============="

echo "=============停止压测环境服务============="

echo "=============解压压测环境tar包============="

echo "=============启动压测环境服务============="
