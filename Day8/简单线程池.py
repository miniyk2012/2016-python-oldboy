#!/usr/bin/env python
# -*- coding:utf-8 -*-
import queue
import threading


class ThreadPool(object):

    def __init__(self, max_num=20):
        self.queue = queue.Queue(max_num)
        for i in range(max_num):
            # 在队列里填充线程类
            self.queue.put(threading.Thread)

    def get_thread(self):
        # 去队列取线程
        # queue特性:有就拿,没有就等,直到有人往里面放元素
        return self.queue.get()

    def add_thread(self):
        self.queue.put(threading.Thread)

pool = ThreadPool(10)

def func(arg, p):
    print(arg)
    import time
    time.sleep(2)
    # 执行完后,归还线程到线程池
    p.add_thread()


for i in range(30):
    # 去线程池拿一个线程,如果没有,就等,直到有人归还线程到线程池
    thread = pool.get_thread()
    # thread = threading.Thread
    t = thread(target=func, args=(i, pool))
    t.start()