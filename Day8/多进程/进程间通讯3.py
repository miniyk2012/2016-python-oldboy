# -*- coding:utf-8 -*-  

from multiprocessing import Process, Manager

def f(d, l, n):
    d[1] = '1'
    d['2'] = 2
    d[0.25] = None
    d[n] = n
    l.append(n)
    print(d)
    print(l)

if __name__ == '__main__':
    with Manager() as manager:
        d = manager.dict()

        l = manager.list(range(5))
        # d = dict()
        # l = list(range(5))
        p_list = []
        for i in range(10):
            p = Process(target=f, args=(d, l, i))
            p.start()
            p_list.append(p)
        for res in p_list:
            res.join()
        print()
        print(d)
        print(l)