# -*- coding:utf-8 -*-

#!/usr/bin/env python
# -*- coding:utf-8 -*-

class Foo(object):

    def __init__(self):
        self.my_dict = {}

    def __getitem__(self, key):
        return self.my_dict.get(key)

    def __setitem__(self, key, value):
       self.my_dict[key] = value

    def __delitem__(self, key):
         self.my_dict[key] = None

obj = Foo()

result = obj['k1']      # 自动触发执行 __getitem__
print(result)
obj['k2'] = 'wupeiqi'   # 自动触发执行 __setitem__
print(obj['k2'])
del obj['k2']           # 自动触发执行 __delitem__
print(obj['k2'])
