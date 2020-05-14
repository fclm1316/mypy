if [ -a $HOME/.profile ]
then
    . $HOME/.profile
else
    . $HOME/.bashrc
fi

if [ -a /tmp/tmp.xtx ]
then
> /tmp/tmp/xtx
fi

for dir in `db2 list db directory|grep "Local database directory"|awk -F "="  '{print $2}'`
do
    dbname = `db2 list db directory on $dir|grep "Database name"|awk -F '=' '{print $2}'`
    db2 connect to $dbname
    db2 "select * from (select executable_id,insert_timestamp,section_type,num_executions,stmt_exec_time,
    case when num_execution=0 then stmt_exec_time/(num_executions +1) else stmt_exec_time/num_exectoins end
    as avg_exec_time,substr(stmt_text,1,3000) stmt_text from table(mon_get_pkg_cache_stmt(null,null,null,-2))
    as t where upper(stmt_text) not like '%MON_GET_PKG_CACHE_STMT%' order by avg_exec_time desc)
    where avg_exec_time >1000">>/tmp/tmp/xtx
    db2 disconnect $dbname
done