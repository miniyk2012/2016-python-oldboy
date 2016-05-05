#_*_coding:utf-8_*_
__author__ = 'Alex Li'
import os,sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
from modules import SocketClient


if __name__ == '__main__':
    sock_cli = SocketClient.Client(sys.argv)