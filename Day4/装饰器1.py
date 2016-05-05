# -*- coding:utf-8 -*-  





def tv(name):
    print("Welcome [%s] to TV page" % name)


def movie(name):
    print("Welcome [%s] to movie page" % name)

def login(func):
    print("passed user verification...")
    return func

# 需求导致了以下想法,不过没卵用:
# tv = login(tv)
# tv('yangkai')


# 下面这段代码相当于会执行home = login(home),这段代码是会执行的,所以没卵用...
@login
def home(name):
    print("Welcome [%s] to home page" % name)




