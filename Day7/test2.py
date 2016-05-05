# __author__ = '111'
# -*- coding: utf-8 -*-

def func(self):
    print('hello wupeiqi')

Foo = type('Foo',(object,), {'func': func})
#type第一个参数：类名
#type第二个参数：当前类的基类
#type第三个参数：类的成员

x = Foo()
x.func()
print(type(x))
print(type(Foo))