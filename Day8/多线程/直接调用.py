# -*- coding:utf-8 -*-
import threading
import time

def sayhi(num): #定义每个线程要运行的函数

    print("running on number:%s" %num)

    time.sleep(3)

if __name__ == '__main__':

    # t1 = threading.Thread(target=sayhi, args=('p1',)) #生成一个线程实例
    # t2 = threading.Thread(target=sayhi, args=('p2',)) #生成另一个线程实例
    #
    # t1.start() #启动线程
    # t2.start() #启动另一个线程
    #
    # print(t1.getName()) #获取线程名
    # print(t2.getName())
    # t1.join()   # 等t1执行完再执行后面的语句
    # t2.join()   # 等t2执行完再执行后面的语句
    # print('---main---') # 一共有三个线程,主线程,t1线程,t2线程.3个线程都是并行的,要想让主线程最后执行,只要前面两个线程都join即可
    t_list = []
    for i in range(100):  # 注意哟一共才过了3秒哟
        t = threading.Thread(target=sayhi, args=[i, ])
        t.start()
        t_list.append(t)
    for t in t_list:
        t.join()
    print('---main---')
