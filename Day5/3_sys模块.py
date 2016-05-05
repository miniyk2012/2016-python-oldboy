# -*- coding:utf-8 -*-  

import time
import sys

for i in range(100):
    sys.stdout.write("#")
    sys.stdout.flush()
    time.sleep(0.5)

print( )
val = sys.stdin.readline()[:-1]
print([val])