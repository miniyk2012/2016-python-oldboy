# -*- coding:utf-8 -*-  

import time
import threading

def run(n):

    print('[%s]------running----\n' % n)
    time.sleep(2)
    print('--done--')

def main():
    for i in range(5):
        t = threading.Thread(target=run,args=[i,])
        #time.sleep(1)
        t.start()
        # t.join(1)
        print('starting thread', t.getName())


m = threading.Thread(target=main,args=[])
m.setDaemon(True)  # 将主线程设置为Daemon线程,它退出时,其它子线程会同时退出,不管是否执行完任务
m.start()
m.join(timeout=3)
print(m.is_alive())
print("---main thread done----")