#encoding:utf-8
#import happybase
#connection = happybase.Connection(host='192.168.100.199',port=9090,protocol='compact',transport='framed')
# connection.open()
#tables = connection.tables()
#print(tables)
# table = connection.table('tbl_user')
# row = table.row('mengday')
# connection.create_table(
#     'mytable',
#     {'cf1': dict(max_versions=10),
#      'cf2': dict(max_versions=1, block_cache_enabled=False),
#      'cf3': dict(),  # use defaults
#     }
# )
# table = connection.table('mytable')
# row = table.row(b'row-key')
# print(row[b'cf1:col1'])


