#_*_coding:utf-8_*_
__author__ = 'Alex Li'


import os,sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
from modules import main


if __name__ == '__main__':
    Entrypoint = main.ArgvHandler(sys.argv)