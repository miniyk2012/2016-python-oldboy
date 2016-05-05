# -*- coding:utf-8 -*-
import gevent

def foo():
    print('Running in foo')
    gevent.sleep(1)
    print('Explicit context switch to foo again')

def bar():
    print('Explicit context to bar')
    gevent.sleep(1)
    print('Implicit context switch back to bar')

def ex():
    print('Explicit context to ex')
    gevent.sleep(1)
    print('Implicit context switch back to ex')


gevent.joinall([    # 产生协程
    gevent.spawn(foo),
    gevent.spawn(bar),
    gevent.spawn(ex),
])