#!/usr/bin/env python
# -*- coding:utf-8 -*-

import threading, queue, time, random

def consumer(n):
    # while True:
        print("\033[32;1mconsumer [%s]\033[0m get task:  %s" % (n, q.get()))
        q.task_done()  # 告知queue中的东东少了一个

def producer(n):
    count = 1
    while True:
        # count = 1
        time.sleep(random.random())
        print("prodcer [%s] produced a new task : %s" % (n, count))
        q.put(count)
        count += 1
        q.join()  # 当task_done直至没有了, 才会终止阻塞(统一通知所有线程),cpu是休息的哟
        print("all taks has been cosumed by consumers...", n)

q = queue.Queue()
c1 = threading.Thread(target=consumer,args=[1,])
c2 = threading.Thread(target=consumer,args=[2,])
c3 = threading.Thread(target=consumer,args=[3,])
c4 = threading.Thread(target=consumer,args=[4,])
p1 = threading.Thread(target=producer,args=["XiaoYu",])
p2 = threading.Thread(target=producer,args=["LiuYao",])
p3 = threading.Thread(target=producer,args=["yangkai",])
p4 = threading.Thread(target=producer,args=["dongshukai",])
c1.start()
c2.start()
c3.start()
c4.start()
p1.start()
p2.start()
p3.start()
p4.start()
