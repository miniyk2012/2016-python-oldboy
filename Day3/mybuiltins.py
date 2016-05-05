# -*- coding:utf-8 -*-

# 内置函数不需要导入模块就可以使用


print(all([1,2,'']))
print(any([1,'',None]))


class Foo:

    def __repr__(self):
        return 'adfafsfas'

f = Foo()
# print(f.__repr__())
print(ascii(f))

print(bytearray('阿扎', encoding='utf-8'))
print(bytes('阿扎', encoding='utf-8'))

func = lambda a: a+1
print(callable(func))  # 是否可被调用,即func()可以被执行
l = []
print(callable(l))  # 如果类里面实现了__call__,那么就为真
print(chr(99))
print(ord('A'))
import random
print(chr(random.randint(30,130)))
# 当你给dir()提供一个模块名字时，它返回在那个模块中定义的名字的列表。当没有为其提供参数时, 它返回当前模块中定义的名字的列表。
print(dir())

print(eval('6*8'))

l = [1,2,3,4]
print(list(map(lambda a:a+100, l)))
def func(x):
    return x*50
print(list(map(func, l)))

def func2(x):
    return x >= 3

print(list(filter(func2, l)))

print(hash('afsdjfa;jfjdfjfjkfsjkjljkjkljjkjklladjklf'))