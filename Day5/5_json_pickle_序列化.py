# -*- coding:utf-8 -*-

# 序列化是为了把硬盘信息转化成内存信息,内存里是个字典,而硬盘里是个字符串, 需要有转换机制

# 字典-->字符串:序列化; 字符串-->字典:反序列化

info = {
    "alex": '123',
    "jack": '444',
}

import pickle

f = open('user_acc_pickle.txt', 'wb')
f.write(pickle.dumps(info))
f.close()

f = open('user_acc_pickle.txt', 'rb')
data_from_file = pickle.loads((f.read()))
f.close()
print(data_from_file)
print(type(data_from_file))


import json


info = {
    "alex": '123',
    "jack": '444',
}
f = open('user_acc_json.txt', 'w')
f.write(json.dumps(info))
f.close()
f = open('user_acc_json.txt', 'r')
data_from_file = json.loads((f.read()))
f.close()
print(data_from_file)
print(type(data_from_file))

def login():
    print('yangkai')


fun_info = {
    'alex': 123,
    'func': login,
}

data = pickle.dumps(fun_info)
print(type(data))

f = open('func.txt', 'wb')
f.write(data)
f.close()

f = open('func.txt', 'rb')
data_from_func_file = pickle.loads(f.read())
print(data_from_func_file)
print(type(data_from_func_file))
f.close()
data_from_func_file['func']()

print()
data = pickle.dumps(info)
print(type(data))

with open('pickle.txt', 'wb') as f2:
    pickle.dump(info, f2)

with open('pickle.txt', 'rb') as f2:
    data = pickle.load(f2)
    print(type(data))
    print(data)

