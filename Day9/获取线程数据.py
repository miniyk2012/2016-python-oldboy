# -*- coding:utf-8 -*-

import time, threading


def run(n):
    time.sleep(3)
    print('from child')
    return n*n

res_list = []
for i in range(10):

    t = threading.Thread(target=run, args=[8, ])
    res_list.append(t)
    t.start()

for t in res_list:
    t.join(timeout=0.1)

print('------')
