# -*- coding:utf-8 -*-

class Foo:

    def __init__(self):
        pass

    def __call__(self, *args, **kwargs):

        print('__call__')


obj = Foo() # 执行 __init__
obj()       # 执行 __call__