# -*- coding:utf-8 -*-
import shelve
import pickle
import shelve_3
print('-'*100)
c = shelve.open('shelve_test')
print(c['test2'])
print(c['test'])
print(c['t1'].n)
c.close()

f = open('pickle.txt', 'rb')
a = pickle.load(f)
print(a.n)
b = pickle.load(f)
print(b.n)
c = pickle.load(f)
print(c)
f.close()
