# -*- coding:utf-8 -*-
# 请编写一个decorator，能在函数调用的前后打印出'begin call'和'end call'的日志。
#
# 再思考一下能否写出一个@log的decorator，使它既支持：
#
# @log
# def f():
#     pass
# 又支持：
#
# @log('execute')
# def f():
#     pass
import functools

# def log(para):
#     if callable(para):
#         @functools.wraps(para)
#         def wrapper(*args, **kw):
#             print("start call {0}():".format(para.__name__))
#             f = para(*args, **kw)
#             print("end call {0}():".format(para.__name__))
#             return f
#         return wrapper
#     else:
#         def decorator(func):
#             @functools.wraps(func)
#             def wrapper(*args, **kw):
#                 print("{0} {1} ():".format(para, func.__name__))
#                 return func(*args, **kw)
#             return wrapper
#         return decorator
#
# @log
# def now():
#     print("2016-2-5")
#
# now()

# def log(text):
#     def decorator(func):
#         def warps(*args,**kw):
#             print("begin call")
#             print("%s : %s" % (text,func.__name__))
#             a = func(*args,**kw)
#             print("end call")
#             return a
#         return warps
#     if isinstance(text,str):
#         return decorator
#     func = text
#     text = "excute"
#     return decorator(func)
# @log
# def now():
#     print("haha")
# now()


# 最最漂亮的代码!!每一行都很漂亮
def log(arg):
    def decorator(func=arg):
        text='call' if func==arg else arg
        @functools.wraps(func)
        def wrapper(*args,**kw):
            print('%s %s():' % (text,func.__name__))
            return (func(*args, **kw),print('end %s %s():' % (text, func.__name__)))[0]
        return wrapper
    return decorator() if callable(arg) else decorator

@log('execute')
def now():
    print("2016-2-9")

@log
def hello():
    print('hello world!')


now()
print(now.__name__)
print()
hello()
print(hello.__name__)
