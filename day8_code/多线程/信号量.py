#!/usr/bin/env python
# -*- coding:utf-8 -*-
import threading,time
def run(n):
    semaphore.acquire()
    time.sleep(1)
    print("run the thread: %s\n" %n)
    semaphore.release()
if __name__ == '__main__':
    num= 0
    semaphore  = threading.BoundedSemaphore(3) #最多允许5个线程同时运行
    for i in range(20):
        t = threading.Thread(target=run,args=(i,))
        t.start()
while threading.active_count() != 1:
    pass #print threading.active_count()
else:
    print('----all threads done---')
    print(num)