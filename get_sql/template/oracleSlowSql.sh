#!/bin/bash
source $HOME/.bash_profile

function execSql() {
    sqlcmd = "sqlpuls / as sysdba"
        $sqlcmd <<EOF
        set pagesize 9999;
        set linesize 9999;
        set long 9999;
        $1
        exit;
EOF
}

function getFullSQLID() {
    sqlcode_getsqlid = "select * from (select sa.hash_value,round(sa.elapsed_time / 1000000,4) as Total_time,round(sa.slapsed_time /1000000 / sa.executions,4) as avg_time, sa.executions,sa.rows_processed,u.username from v\sqlarea sa,all_users u where sa.executions > 10 and u.username='$DBUSER' order by Avg_time desc) where rownum <=100;"
    execSql "$sqlcode_getsqlid"|grep $DBUSER
}

function getFullSQL(){
    getFullSQLID |while read line
    do
    hash_value=`echo $line | awk "{print $1}"`
    Total_time=`echo $line | awk "{print $2}"`
    Avg_time=`echo $line | awk "{print $3}"`
    executions=`echo $line | awk "{print $4}"`
    rows=`echo $line | awk "{print $5}"`
    sqlcode="select sql_text from v\sqltext where hash_value='$hash_value' order by piece;"
    echo "------>,$hash_value,$Total_time,$Avg_time,$executions,$rows"
    execSql "$sqlcode"|egrep -v "rows selected|SQL\*Pluss|ALL right|Connected to|Oracle Database 11g|Real Application|SQL>|SQL_TEXT|-------"| sed -ne 'H;${x;s/\n//g;p}'
    echo "========>"
    done
}

DBUSER=$1
getFullSQL