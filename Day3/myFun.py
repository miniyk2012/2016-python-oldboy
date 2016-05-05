# -*- coding:utf-8 -*-
import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr

def mail(user):
    ret = True
    try:
        msg = MIMEText('你好,这是实验,我试试看的', 'plain', 'utf-8')
        msg['From'] = formataddr(["杨恺",'yk_ecust_2007@163.com'])
        msg['To'] = formataddr(["赵老板", user])
        msg['Subject'] = "实验"

        server = smtplib.SMTP("smtp.163.com", 25)
        server.login("yk_ecust_2007@163.com", "Yk@5078231")
        # for i in range(5):
        server.sendmail('yk_ecust_2007@163.com', [user,], msg.as_string())
        server.quit()
    except Exception as e:
        print(e)
        ret = False
    return ret
count = 0
for i in range(5000):
    ret = mail('630915171@qq.com')
    if ret:
        count += 1
        print('发送成功', count)
    else:
        print('发送失败')




# 动态参数
def show1(*args):  # 收集,将参数转换为元组
    print(args, type(args))

n = [1, 2, 3, 4]
show1(n, 1, 2, 3)

def show2(**kwargs):  # 收集,将参数转换为字典
    print(kwargs, type(kwargs))

show2(n1=78, n2='xx')


def show3(*args, **kwargs):
    print(args, type(args))
    print(kwargs, type(kwargs))

show3(11,22,'xx',33,{1:'z'},x=4,y=8)

l = [11, 22, 33, 44]
d = {'x':1, 'y':2, 'z':3}
show3(l, d)

def show(k1, k2):
    print(k1, k2)

show(*[11,22])  # 分散

show(**{'k1':5, 'k2':6})  # 分散

show3(*l, **d)  # 先分散,再收集

# 应用
print('应用'.center(50, '-'))
s1 = "{0} is {1}"
print(s1.format('alex', '2b'))

l = ['alex', '2b']
print(s1.format(*l))

s2 = "{name} is {actor}"
print(s2.format(name = 'alex', actor = 'sb'))

d = {'name':'alex', 'actor':'sb'}
print(s2.format(**d))

