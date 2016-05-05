# -*- coding:utf-8 -*-  


# 默认func只是代指了原函数show
# 原函数的元数据遗漏掉了
import  functools

def outer(func):
    @functools.wraps(func)
    def inner(*args, **kwargs):
        return func(*args, **kwargs)
    return inner


@outer
def show():
    """
    卡卡卡
    :return:
    """
    print('show')

print(show.__doc__)
print(show.__name__)