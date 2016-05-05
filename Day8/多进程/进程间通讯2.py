# -*- coding:utf-8 -*-  

from multiprocessing import Process, Pipe

def f(conn, args):
    conn.send([args, None, 'hello'])
    conn.close()

if __name__ == '__main__':
    parent_conn, child_conn = Pipe()
    p = Process(target=f, args=(child_conn, 42))
    p.start()
    print(parent_conn.recv())   # prints "[42, None, 'hello']"
    p.join()