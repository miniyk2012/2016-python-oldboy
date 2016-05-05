# -*- coding:utf-8 -*-

from gevent import monkey; monkey.patch_all()
import gevent
from urllib.request import urlopen

def f(url):
    print('GET: %s' % url)
    resp = urlopen(url)
    data = resp.read()
    print('%d bytes received from %s.' % (len(data), url))


# 协程切换的好处是三个协程可以并行的读
gevent.joinall([
        gevent.spawn(f, 'http://www.baidu.com'),
        gevent.spawn(f, 'https://www.taobao.com/'),
        gevent.spawn(f, 'https://www.mi.com/'),
        gevent.spawn(f, 'https://www.jd.com/'),
        gevent.spawn(print, 'haha'),
])

