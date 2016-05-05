# -*- coding:utf-8 -*-

class Foo(object):
    pass


obj = Foo()

for i in obj:
    print(i)

# 报错：TypeError: 'Foo' object is not iterable
