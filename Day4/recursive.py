# -*- coding:utf-8 -*-

def calc(n):
    print(n)
    if n/2 >1:
        calc(n/2)
    print(n)
    return n

# ret = calc(40)
# print(ret)

# 斐波那契数列
def func(arg1,arg2,stop=100):
    if arg1 == 0:
        print(arg1, arg2)
    arg3 = arg1 + arg2
    if arg3 < stop:
        print(arg3)
        func(arg2, arg3, stop)

# func(0,1,100)

# 二分查找
data = list(range(1,600000,3))
# print(data)
# 看50904在不在列表里呢?
def binary_search(data, target):
    if data == []:
        print('can\' find the targe!')
        return
    mid = len(data) // 2
    if data[mid] == target:
        print('find it!')
    elif data[mid] < target:
        print('in the right side of %s' %data[mid])
        binary_search(data[mid+1:], target)
    else:
        print('in the left side of %s' %data[mid])
        binary_search(data[:mid], target)

binary_search(data, 599998)