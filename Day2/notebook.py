# -*- coding:utf-8 -*-
from collections import Counter, OrderedDict, defaultdict, namedtuple, deque


# Counter是对字典类型的补充，用于追踪值的出现次数。
# ps：具备字典的所有功能 + 自己的功能
print("Counter".center(50, "-"))
c = Counter('abcdeabcdabcaba')
print(c.most_common(3))
print(''.join(c.elements()))
print(''.join(sorted(c.elements())))
print(''.join(sorted(c)))
print(c['b'])
c['b'] -= 3
print(c['b'])
print(''.join(c.elements()))


# orderdDict是对字典类型的补充，他记住了字典元素添加的顺序
# 见博客http://blog.csdn.net/liangguohuan/article/details/7088304，写的已经足够好了
print("orderDict".center(50, "-"))
d1 = {}
d1['a'] = 'A'
d1['b'] = 'B'
d1['c'] = 'C'

d2 = OrderedDict()
d2['a'] = 'A'
d2['b'] = 'B'
d2['c'] = 'C'
print(d1 == d2)


d3 = OrderedDict()
d3['b'] = 'B'
d3['a'] = 'A'
d3['c'] = 'C'
print(d2 == d3)


# Python collections.defaultdict() 与 dict的使用和区别
# http://www.pythontab.com/html/2013/pythonjichu_1023/594.html
print('defaultdict'.center(50, '-'))
values = [11, 22, 33, 44, 55, 66, 77, 88, 99, 90]

my_dict1 = defaultdict(list)

for value in values:
    if value > 66:
        my_dict1['k1'].append(value)
    else:
        my_dict1['k2'].append(value)
print(my_dict1)

my_dict2 = {}

for value in values:
    if value > 66:
        my_dict2.setdefault('k1', []).append(value)
    else:
        my_dict2.setdefault('k2', []).append(value)
print(my_dict2)
print(my_dict1['x'])
print(my_dict1)

s = 'mississippi'
d = defaultdict(int)
for k in s:
    d[k] += 1
print(list(d.items()))


# 根据nametuple可以创建一个包含tuple所有功能以及其他功能的类型。
# 博客地址http://blog.csdn.net/wukaibo1986/article/details/8188906
print("nametuple".center(50, "-"))
Bob = ('bob', 30, 'male')
Jane = ('Jane', 29, 'female')
for people in[Bob, Jane]:
    print("%s is %d years old %s" % people)

Person = namedtuple('Person', 'name age gender')
print('Type of Person:', type(Person))

Bob = Person(name='Bob', age=30, gender='male')
print('Representation:', Bob)

Jane = Person(name='Jane', age=29, gender='female')

print('Field by Name:', Jane.name)

for people in[Bob, Jane]:
    print("%s is %d years old %s" % people)


# 双向队列(deque)
# 一个线程安全的双向队列
print("deque".center(50, "-"))
q = deque('abaacdefgh')
print(q)
q.append('x')
print(q)
q.appendleft(3)
print(q)
print(q.count('a'))
q.extend(['a','b'])
print(q)
q.extendleft(['a', 'b', 'c'])
print(q)
print(q.pop())
print(q.popleft())
print(q)
q.remove(3)
print(q)
q.reverse()
print(q)


# 单向队列,是先进先出（FIFO），使用了queue模块，其中单项和双项队列均有。
# Queue是一个队列的同步实现。队列长度可为无限或者有限。
# 可通过Queue的构造函数的可选参数maxsize来设定队列长度。如果maxsize小于1就表示队列长度无限。
import queue
print("Queue".center(50, "-"))
q = queue.Queue(maxsize = 2)
q.put(1)
q.put(2)
# q.put('a', block=False)  # 如果队列当前已满且block为True(默认)，put()方法就使调用线程暂停,直到空出一个数据单元。如果block为False，put方法将引发Full异常。
# q.put_nowait(3)  #  相当q.put(3, block=False)
print(q.get())
print(q.get())
# print(q.get(block=False))  # 调用队列对象的get()方法从队头删除并返回一个项目。可选参数为block，默认为True。如果队列为空且block为True，get()就使调用线程暂停，直至有项目可用。如果队列为空且block为False，队列将引发Empty异常。
# print(q.get(timeout=2))  # 等待2秒后仍然为空则报异常,常用于多线程





