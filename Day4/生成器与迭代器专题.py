# -*- coding:utf-8 -*-
# 生成器
print('生成器'.center(50, '-'))
g = (x * x for x in range(10))
print(g)

def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
    return 'done'
g = fib(6)
while True:
    try:
        print(next(g))
    except StopIteration as e:
        print(e)
        break

# 用生成器写杨辉三角
def triangles():
    lst = [1]
    while True:
        yield lst
        lst = list(map(lambda x,y: x+y, lst[:len(lst)-1], lst[1:]))
        lst = [1] + lst + [1]

n = 0
for t in triangles():
    print(t)
    n = n + 1
    if n == 10:
        break

s = (x * x for x in range(5))
print(s)
print(next(s))
print()
for x in s:
    print(x)

def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
    return 'done'

f = fib(10)
print('fib(10):', f)
for x in f:
    print(x)

# call generator manually:
g = fib(5)
while 1:
    try:
        x = next(g)
        print('g:', x)
    except StopIteration as e:
        print('Generator return value:', e.value)
        break

print('迭代器'.center(50, '-'))
