# -*- coding:utf-8 -*-

# 生产者消费者模型,在串行程序里模拟这个模型哟,用yield语法实现,
# 异步的含义是指消费者可以去干其他事，直到生产者通知他包子来了。。。, 虽然这个程序做不到这点,但有点这个意思了

import time
def consumer(name):
    print("%s 准备吃包子啦!" %name)
    while True:
       baozi = yield

       print("包子[%s]来了,被[%s]吃了!" %(baozi,name))

def producer(name):
    c = consumer('A')
    c2 = consumer('B')

    c.__next__()
    c2.__next__()
    print("老子开始准备做包子啦!")
    for i in range(10):
        time.sleep(1)
        print("做了2个包子!")
        c.send(i)  # 异步的含义是指消费者可以去干其他事，直到生产者通知他包子来了。。。
        c2.send(i)

producer("alex")
