# __author__ = '111'
# -*- coding: utf-8 -*-


class Foo(object):

    def __init__(self, sq):
        self.sq = sq

    def __iter__(self):
        return iter(self.sq)

obj = Foo([11,22,33,44])
print type(obj) # 输出：<class '__main__.Foo'>     表示，obj 对象由Foo类创建
print type(Foo) # 输出：<type 'type'>              表示，Foo类对象由 type 类创建
for i in obj:
    print type(i)
    print i

obj = iter([1,2,3])
while True:
    try:
        val = obj.next()
        print val
    except:
        break