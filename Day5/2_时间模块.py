import time
import datetime
print(time.time())  # 从1970年开始过了多少秒
print(time.ctime())
print(time.ctime(time.time()-86400))
print(time.gmtime(time.time()))  # 格林威治struct_time格式
print(time.localtime(time.time()))
print(time.localtime())
print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))  # #将struct_time格式转成指定的字符串格式
print(time.strftime("%Y-%m-%d %H-%M-%S"))
print(time.strptime("2016:01:28", "%Y:%m:%d"))  #将字符串格式转换成struct_time格式

# 将字符串的小时,分,秒去掉
str = '2016-02-20 10:54:20'
mytime = time.strptime(str, '%Y-%m-%d %H:%M:%S')
str_2 = time.strftime('%Y-%m-%d', mytime)
print(mytime)
print(str_2)

current_time = datetime.date.today()
datetime.datetime
print(current_time)
print(type(current_time))
print(current_time.timetuple())