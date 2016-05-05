# -*- coding:utf-8 -*-

from multiprocessing import Process
import time
def f(name):
    time.sleep(2)
    print('hello', name)

if __name__ == '__main__':
    p = Process(target=f, args=('bob',))
    p2 = Process(target=f, args=('bob',))
    p.start()
    p2.start()
    p.join()
    p2.join()
