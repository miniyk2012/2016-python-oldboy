# -*- coding:utf-8 -*-

log_data = []

def loadData():
    log_data.clear()
    with open("user.log") as f:
        for line in f:
            log_message = []
            for item in line.strip().split(','):
                log_message.append(item)
            log_data.append(log_message)


# 本段代码假设用户名输入是正确的,密码可能不正确
# 本段代码假设连续多次输入的姓名是相同的,直到登录成功或者被锁住为止
log_count = 0
while True:
    name = input("input your name")
    passwd = input("input your password")
    log_count += 1
    loadData()
    for log_message in log_data:
        if name == log_message[0]:
            if log_message[2] == 'lock':
                log_count = 0   # 该用户被锁定,登录次数重置为零
                print("sorry, you're locked")
            elif passwd == log_message[1]:
                log_count = 0   # 用户登录成功,登录次数重置为零
                print("Welcome, %s" %name)
            else:
                print("your passwd is incorrect")
            break
    if log_count >= 3:
        log_count = 0   # 用户被锁定,登录次数重置为零
        print("sorry, you input wrong password 3 times, you'll be locked!")
        with open("user.log", 'w') as f:
            for log_message in log_data:
                if name == log_message[0]:
                    log_message[2] = 'lock'
                line = ','.join(log_message) + '\n'
                f.write(line)


