#!/usr/bin/python
#-*- coding:utf-8 -*-
import time

appName='ALS6'
nameList=["app3svr1,app3Node01","app3svr2,app3Node01",
          "app4svr1,app4Node01","app4svr2,app4Node01",
          "app5svr1,app5Node01","app5svr2,app5Node01",
          "app6svr1,app6Node01","app6svr2,app6Node01"]


def init():
    global appManagerList,nodeList,packagePath
    packagePath='/tmp/' + appName + '.ear'
    appManagerList=[]
    nodeList=[]
    for i in nameList:
        svrName,nodeName = i.split(',')
        appManagerList.append(AdminControl.queryNames('process=' + svrName + ',node=' + nodeName + ',type=ApplicationManager,*'))
        nodeList.append(AdminControl.completeObjectName('type=NodeSync,node='+ nodeName + ',*'))

def save():
    print "export to Application"
    AdminApp.export(appName,packagePath)
    print packagePath

def update():
    init()
    print "Update to Application"
    AdminApp.update(appName,'partialapp',['-operation','update','-contents',packagePath])
    print "Save Application Config"
    AdminConfig.save()

def sync():
    init()
    print "Syncing Application"
    for node in nodeList:
        try:
            AdminControl.invoke(node,'sync')
        except:
            print "Syncing Application error"
            print node

def checkSync():
    init()
    print "Checking Node Syncing Status"
    for node in nodeList:
        count = 0
        while count < 20:
            if AdminControl.invoke(node,'isNodeSynchronized') == 'false':
                print 'Nodes', node, "are Syncing."
                time.sleep(10)
                count = count + 1
            else:
                print 'Nodes', node, "is Synced."
                break

def checkIsReady():
    init()
    count = 0
    while count < 20:
        if AdminApp.isAppReady(appName) == "false":
            print 'Waiting for application to be ready really...' , time.strftime('%Y%m%d-%H%M%S',time.localtime(time.time()))
            time.sleep(10)
            count = count + 1
        else:
            print "Application ready "
            break

def restart():
    init()
    count = 0
    while count < 20:
        if AdminApp.isAppReady(appName) != "false":
            print "Application is ready now"
            print "restart Application "
            for node in appManagerList:
                try:
                    print node, ' stopping........'
                    AdminControl.invoke(node,'stopApplication',appName)
                except:
                    print node
                    print 'stop application error'
                try:
                    print node, ' starting........'
                    AdminControl.invoke(node,'startApplication',appName)
                except :
                    print node
                    print 'start application error'
            break
        else:
            count = count + 1
            print 'Application is not ready ' + time.strftime('%Y%m%d-%H%M%S',time.localtime(time.time()))
            print "time sleep 10 , waitting ..... "
            time.sleep(10)

#AdminControl.completeObjectName('type=Application,node='+ 'app3Node01' +',process=' + 'app3svr1' + ',name='+appName+',*')

typeList = ['save','update','sync','checkSync','checkIsReady','restart']
try:
    type = sys.argv[0]
except:
    print sys.argv[0], typeList
    print 'not in list.exit'
    sys.exit()

if type == 'update':
    update()
elif type == 'sync':
    sync()
elif type == 'checkSync':
    checkSync()
elif type == 'checkIsReady': 
    checkIsReady()
elif type == 'restart': 
    restart()
elif type == 'save': 
    save()
else:
    pass
