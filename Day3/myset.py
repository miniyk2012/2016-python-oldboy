# -*- coding:utf-8 -*-


# 集合,作用之一是可以再做爬虫的时候保存已访问过的网址
# 访问速度快,天生解决了重复问题
s1 = set()
s1.add('alex')
print(s1)
s1.add('alex')

print(s1)
s2 = set(['alex', 'yangkai', 'alex'])
print(s2)

s3 = s2.difference(s1)
print(s2)
print(s3)

# s4 = s2.difference_update(s1)
# print(s2)
# print(s4)

s2.remove('alex')  # 不存在会抛异常
print(s2)

print(s2.pop())
print(s2)

s2.discard('alex')  # 不存在也不会抛异常
print(s2)

s1 = set([11,22,33])
s2 = set([22, 44])
print(s1.difference(s2))  # 差集
print(s1.symmetric_difference(s2))  # 两个集合的对称差是只属于其中一个集合，而不属于另一个集合的元素组成的集合
print(s2.symmetric_difference(s1))  # 显然与上一行的结果相同