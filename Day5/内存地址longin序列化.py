# -*- coding:utf-8 -*-

import pickle
import os
print(os.curdir)

f = open('func.txt', 'rb')
data_from_func_file = pickle.loads(f.read())  # 这是因为内存地址只在同一个程序中有效,在另一个程序中就没用了.
print(data_from_func_file)
print(type(data_from_func_file))
f.close()
data_from_func_file['func']()
