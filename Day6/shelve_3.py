# -*- coding:utf-8 -*-
import shelve

d = shelve.open('shelve_test') #打开一个文件

class Test(object):
    def __init__(self,n):
        self.n = n


t = Test(123)
t2 = Test(123334)

name = ["alex","rain","test"]
d["test"] = name #持久化列表
d["t1"] = t      #持久化类
d["t2"] = t2

d.close()

a = shelve.open('shelve_test')
print(dir(a))
print(a.get('t1').n)
print(a.get('t2').n)
print(a.get('test'))
a['test2'] = 'yangkai'
a.close()

c = shelve.open('shelve_test')
print(c['test2'])
print(c['test'])
c.close()

import pickle

f = open('pickle.txt', 'bw')
pickle.dump(t, f)
pickle.dump(t2, f)
pickle.dump(name, f)
f.close()

f = open('pickle.txt', 'rb')
a = pickle.load(f)
print(a.n)
b = pickle.load(f)
print(b.n)
c = pickle.load(f)
print(c)
f.close()