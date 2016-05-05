# -*- coding:utf-8 -*-
import copy
# 浅拷贝
# copy.copy()
# # 深拷贝
# copy.deepcopy()
# 赋值
# =

# 字符串和数字，数字池和字符池,可以认为是内存中的最小单元
print('字符串和数字，数字池和字符池'.center(50, '-'))
a1 = 123123
a2 = 123123
print(id(a1))
print(id(a2))
a2 = a1
print(id(a1))
print(id(a2))


a3 = copy.copy(a1)
print(id(a1))
print(id(a3))

a4 = copy.deepcopy(a1)
print(id(a1))
print(id(a4))

# 其他,元组\列表\字典等
print('其他,元组\列表\字典等'.center(50, '-'))
n1 = {"k1": "wu", "k2": 123, "k3": ["alex", 456]}
n2 = n1
print(id(n1))
print(id(n2))

print('浅拷贝'.center(30, '-'))
n3 = copy.copy(n1)
print(id(n1))
print(id(n3))
print(id(n1['k3']))
print(id(n3['k3']))

print('深拷贝'.center(30, '-'))
n4 = copy.deepcopy(n1)
print(id(n1))
print(id(n4))
print(id(n1['k3']))
print(id(n4['k3']))
print(id(n1['k1']))
print(id(n4['k1']))

# 应用
print('应用'.center(50, '-'))
dic = {
    'cpu': [80, ],
    'mem': [80, ],
    'disk': [80, ],
}

# new_dic = copy.copy(dic)
# new_dic['cpu'][0] = 50
# print('dic', dic)
# print('new_dic', new_dic)

new_dic = copy.deepcopy(dic)
new_dic['cpu'][0] = 50
print('dic', dic)
print('new_dic', new_dic)


