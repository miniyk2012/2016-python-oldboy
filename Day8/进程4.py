#!/usr/bin/env python
# -*- coding:utf-8 -*-

from multiprocessing import Process, Array, RLock

def Foo(lock,temp,i):
    """
    将第0个数加i
    """
    import time
    time.sleep(1)
    lock.acquire()
    temp[0] += i
    for item in temp:
        print(i,'----->',item)
    lock.release()

lock = RLock()
temp = Array('i', [11, 22, 33, 44])

for i in range(100):
    p = Process(target=Foo,args=(lock,temp,i,))
    p.start()