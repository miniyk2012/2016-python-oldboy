# -*- coding:utf-8 -*-
import time


def consumer(name):
    print('%s要吃包子啦' % name)
    while True:
        baozi = yield
        print('包子%s被%s吃了' % (baozi, name))


def producer(name):
    c1 = consumer('yangkai')
    c2 = consumer('yangxiang')
    next(c1)
    c2.__next__()
    print("%s 要做包子啦" % name)
    for dummy_i in range(5):
        time.sleep(1)
        c1.send(dummy_i)  # 异步的含义是指消费者可以去干其他事，直到生产者通知他包子来了。。。
        c2.send(dummy_i)

producer('alex')
