# -*- coding:utf-8 -*-

import threading,time

def run(n):
    semaphore.acquire()
    time.sleep(1)
    print("run the thread: %s\n" %n)
    semaphore.release()

if __name__ == '__main__':

    num= 0
    semaphore  = threading.BoundedSemaphore(5) # 最多允许5个线程同时运行,如mysql最大链接数
    for i in range(20):
        t = threading.Thread(target=run,args=(i,))
        t.start()

while threading.active_count() != 1:
    pass  # print threading.active_count()
else:
    print('----all threads done---')
    print(num)
