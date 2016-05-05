#_*_coding:utf-8_*_
__author__ = 'Alex Li'

import main
import json,os
import hashlib
from conf import settings
import time
import socketserver as SocketServer
class MyTCPHandler(SocketServer.BaseRequestHandler):
    #def __init__(self):
    #    self.n  = 1
    #    super(MyTCPHandler,self).__init__()
    #继承BaseRequestHandler基类，然后必须重写handle方法，并且在handle方法里实现与客户端的所有交互
    print('\033[32;1mStarting CrazyFTP server on %s:%s ......\n\033[0m' %(main.settings.BIND_HOST,main.settings.BIND_PORT))
    response_code_list = {
        '200': "Pass authentication!",
        '201': "Wrong username or password",
        #202 this error code will be deprecated in next release 1.9
        '202': "Invalid username or password",
        '300': "Ready to send file to client",
        '301': "Client ready to receive file data ",
        '302': "File doesn't exist",
    }

    def handle(self):

        while  True:
            data = self.request.recv(1024) #接收1024字节数据,收到的数据不一定是1024,根据客户端实际发过来的大小来定
            print("--->data:",data)
            if not data:
                print("\033[31;1mHas lost client\033[0m", self.client_address)
                break     #如果收不到客户端数据了（代表客户端断开了），就断开
            self.instruction_allowcation(data) #客户端发过来的数据统一交给功能分发器处理

    def instruction_allowcation(self,instructions):
        '''功能分发器,负责按照客户端的指令分配给相应的函数处理'''
        #'file_get|{filename,md5,...}'
        instructions = instructions.split("|")
        function_str = instructions[0] # 客户端发过来的指令中,第一个参加都必须在服务器端有相应的方法处理
        if hasattr(self,function_str):
            func = getattr(self,function_str)
            func(instructions)
        else:
            print("\033[31;1mReceived invalid instruction [%s] from client!\033[0m" %(instructions))
    #@login_required
    def file_get(self,user_data):
        print("\033[32;1m---client get file----\033[0m")
        if self.login_user : #make sure user is logined first
            filename_with_path = json.loads(user_data[1])
            file_abs_path = "%s/%s/%s" %(settings.USER_HOME,self.login_user, filename_with_path)
            print file_abs_path
            if os.path.isfile(file_abs_path):
                # send back to client [response_str,code,file_size,file_md5]
                file_size = os.path.getsize(file_abs_path)
                response_msg = "response|300|%s|n/a" %(file_size)
                self.request.send(response_msg)
                client_response = self.request.recv(1024).split("|")  # 为了解决粘包问题,因为大小必须告知.
                print '-->',client_response
                if client_response[1] == "301": #client ready recv file data
                    sent_size = 0
                    f = open(file_abs_path,"rb")
                    file_md5 = hashlib.md5()
                    t_start = time.time()
                    while file_size != sent_size:
                        data = f.read(4096)
                        self.request.send(data)
                        sent_size += len(data)
                        #file_md5.update(data)
                        print("send:",file_size,sent_size)
                    else:
                        md5_str = file_md5.hexdigest()
                        t_cost = time.time() - t_start
                        print "----file transfer time:---",t_cost
                        print("\033[32;1m----successfully sent file to client----\033[0m")
                        #print("\033[32;1m---- file md5 [%s]----\033[0m" %md5_str)


                        f.close()
            else:
                response_msg = "response|302|n/a|n/a"
                self.request.send(response_msg)


    def user_auth(self,data):
        #try:
        auth_info = json.loads(data[1])
        auth_info['username']
        auth_info['password']
        if auth_info['username'] in settings.USER_ACCOUNT:
            if settings.USER_ACCOUNT[auth_info['username']]['password'] == auth_info['password']:
                #pass authentication
                response_code = '200'
                self.login_user = auth_info['username']

            else:
                #wrong username or password
                response_code = '201'
        else:
            response_code = '202'
            #invalid username or password
        #except
        response_str = "response|%s|%s" %(response_code,self.response_code_list[response_code])
        self.request.send(response_str)
        return  response_code
if __name__ == "__main__":
    pass
    '''HOST, PORT = "localhost", 50007

    # 把刚才写的类当作一个参数传给ThreadingTCPServer这个类，下面的代码就创建了一个多线程socket server
    server = SocketServer.ThreadingTCPServer((HOST, PORT), MyTCPHandler)

    # 启动这个server,这个server会一直运行，除非按ctrl-C停止
    server.serve_forever()'''
