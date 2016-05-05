# -*- coding:utf-8 -*-


def login(func):

    def inner(*arg, **kwargs):
        print("passed user verification...")
        return func(*arg, **kwargs)

    return inner

@login
def tv(name, passwd):
    print("Welcome [%s] to TV page, password is [%s]" % (name, passwd))
    return 4

@login
def movie(name):
    print("Welcome [%s] to movie page" % name)


movie('yangkai')

ret = tv('zhoumin', passwd = 'xx')
print(ret)