#!/usr/bin/env python
# -*- coding:utf-8 -*-
import time
import threading

def run(n):
    print('[%s]------running----\n' % n)
    time.sleep(2)
    print('[%s]--done--' % n)

def main():
    for i in range(10):
        t = threading.Thread(target=run,args=[i,])
        # time.sleep(1)
        t.start()
        #t.join(1)
        print('starting thread', t.getName())


m = threading.Thread(target=main,args=[])
# m.setDaemon(True) #将主线程设置为Daemon线程,它退出时,其它子线程会同时退出,不管是否执行完任务
m.start()
m.join()
print("main thread is alive:",m.is_alive())

print("---main thread done----")
time.sleep(4)