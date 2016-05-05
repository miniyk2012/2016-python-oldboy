# -*- coding:utf-8 -*-
#方法一，Array
from multiprocessing import Process,Array
temp = Array('i', [11,22,33,44])

def Foo(i):
    temp[i] = 100+i
    for item in temp:
        print(i, '----->', item)

for i in range(2):
    p = Process(target=Foo, args=(i,))
    p.start()
