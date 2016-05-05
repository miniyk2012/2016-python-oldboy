# -*- coding:utf-8 -*-  

# 貌似在python2里面才可以用
class Foo(object):

    def __getslice__(self, i, j):
        print('__getslice__',i,j)

    def __setslice__(self, i, j, sequence):
        print('__setslice__',i,j)

    def __delslice__(self, i, j):
        print('__delslice__',i,j)

obj = Foo()

obj[-1:1]   # 自动触发执行 __getslice__
obj[0:1] = [11,22,33,44]   # 自动触发执行 __setslice__
del obj[0:2]   # 自动触发执行 __delslice__