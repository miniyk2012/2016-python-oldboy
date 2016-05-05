# -*- coding:utf-8 -*-
import functools


def wrapper(func):
    @functools.wraps(func)
    def wrapper():
        print('before')
        func()
        print('after')
    return wrapper

@wrapper
def foo():
    print('foo')

foo()
print('foo\'s name is '+foo.__name__)