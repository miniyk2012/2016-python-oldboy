# -*- coding:utf-8 -*-

import sys
import os
base_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(base_dir)
print(sys.path)
from config import settings


def db_auth(configs):
    if configs.DATABASE['user'] == 'yangkai' and configs.DATABASE['password'] == '123':
        print('passed')
        return True
    else:
        print('error')


def select(table, column):

    if db_auth(settings):
        if table == 'user':
            user_info = {
                "001": ['alex', 23, 'engineer'],
                "002": ['longGe', 25, 'chef'],
                "003": ['alex', 24, 'baoan'],
            }

            return user_info
