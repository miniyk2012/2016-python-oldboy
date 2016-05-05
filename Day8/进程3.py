# -*- coding:utf-8 -*-
#方法二：manage.dict()共享数据
from multiprocessing import Process,Manager

manage = Manager()
dic = manage.dict()

def Foo(i):
    import time
    time.sleep(1)
    dic[i] = 100+i
    print(dic.values())

p_list = []
for i in range(100):
    p = Process(target=Foo, args=(i,))
    p_list.append(p)
    p.start()

for p in p_list:
    p.join()

