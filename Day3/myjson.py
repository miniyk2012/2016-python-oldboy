# -*- coding:utf-8 -*-  

import json
inp_str = "[11,22,33,44]"
inp_list = json.loads(inp_str) # 根据字符串书写格式，将字符串自动转换成 列表类型
print(inp_list)

inp_str = ' {"k1":123, "k2": "wupeiqi"} '  # 正确的输入      切记，内部必须是 双引号 ！！！
# inp_str = " {'k1':123, 'k2': 'wupeiqi'}"   # 错误的输入
inp_dict = json.loads(inp_str)  # 根据字符串书写格式，将字符串自动转换成 字典类型
print(inp_dict)