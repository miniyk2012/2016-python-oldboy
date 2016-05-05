#!/usr/bin/env python
#coding:utf-8

from multiprocessing import Process
from multiprocessing import Manager
from threading import Thread
import time

import time

li = []

def foo(i):
    time.sleep(1)
    li.append(i)
    print('say hi',li)

for i in range(10):
    p = Process(target=foo, args=(i,))  #
    # p = Thread(target=foo, args=(i,))
    p.start()

print('ending',li)