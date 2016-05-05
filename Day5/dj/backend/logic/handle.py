# -*- coding:utf-8 -*-

import os, sys
base_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
print(__file__)
print(base_dir)
sys.path.append(base_dir)

from backend.db.sql_api import select

def home():
    print('welcome to home page')
    data = select("user", 'ddd')
    print('query res:', data)

def movie():
    print('welcome to movie page')

def tv():
    print('welcome to tv page')




