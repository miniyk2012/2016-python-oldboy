# -*- coding:utf-8 -*-
import collections
obj = collections.Counter('akjfadskjkjkjjkj')
print(obj)
print(obj.most_common(4))

for item in obj.elements():
    print(item)

for k, v in obj.items():
    print(k, v)

obj2 = collections.Counter(['11', '22', '33', '22'])
obj2.update(['laex', '11', '11'])
print(obj2)
obj2.subtract(['laex', '11', '11', '11', '11'])
print(obj2)


# Knuth's example for prime factors of 1836:  2**2 * 3**3 * 17**1
prime_factors = collections.Counter({2: 2, 3: 3, 17: 1})
product = 1
for factor in prime_factors.elements():     # loop over factors
    product *= factor
print(product)

# 有序字典
dic = collections.OrderedDict()
# dic = dict()
dic['key1'] = 'v1'
dic['key2'] = 'v2'
dic['key3'] = 'v3'
# dic.move_to_end('key2')
print(dic)
print(dic.popitem())  # 后进先出
print(dic)
print(dic.pop('key2'))
print(dic)
dic.update({'key1':'v111', 'key10': 'v10'})
print(dic)

# 默认字典
dic = collections.defaultdict(list)
dic['k1'].append('alex')
dic['k1'].append(4)
dic['k2'].append('yangkai')
print(dic)

# 创建类
MytupleClass = collections.namedtuple('MytupleClass', ['x', 'y', 'z'])  # nametuple是个方法,创建了一个类MytupleClass
# print(help(MytupleClass))  # 可以查看类MytupleClass的所有方法
obj = MytupleClass(11, 22, 33)
print(obj.x)
print(obj.y)
print(obj.z)
print(obj._asdict())

# 双向队列,内存级别
d = collections.deque()
d.append(1)
d.appendleft(10)
d.appendleft(1)
print(d)
print(d.count(1))
d.extend(['yy', 'uu', 'zz'])
d.extendleft(['yy1', 'uu1', 'zz1'])
print(d)
d.rotate(1)
print(d)

# 单向队列,以后能用于多线程,学网络通信的时候也会用到
import queue
q = queue.Queue()
q.put('123')
q.put('678')
print(q.qsize())
print(q.get())

