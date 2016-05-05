#!/usr/bin/env python
# -*- coding:utf-8 -*-

import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


BIND_HOST = '0.0.0.0'
BIND_PORT = 9999
BUFFER_SIZE = 1024

USER_HOME = os.path.join(BASE_DIR, 'home')

USER_ACCOUNT = {
    'alex': {
        'password': 'alex123',
        'quotation': 1000000,
        'expire': '2016-04-22'
    },
    'rain': {
        'password': 'rain123',
        'quotation': 2000000,
        'expire': '2016-03-22'
    },
    'Thomas Young': {
        'password': '123',
        'quotation': 100000,
        'expire': '2016-04-01'
    }
}