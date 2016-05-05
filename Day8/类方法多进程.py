# -*- coding:utf-8 -*-

from multiprocessing import Process

class Foo(object):

    def show(self):
        print('show')

obj = Foo()

t = Process(target=obj.show())
t.start()

