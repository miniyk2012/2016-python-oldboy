# -*- coding:utf-8 -*-
import threading, time


def doWaiting(t):
    print('start waiting:', time.strftime('%H:%M:%S'))
    time.sleep(t)
    print('stop waiting', time.strftime('%H:%M:%S'))
thread1 = threading.Thread(target=doWaiting, args=[4])
thread2 = threading.Thread(target=doWaiting, args=[5])
thread1.start()
thread2.start()
print(thread1.name)
print(thread2 .name)
time.sleep(1)  #确保线程thread1已经启动
print('start join', time.strftime('%H:%M:%S'))
thread1.join(1)  #将一直堵塞，直到thread1运行结束。
print('end join', time.strftime('%H:%M:%S'))
