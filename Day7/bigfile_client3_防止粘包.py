# -*- coding:utf-8 -*-
import socket
ip_port = ('127.0.0.1',9999)

sk = socket.socket()
sk.connect(ip_port)


while True:
    user_input = input("cmd>>:").strip()
    if not user_input:
        continue
    if user_input == 'q':
        break
    sk.send(bytes(user_input,'utf8'))

    # 'CMD_RESULT_SIZE|%s' % len(cmd_result)
    server_ack_msg = sk.recv(100)
    sk.send(b'ok')
    cmd_res_msg = str(server_ack_msg, 'utf8').split('|')
    print(cmd_res_msg)
    if cmd_res_msg[0] == 'CMD_RESULT_SIZE':
        cmd_res_size = int(cmd_res_msg[1])

    res = ''
    received_size = 0
    while received_size < cmd_res_size:  # 收大文件

        server_reply = sk.recv(500)
        received_size += len(server_reply)
        res += str(server_reply, 'utf8')
    else:
        print(res)
        print('-----done-----')
sk.close()


