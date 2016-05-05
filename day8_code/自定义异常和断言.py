# -*- coding:utf-8 -*-  
class WupeiqiException(Exception):

    def __init__(self, msg):
        self.message = msg

    def __str__(self):
        return self.message
a = 5
try:
    raise WupeiqiException('我的异常')
    assert type(a) is int
except WupeiqiException as e:
    print(e)
else:
    print('如果没有出现异常,执行else,常在测试用例里面用到')
finally:
    print("no matter right or wrong, run this anyway.")
