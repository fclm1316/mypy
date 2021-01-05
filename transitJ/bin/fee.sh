#!/bin/bash
#var ip 192.32.242.132
#
fee_stop='sh /home/fee/stopfee.sh'
target_facepl='cd /home/fee/facepl;ls -t face*.jar|head -n1|xargs tar zcf /tmp/facepl.tgz'
target_access='cd /home/fee/access;ls -t access*.jar|head -n1|xargs tar zcf /tmp/access.tgz'
target_nosql='cd /home/fee/nosql;ls -t nosql*.jar|head -n1|xargs tar zcf /tmp/nosql.tgz'


echo "=============打包验证环境tgz包============="
#$HOME/trans.py fee_var cmd  "${target_facepl}"
#$HOME/trans.py fee_var cmd  "${target_access}"
#$HOME/trans.py fee_var cmd  "${target_nosql}"
echo "=============获取验证环境tgz包============="
#$HOME/trans.py fee_var get /tmp/facepl.tgz $HOME/tmp/facepl.tgz
#$HOME/trans.py fee_var get /tmp/access.tgz $HOME/tmp/access.tgz
#$HOME/trans.py fee_var get /tmp/nosql.tgz $HOME/tmp/nosql.tgz

echo "=============传输tgz包至压测环境============="
#$HOME/trans.py fee_lpt put $HOME/tmp/facepl.tgz /tmp/
#$HOME/trans.py fee_lpt put $HOME/tmp/access.tgz /tmp/
#$HOME/trans.py fee_lpt put $HOME/tmp/nosql.tgz /tmp/


echo "=============停止压测环境服务============="
#$HOME/trans.py fee_lpt cmd  "${fee_stop}"

echo "=============解压压测环境tar包============="
#$HOME/trans.py fee_lpt cmd  "tar zxf /tmp/facepl.tgz -C /home/fee/facepl"
#$HOME/trans.py fee_lpt cmd  "tar zxf /tmp/access.tgz -C /home/fee/access"
#$HOME/trans.py fee_lpt cmd  "tar zxf /tmp/nosql.tgz -C /home/fee/nosql"


echo "=============启动压测环境服务============="
$HOME/trans.py fee_lpt cmd "sh /home/fee/facepl/run.sh"
$HOME/trans.py fee_lpt cmd "sh /home/fee/nosql/run.sh"
$HOME/trans.py fee_lpt cmd "sh /home/fee/access/run.sh"
