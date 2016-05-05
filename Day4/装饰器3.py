# -*- coding:utf-8 -*-  



def login(func):

    def inner(arg):
        print("passed user verification...")
        return func(arg)

    return inner

# 本段代码功能等效于tv = login(tv),执行了这段代码也不会发生什么,只是改变了tv的原有功能
# 是一种与语法糖的功能
@login
def tv(name):
    print("Welcome to TV page")

@login
def movie(name):
    print("Welcome [%s] to movie page" % name)

print('xxs')
tv('yangkai')
movie('zhoumin')