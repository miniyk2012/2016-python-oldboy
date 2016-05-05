# -*- coding:utf-8 -*-

import os
# 替换原文件中的某个字段,方法是新写一个文件
f = open('old.txt', 'r')
f_new = open('new.txt', 'w')
for line in f:
    if line.startswith('alex'):
        new_line = line.replace('alex', "ALEX LI...")
        f_new.write(new_line)
    else:
        f_new.write(line)
f.close()
f_new.close()
os.rename('new.txt', 'old.txt')