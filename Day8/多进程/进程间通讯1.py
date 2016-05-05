# -*- coding:utf-8 -*-  

import queue


a = queue.Queue() # 这个a是当前进程里的Queue,其它进程不能访问,因此多进程需要进行1层封装,让所有进程能共享该Queue
a.put(123)
a.put(321)
a.get()

from multiprocessing import Process, Queue  # 进行1层封装的Queue,让所有进程能共享该Queue

def f(q, arg):
    q.put([arg, None, 'hello'])  # 子进程put,必须通过参数传进来,而不是global,因为内存不共享

if __name__ == '__main__':
    q = Queue()
    p = Process(target=f, args=(q, 5))
    p2 = Process(target=f, args=(q, 6))
    p.start()
    p2.start()
    print(q.get())    # 父进程get,prints "[5, None, 'hello']",但是并不知道顺序哟,因为两个进程执行顺序并不知道.
    print(q.get())    # 父进程get,prints "[6, None, 'hello']"
    p.join()

