# -*- coding:utf-8 -*-
#!/usr/bin/env python

import sys


def s1():
    print('s1')


def s2():
    print('s2')


this_module = sys.modules[__name__]

hasattr(this_module, 's1')
getattr(this_module, 's2')
