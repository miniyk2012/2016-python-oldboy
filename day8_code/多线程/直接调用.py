#!/usr/bin/env python
# -*- coding:utf-8 -*-
import threading
import time

def sayhi(num): #定义每个线程要运行的函数
    print("running on number:%s" %num)
    time.sleep(3)
if __name__ == '__main__':
    '''
    t1 = threading.Thread(target=sayhi,args=(1,)) #生成一个线程实例
    t2 = threading.Thread(target=sayhi,args=(2,)) #生成另一个线程实例
    t1.start() #启动线程
    t2.start() #启动另一个线程
    print(t1.getName()) #获取线程名
    print(t2.getName())
    t1.join() #t2.wait()
    t2.join() #t2.wait()'''
    t_list = []
    for i in range(10):
        t = threading.Thread(target=sayhi,args=[i,])
        t.start()
        t_list.append(t)
    for i in t_list:
        i.join()
    print('---main---')