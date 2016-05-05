# -*- coding:utf-8 -*-
class C:

    name = "公有静态字段"

    def func(self):
        print(C.name)

class D(C):

    def show(self):
        print(C.name)


print(C.name)         # 类访问

obj = C()
obj.func()     # 类内部可以访问

obj_son = D()
obj_son.show() # 派生类中可以访问

class C:

    __name = "__公有静态字段"

    def func(self):
        print(C.__name)

class D(C):

    def show(self):
        print(C.__name)


# C.__name       # 类访问            ==> 错误

obj = C()
obj.func()     # 类内部可以访问     ==> 正确

obj_son = D()
# obj_son.show()  # 派生类中可以访问   ==> 错误

class C:

    def __init__(self):
        self.__foo = "私有字段"

    def func(self):
        print(self.__foo)  #　类内部访问

class D(C):

    def show(self):
        print (self.__foo)  # 　派生类中访问

obj = C()

# obj.__foo  # 通过对象访问    ==> 错误
print(obj._C__foo)  # ps：非要访问私有属性的话，可以通过 对象._类__属性名
obj.func()  # 类内部访问        ==> 正确

obj_son = D();
# obj_son.show()  # 派生类中访问  ==> 错误
