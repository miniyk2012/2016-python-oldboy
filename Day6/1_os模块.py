# -*- coding:utf-8 -*-  

import os
a = os.popen('ls')
print(type(a))
print(a.read())

b = os.system('ls')
print(b)

c = os.stat('1_os模块.py')
print(c)

print(os.path.isfile('.'))
print(os.path.isdir('.'))
print()
print(os.path.isfile('1_os模块.py'))
print(os.path.isdir('1_os模块.py'))