# -*- coding:utf-8 -*-

import os, pickle

from config import settings

def auth(account, password):
    account_db = '%s/%s.pkl' % (settings.AccountDBPath, account)
    # print(account_db)
    if os.path.isfile(account_db):
        with open(account_db, 'rb') as f:
            acc_data = pickle.load(f)
            if password == acc_data['password']:
                return acc_data
            else:
                print("wrong password!")
    else:
        print('wrong account id or password')



def ATM():
    # user authentication
    print(settings.AccountDBPath)
    account = input('account').strip()
    passowrd = input('password').strip()
    user = auth(account, passowrd)
    if user:
        print('welcom login...')
