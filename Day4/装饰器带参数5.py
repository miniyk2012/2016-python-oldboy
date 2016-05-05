#!/usr/bin/env python
#coding:utf-8

def Before(request,kargs):
    print('before')

def After(request,kargs):
    print('after')

# 装饰器框架多了一层,为了本身带参数...
def Filter(before_func,after_func):
    # print('haha')
    def outer(main_func):
        # print('yoyo')
        def wrapper(request,kargs):

            before_result = before_func(request,kargs)
            if(before_result != None):
                return before_result;

            main_result = main_func(request,kargs)
            if(main_result != None):
                return main_result;

            after_result = after_func(request,kargs)
            if(after_result != None):
                return after_result;

        return wrapper
    return outer

@Filter(Before, After)
def Index(request,kargs):
    print('index')

Index('abc', 'def')