#!/usr/bin/env python
# -*- coding:utf-8 -*-

import threading

class Foo(object):
    def show(self):
        print('show')

def do(event):
    print('start')
    event.wait()
    print('execute')

if __name__ == '__main__':
    event_obj = threading.Event()
    for i in range(10):
        t = threading.Thread(target=do, args=(event_obj,))
        t.start()

    event_obj.clear()
    inp = input('input:')
    if inp == 'true':
        event_obj.set()

