# -*- coding:utf-8 -*-

import threading
import time


class MyThread(threading.Thread):
    def __init__(self, num):
        # threading.Thread.__init__(self)
        super(MyThread, self).__init__()
        self.num = num

    def run(self):  # 定义每个线程要运行的函数,必须叫run

        print("running on number:%s" %self.num)

        time.sleep(3)

if __name__ == '__main__':

    t1 = MyThread(1)
    t2 = MyThread(2)
    t1.start()  # start会调run
    t2.start()
    print('---main---')
