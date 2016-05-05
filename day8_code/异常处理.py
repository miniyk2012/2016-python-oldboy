#!/usr/bin/env python
# -*- coding:utf-8 -*-
class AlexException(Exception):
    def __init__(self, msg):
        self.message = msg
    def __str__(self):
        return self.message
a = 1
try:
    assert a == 1
    #raise AlexException('我的异常')
except AlexException as e:
    print(e)
else:
    print("hahaha else ")
finally:
    print("no matter right or wrong, run this anyway !")