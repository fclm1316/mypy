#!/usr/bin/python
#-*- coding:utf-8 -*-
import sys,json,os
from fabric import Connection
from concurrent.futures import ThreadPoolExecutor


d_user = ''
d_pwd = ''
json_file = '/home/transitJ/etc/ip.json'
json_user = ''
json_pwd = ''
json_ip = []

def runcmd(user,pwd,ip,cmd):
    c = Connection(host=ip, user=user, connect_kwargs={'password':pwd},connect_timeout=120)
    result = c.run(cmd, warn=True, hide=True)
    #result = c.run(cmd)
    if result.stderr != "":
        print '{} <------\n{}'.format(ip, result.stderr)
    elif result.stdout != "":
        print '{} <------\n{}'.format(ip, result.stdout)

def runfile(put_get,user,pwd,ip,path1,path2):
    c = Connection(host=ip, user=user, connect_kwargs={'password':pwd},connect_timeout=120)
    if put_get == "put":
        try:
            result = c.put(path1,path2)
            print '{} ------> put done'.format(ip, )
        except Exception as e:
            print '{} ------> {} put faild'.format(ip,e )
    else:
        try:
            #getFile = local_file
            #getSavePath = os.path.join(route_path,os.path.basename(local_file))
            result = c.get(path1,path2)
            print '{} ------> get done'.format(ip, )
        except Exception as e:
            print '{} ------> {} get faild'.format(ip,e )
        

def echo_msg():
    print '=============================================='
    print '{} + ip_key + cmd + "cmd"'.format(sys.argv[0])
    print '{} + ip_key + put + local_file + route_path'.format(sys.argv[0])
    print '{} + ip_key + get + route_file + local_file'.format(sys.argv[0])
    print '----------------------------------------------'

def check_input():
    global d_user,d_pwd,json_user,json_pwd,json_ip
    if len(sys.argv) == 4 or len(sys.argv) == 5:
        input_key = sys.argv[1]
        if sys.argv[2] != 'cmd' and sys.argv[2] != 'get' and sys.argv[2] != 'put':
            echo_msg()
            sys.exit()
        with open(json_file,'r') as f:
            json_load = json.load(f)
            default_data = json_load['default']
            d_user = default_data[0].get('user')
            d_pwd = default_data[0].get('password')
            try:
              json_data = json_load[input_key]
              json_user = json_data[0].get('user',d_user)
              json_pwd = json_data[0].get('password',d_pwd)
              json_ip = json_data[0].get('ip_list')
            except:
                print 'input json_key not in ip.json '.format(sys.argv[0])
    else:
        echo_msg()
        sys.exit()
        
def main():
    check_input()
    mode_type = sys.argv[2]
    if mode_type == "cmd":
        exec_cmd = sys.argv[3] 
        with ThreadPoolExecutor(20) as executor:
            all_task = [executor.submit(runcmd,json_user,json_pwd,(ip),exec_cmd) for ip in json_ip]

    elif mode_type == "put":
        put_get = "put"
        try: 
            local_path = sys.argv[3]
            route_path = sys.argv[4]
            with ThreadPoolExecutor() as executor:
                all_task = [executor.submit(runfile,put_get,json_user,json_pwd,(ip),local_path,route_path) for ip in json_ip]
        except:
            echo_msg()

    elif mode_type == "get":
        put_get = "get"
        try: 
            local_file = sys.argv[3]
            route_file = sys.argv[4]
            with ThreadPoolExecutor() as executor:
                all_task = [executor.submit(runfile,put_get,json_user,json_pwd,(ip),local_file,route_file) for ip in json_ip]
        except:
            echo_msg()
    else:
        echo_msg()
        sys.exit()

if __name__ == '__main__':
    main()
