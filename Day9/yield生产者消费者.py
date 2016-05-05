# -*- coding:utf-8 -*-
import time
import queue
def consumer(name):
    print("--->starting eating baozi...")
    while True:
        new_baozi = yield
        print("[%s] is eating baozi %s" % (name,new_baozi))

def producer():

    con.__next__()
    con2.__next__()
    n = 0
    while n < 5:
        n += 1
        time.sleep(1)
        print("\033[32;1m[producer]\033[0m is making baozi %s" %n )
        con.send(n)  # 包子发给yield,yield又赋给new_baozi
        con2.send(n)


if __name__ == '__main__':
    con = consumer("c1")
    con2 = consumer("c2")
    p = producer()
