# -*- coding:utf-8 -*-
class Foo:

    def __init__(self, name):
        self.name = name

    def ord_func(self):
        """ 定义普通方法，至少有一个self参数 """

        # print self.name
        print('普通方法')

    @classmethod
    def class_func(cls):
        """ 定义类方法，至少有一个cls参数 """

        print('类方法')

    @staticmethod
    def static_func():
        """ 定义静态方法 ，无默认参数"""

        print('静态方法')


# 调用普通方法
f = Foo('Tom')
f.ord_func()

# 调用类方法
Foo.class_func()

# 调用静态方法
Foo.static_func()

# ############### 定义 ###############
class Foo:

    def func(self):
        pass

    # 定义属性
    @property
    def prop(self):
        print('wupeiqi')
# ############### 调用 ###############
foo_obj = Foo()

foo_obj.func()
foo_obj.prop   #调用属性

# ############### 定义 ###############
class Pager:

    def __init__(self, current_page):
        # 用户当前请求的页码（第一页、第二页...）
        self.current_page = current_page
        # 每页默认显示10条数据
        self.per_items = 10


    @property
    def start(self):
        val = (self.current_page - 1) * self.per_items
        return val

    @property
    def end(self):
        val = self.current_page * self.per_items
        return val

# ############### 调用 ###############

print(Pager(3).start)
print(Pager(3).end)
p = Pager(5)
print(p.start)  # 就是起始值，即：m
print(p.end)   # 就是结束值，即：n

p2 = Pager(50)
print(p2.start)  # 就是起始值，即：m
print(p2.end)   # 就是结束值，即：n



