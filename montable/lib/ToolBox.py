#!/usr/bin/python
#coding:utf-8
import os,hashlib,xlwt
from datetime import date,timedelta
from lib.logger import Log
from etc.setting_general import abs_path


log = Log.make_logger()


def md5(text):
    your_md5 = hashlib.md5(text).hexdigest()
    return your_md5


def getDate(num):
    before_day = timedelta(days=num)
    today = date.today()
    numday = today + before_day
    numday = numday.strftime('%Y%m%d')
    return numday

def formatDate(date):
    year = date[0:4]
    mounth = date[4:6]
    day = date[6:8]
    return '{}-{}-{}'.format(year,mounth,day)

def makeDir(path,dbtype):
    time_now = getDate(0)
    dir_path = os.path.join(path,'dbtables',time_now,dbtype)
    if os.path.exists(dir_path):
        log.info('file path exists')
    else:
        os.makedirs(dir_path,mode=0o755)
    return dir_path

def renameFile(host,dbuser):
    file_name = ''.join(host.replace('.','-') + '-' + dbuser +  '.xtx')
    return file_name

def fromatTuple(format_str,upper_lower):
    str_list = []
    for i in format_str.split(','):
        if upper_lower == 'upper':
            str_list.append(i.upper())
        elif upper_lower == 'lower':
            str_list.append(i.lower())
        else:
            str_list.append(i)
    if len(str_list) == 1:
        str_list.append('QWERTYUIOP')
        return tuple(str_list)
    else:
        return tuple(str_list)

def saveDb2Str(rows,save_path_file):
    #print save_path_file,rows
    with open(save_path_file,'w') as f:
        for i in rows:
            f.write('{}\n'.format(i))

def saveMysqlStr(rows,save_path_file):
    with open(save_path_file,'w') as f:
        for i in rows:
            a,b,c,d,e = i
            if e == 'YES':
                e = 'NOT NULL'
            else:
                e = 'ASDFGHJKL'
            if str(d).strip() != 'None':
                d = 'DEFAULT {}'.format(d.strip())
            else:
                d ='ASDFGHJKL'
            mysql_line = '{},{},{},{},{}'.format(a,b,c,d,e)
            f.write('{}\n'.format(mysql_line))

def saveOracleStr(rows,save_path_file):
    with open(save_path_file,'w') as f:
        for i in rows:
            a,b,c,d,e,_f = i
            if _f == 'Y':
                _f = 'NOT NULL'
            else:
                _f = 'ASDFGHJKL'
            if str(e).strip() != 'None':
                e = 'DEFAULT {}'.format(e.strip())
            else:
                e ='ASDFGHJKL'
            oracle_line = '{},{},{}({}),{},{}'.format(a,b,c,d,e,_f)
            #print a,b,str(e).strip(),f
            f.write('{}\n'.format(oracle_line))

def saveXLS(ods_ip,target_ipaddr,filename,own_ods,own_target,same,diff,xls_path):
    save_path = os.path.join(abs_path,xls_path)
    save_file = ''.join(filename + "_" + getDate(0)+ ".xls")
    file_path = os.path.join(save_path,save_file)
    target_name = '{}_{}'.format(target_ipaddr , '源地址_多')
    ods_name = '{}_{}'.format(ods_ip , 'ods地址_多')

    log.info('saving... {} '.format(save_file))

    workbook = xlwt.Workbook(encoding = 'utf-8')
    worksheet_same = workbook.add_sheet('相同表')
    worksheet_target = workbook.add_sheet(target_name)
    worksheet_ods = workbook.add_sheet(ods_name)
    worksheet_diff = workbook.add_sheet('不一样的表')

    
    title = ['表名','字段名','内容']
    title_i = 0 
    for j in title:
        worksheet_target.write(0,title_i,j)
        worksheet_ods.write(0,title_i,j)
        worksheet_same.write(0,title_i,j)
        title_i = title_i + 1



    target_i = 0
    for j in own_target:
        o,p,q =  j.split(',') 
        worksheet_target.write(target_i+1,0,o)
        worksheet_target.write(target_i+1,1,p)
        worksheet_target.write(target_i+1,2,q)
        target_i = target_i + 1


    ods_i = 0
    for j in own_ods:
        o,p,q =  j.split(',') 
        worksheet_ods.write(ods_i+1,0,o)
        worksheet_ods.write(ods_i+1,1,p)
        worksheet_ods.write(ods_i+1,2,q)
        ods_i = ods_i + 1



    same_i = 0
    for j in same:
        o,p,q =  j.split(',') 
        worksheet_same.write(same_i+1,0,o)
        worksheet_same.write(same_i+1,1,p)
        worksheet_same.write(same_i+1,2,q)
        same_i = same_i + 1


    title_diff = ['表名','字段名','差别']
    title_diff = 0 
    for j in title:
        worksheet_diff.write(0,title_diff,j)
        title_diff = title_diff + 1


    diff_i = 0
    for j in diff:
        o,p,q =  j.split(',') 
        worksheet_diff.write(diff_i+1,0,o)
        worksheet_diff.write(diff_i+1,1,p)
        worksheet_diff.write(diff_i+1,2,q)
        diff_i = diff_i + 1


    workbook.save(file_path)
