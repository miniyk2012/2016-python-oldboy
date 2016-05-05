# -*- coding:utf-8 -*-

class Province:

    """
    哈哈
    """
    country = 'China'

    def __init__(self, name, count):
        self.name = name
        self.count = count

    def func(self, *args, **kwargs):
        print('func')

# 获取类的成员，即：静态字段、方法、
print(Province.__dict__)
print(Province.__doc__)
# 输出：{'country': 'China', '__module__': '__main__', 'func': <function func at 0x10be30f50>, '__init__': <function __init__ at 0x10be30ed8>, '__doc__': '\n    哈哈\n    '}

obj1 = Province('HeBei',10000)
print(obj1.__class__)
print(obj1.__dict__)
# 获取 对象obj1 的成员
# 输出：{'count': 10000, 'name': 'HeBei'}

obj2 = Province('HeNan', 3888)
print(obj2.__dict__)
# 获取 对象obj1 的成员
# 输出：{'count': 3888, 'name': 'HeNan'}
