#_*_coding:utf-8_*_
__author__ = 'Alex Li'

import os,sys
import socket
import json


class Client(object):

    def __init__(self,sys_argv):
        self.args = sys_argv
        self.argv_parser()
        self.response_code = {
            '200': "pass user authentication",
            '201': "wrong username or password",
            '202': "invalid username or password",
            '300': "Ready to get file from server",
            '301': "Ready to send to  server",
            '302': "File doesn't exist on ftp server",


        }
        self.handle()
    def help_msg(self):
        msg = '''
        -s ftp_server_addr    :ftp server ip address, mandatory
        -p ftp_server_port    :ftp server port , mandatory
        '''
        print(msg)
    def instruction_msg(self):
        msg = '''
        get ftp_file        : download file from ftp server
        put local  remote   : upload local file to remote
        ls                  : list files on ftp server
        cd  path            : change dir on ftp server

        '''
    def argv_parser(self):
        if len(self.args) < 5:
            self.help_msg()
            sys.exit()
        else:
            mandatory_fields = ["-p","-s"]
            for i  in mandatory_fields:
                if i not in self.args:
                    sys.exit("\033[31;1mLack of argument [%s]\033[0m" % i)
            try:
                self.ftp_host = self.args[self.args.index("-s") + 1]
                self.ftp_port = int(self.args[self.args.index("-p") + 1])
            except (IndexError,ValueError):
                self.help_msg()
                sys.exit()

    def connect(self,host,port):
        try:
            self.sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM) #实例化socket
            self.sock.connect((host,port)) #连接socket服务器
        except socket.error as e:
            sys.exit("\033[31;1m%s\033[0m" %e)
    def auth(self):
        retry_count = 0
        while retry_count < 3:
            username = raw_input("\033[32;1mUsername:\033[0m").strip()
            if len(username) == 0 : continue
            password = raw_input("\033[32;1mPassword:\033[0m").strip()
            if len(password) == 0 : continue
            raw_json = json.dumps({
                'username': username,
                'password': password
            })
            auth_str = "user_auth|%s" %(raw_json)
            self.sock.send(auth_str)
            server_response = self.sock.recv(1024)
            response_code = self.get_response_code(server_response)
            print(self.response_code[response_code])
            if response_code == '200':
                self.login_user = username
                self.cwd = "/"
                return  True
            else:
                retry_count +=1
        else:
            sys.exit("\033[31;1mToo many attempts!\033[0m")
    def get_response_code(self,response):
        response_code = response.split("|")
        code =response_code[1]
        return code
    def parse_instruction(self,user_input):
        user_input_to_list = user_input.split()
        func_str = user_input_to_list[0]
        if hasattr(self,'instruction__'+ func_str):
            return True,user_input_to_list
        else:
            return False,user_input_to_list
    def interactive(self):
        self.logout_flag = False
        while  self.logout_flag is not True:
            user_input = raw_input("[%s]:%s" %(self.login_user,self.cwd)).strip()
            if len(user_input) == 0:continue
            status,user_input_instructions = self.parse_instruction(user_input)
            if status is True:
                func = getattr(self,"instruction__" + user_input_instructions[0])
                func(user_input_instructions)
            else:
                print("\033[31;1mInvalid instruction!\033[0m")

    def instruction__get(self,instructions):
        if len(instructions) == 1:
            print("Input the remote filename which you want to be downloaded!")
            return
        else:
            file_name = instructions[1]
            raw_str = "file_get|%s"% (json.dumps(file_name))
            self.sock.send(raw_str)
            response_str,code,file_size,file_md5 = self.sock.recv(1024).split("|")
            if code == "300": #ready to get file
                self.sock.send("response|301")
                total_file_size = int(file_size)
                received_size = 0
                local_file_obj = open(file_name,"wb")

                while total_file_size != received_size:
                    data = self.sock.recv(4096)
                    received_size += len(data)
                    local_file_obj.write(data)
                    print("recv size:", total_file_size,received_size)
                else:
                    print("\033[32;1m----file download finished-----\033[0m")
                    local_file_obj.close()
            elif code == '302' : #file doesn't exist
                print(self.response_code[code])
    def handle(self):
        self.connect(self.ftp_host,self.ftp_port)
        if self.auth():
            self.interactive()

