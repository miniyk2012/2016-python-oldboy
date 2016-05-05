#!/usr/bin/env python
# -*- coding:utf-8 -*-
from multiprocessing import Process, Queue

def f(q):
     q.put([42, None, 'hello'])

if __name__ == '__main__':
    que  = Queue()
    p = Process(target=f, args=(que,))
    p2 = Process(target=f, args=(que,))
    p.start()
    p2.start()
    print('from parent:',que.get())    # prints "[42, None, 'hello']"
    print('from parent2:',que.get())    # prints "[42, None, 'hello']"
    p.join()