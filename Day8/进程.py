from multiprocessing import Process
import threading
import time

def foo(i):
    print('say hi',i)

for i in range(10):
    p = Process(target=foo,args=(i,))
    p.start()
