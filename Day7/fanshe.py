# -*- coding:utf-8 -*-


# 反射的意思是将字符串和变量名对应起来
import sys

class WerServer(object):
    def __init__(self, host, port):
        self.host = host
        self.port = port

    def start(self):
        print("starting")

    def stop(self):
        print("stop")

    def restart(self):
        self.stop()
        self.start()

def test_run(ins, name):
    print("runing..." + name + ' ' + ins.host)

if __name__ == "__main__":
    server = WerServer('localhost', 333)
    # 在命令行中运行:python fanshe.py restart
    # print(sys.argv[1])

    # cmd_dict = {
    #     'start': server.start,
    #     'stop': server.stop,
    #     'stop': server.restart,
    # }
    #
    # if sys.argv[1] in cmd_dict:
    #     cmd_dict[sys.argv[1]]()

    if hasattr(server, sys.argv[1]):
        func = getattr(server, sys.argv[1])  # 获取server.start方法的内存地址
        func()  # server.start()

    # 将test_run加到server上
    setattr(server, 'run', test_run)
    server.run(server, 'yangkai')
    print(server.__dict__)
    print(WerServer.__dict__)

    server2 = WerServer('localhost2', 3332)
    server2.restart()
    print(server2.host)
    delattr(server2, 'host')
    # print(server2.host)
    print(server2.__dict__)

    delattr(WerServer, 'restart')  # 记的restart方法在类Werserber上哟
    # server2
    # server.restart()
