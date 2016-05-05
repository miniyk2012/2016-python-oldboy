# -*- coding:utf-8 -*-

# # 迭代器
# print('迭代器'.center(50, '-'))
a = iter([1,2,3,4,5])
# print(type(a))
# print(sum(a))

# # 迭代器不能通过下标访问哟
# # a[1]报错
# print(next(a))
# print(next(a))
# # print(next(a))
# # print(next(a))
# # print(a.__next__())
# # print(a.__next__())
# print('loop')
# for x in a:
#     print(x)
#
# f = open('test.txt')
# print(type(f))
# for line in f:
#     print(line, end='')

# 生成器
# print('生成器'.center(50, '-'))
#
#
# def cash_out(amount):
#     while amount > 0:
#         amount -= 100
#         yield 100
#         print("擦，又来取钱了。。。败家子！")
#
#
# print(type(cash_out(600)))
# atm = cash_out(600)
# print(type(atm))
# print(next(atm))
# print(next(atm))
# print("叫个大保健")
# print(atm.__next__())
# print(atm.__next__())
# print(atm.__next__())
#
# for x in cash_out(300):
#     print(type(x))
#
#
# def G():
#     print(1)
#     yield 1
#     print(2)
#     yield 2
#     print(3)
#     yield 3
#
#
# print(type(G))
# print(type(G()))
# for x in G():
#     pass
#
#
# def nrange(num):
#     temp = -1
#     while True:
#         temp = temp + 1
#         if temp >= num:
#             return
#         else:
#             yield temp
#
#
# for i in nrange(10):
#     print(i)
#
# from collections import Iterable
# print(isinstance(a, Iterable))


from collections import Iterable, Iterator

def g():
    yield 1
    yield 2
    yield 3

print('Iterable? [1, 2, 3]:', isinstance([1, 2, 3], Iterable))
print('Iterable? \'abc\':', isinstance('abc', Iterable))
print('Iterable? 123:', isinstance(123, Iterable))
print('Iterable? g():', isinstance(g(), Iterable))

print('Iterator? [1, 2, 3]:', isinstance([1, 2, 3], Iterator))
print('Iterator? iter([1, 2, 3]):', isinstance(iter([1, 2, 3]), Iterator))
print('Iterator? \'abc\':', isinstance('abc', Iterator))
print('Iterator? 123:', isinstance(123, Iterator))
print('Iterator? g():', isinstance(g(), Iterator))

# iter list:
print('for x in [1, 2, 3, 4, 5]:')
for x in [1, 2, 3, 4, 5]:
    print(x)

print('for x in iter([1, 2, 3, 4, 5]):')
for x in iter([1, 2, 3, 4, 5]):
    print(x)

print('next():')
it = iter([1, 2, 3, 4, 5])
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))

d = {'a': 1, 'b': 2, 'c': 3}

# iter each key:
print('iter key:', d)
for k in d.keys():
    print('key:', k)

# iter each value:
print('iter value:', d)
for v in d.values():
    print('value:', v)

# iter both key and value:
print('iter item:', d)
for k, v in d.items():
    print('item:', k, v)

# iter list with index:
print('iter enumerate([\'A\', \'B\', \'C\']')
for i, value in enumerate(['A', 'B', 'C']):
    print(i, value)

# iter complex list:
print('iter [(1, 1), (2, 4), (3, 9)]:')
for x, y in [(1, 1), (2, 4), (3, 9)]:
    print(x, y)