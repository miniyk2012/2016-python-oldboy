# -*- coding:utf-8 -*-

import pickle

acc_info = {
    'id': 1234,
    'credit': 10000,
    'balance': 1000,
    'password': '123',
}

f = open('1234.pkl', 'bw')
pickle.dump(acc_info, f)
f.close()