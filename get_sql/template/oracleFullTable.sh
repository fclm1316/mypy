#!/bin/bash
function execSql(){
    sqlcmd = "sqlplus / as sysdba"
    $sqlcmd <<EOF
    $1
    exit
EOF
}

function getFullSQLID(){
    sqlcode_getsqlid = "select sql_id,hash_value,plan_hash_value,object_name from v\$sql_plan v where v.operation='Table ACCESS' and v.options='FULL' and v.object_owner='$DBUSER';"
    execSql "$sqlcode_getsqlid"|awk 'NF==4{print}'|egrep -v "SQL_ID"|uniq
}

function getFullSQL(){
    getFullSQLID | while read line
    do
        sql_id=`echo $line | awk '{print $1}'`
        hash_value = `echo $line | awk '{print $2}'`
        plan_hash_value =`echo $line |awk '{print $3}'`
        object_name=`echo $line |awk '{print $4}'`
        sqlcode = "select SQL_TEXT from v\$sqltext where hash_value='$hash_value' and SQL_ID='$sql_id' order by piece;"
        echo "==============>"
        echo $hash_value
        execSql "$sqlcode" | head -n -5 sed "1,12d" | egrep -v "SQL_TEXT|-" | sed -ne 'H;${x;s/\n//g;p}'
    done
}

DBUSER=CZBOA

getFullSQL