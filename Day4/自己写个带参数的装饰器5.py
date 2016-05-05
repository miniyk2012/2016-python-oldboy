# -*- coding:utf-8 -*-

def before():
    print('before')

def after():
    print('after')


def login(before_func, after_func):
    def outer(main_func):
        def wrapper(*args, **kwargs):
            before()
            ret = main_func(*args, **kwargs)
            after()
            return ret
        return wrapper
    return outer


@login(before, after)
def main(*args, **kwargs):
    print('main')
    return args


ret = main(1,2,3,4)
print(ret)

def constrain(*args1, **kwargs1):
    def outer(main_func):
        def wrapper(*args, **kwargs):
            print(args1)
            ret = main_func(*args, **kwargs)
            print(kwargs1)
            return ret
        return wrapper
    return outer

@constrain('a', 'b', x=1, y=2)
def main2(*args, **kwargs):
    print('main')
    return args, kwargs

print()
ret = main2('1', z='2')
print(ret)



