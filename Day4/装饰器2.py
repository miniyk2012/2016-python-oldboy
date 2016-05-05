# -*- coding:utf-8 -*-  


def tv(name):
    print("Welcome to TV page")

def login(func):

    def inner(arg):
        print("passed user verification...")
        return func(arg)

    return inner

tv = login(tv)

tv('yangkai')