# -*- coding:utf-8 -*-

import time
import threading

def addNum():
    global num #在每个线程中都获取这个全局变量

    time.sleep(1)
    lock.acquire()
    print('--get num:',num )  # 这把锁和GIL没有关系,GIL是用来锁c的接口滴,是在解释器一层的一把锁
    num  -=1 #对此公共变量进行-1操作
    lock.release()

lock = threading.Lock()
num = 100 #设定一个共享变量
thread_list = []
for i in range(100):
    t = threading.Thread(target=addNum)
    t.start()
    thread_list.append(t)

for t in thread_list: #等待所有线程执行完毕
    t.join()


print('final num:', num )

