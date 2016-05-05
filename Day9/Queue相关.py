# -*- coding:utf-8 -*-

import queue

class Foo(object):
    def __init__(self, n):
        self.n = n


q = queue.Queue(maxsize=3)
# q = queue.LifoQueue(maxsize=3)  # 先入后出的queue


q.put(Foo(1))
q.put(Foo(2))
q.put(Foo(3))

print(q.full())
print('现在队列大小', q.qsize())

# q.get(timeout=3)
data = q.get_nowait()
print(data, type(data))
print(q.full())
print(data.n)
print('现在队列大小', q.qsize())

q = queue.PriorityQueue(maxsize=3)  # 按 (priority_number, data)取, priority_number越小, 优先级越高.
q.put(((1, 'a')))
q.put((2, 'b'))
q.put((0, 'c'))
print(q.get())
