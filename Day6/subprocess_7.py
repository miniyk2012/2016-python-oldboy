# -*- coding:utf-8 -*-
import subprocess

# b = subprocess.run('ifconfig')
# print(b.returncode)
# a = subprocess.run('ls -l', shell=True)
# print(a.returncode)

c = subprocess.Popen('df -h', shell=True, stdout=subprocess.PIPE)
print(c.stdout.read())


x = subprocess.run("sdf", shell=True)
print('exit code', x.returncode)
# subprocess.check_call("sdf", shell=True)