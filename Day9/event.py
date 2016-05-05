# -*- coding:utf-8 -*-

import threading


event = threading.Event()

event.set()
event.wait()
event.clear()
event.is_set()