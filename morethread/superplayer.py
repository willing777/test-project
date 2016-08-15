#coding=utf-8
from time import sleep, ctime
import threading
'''
Created on 2016年8月15日

@author: dmrj
'''
from time import ctime
def super_player(file,time):
    for i in range(1):
        print 'Start palying:%s! %s' %(file,ctime())
        sleep(time)
        
list = {'爱情买卖.mp3':3,'阿发达.mp4':4}

threads = []
files = range(len(list))

for file,time in list.items():
    t = threading.Thread(target=super_player,args=(file,time))
    threads.append(t)
    
if __name__ =='__main__':
    for i in files:
        threads[i].start()
    for i in files:
        threads[i].join()
        
print 'end:%s' %ctime()
    

