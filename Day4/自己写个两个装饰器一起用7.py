# -*- coding:utf-8 -*-
import functools
def w1(*args1, **kwargs1):
    def outer(func):
        @functools.wraps(func)
        def wrapper1(*args, **kwargs):
            print('w1')
            print(args1)
            ret = func(*args, **kwargs)
            print(kwargs1)
            return ret
        return wrapper1
    return outer

def w2(*args1, **kwargs1):
    def outer(func):
        @functools.wraps(func)
        def wrapper2(*args, **kwargs):
            print('w2')
            print(args1)
            ret = func(*args, **kwargs)
            print(kwargs1)
            return ret
        return wrapper2
    return outer

@w1('d1', d1=1)
@w2('d2', d2=2)
def main(*args, **kwargs):
    print('main')
    return args, kwargs

ret = main('m', m=1)
print(ret)
print('main\'s name is '+main.__name__)