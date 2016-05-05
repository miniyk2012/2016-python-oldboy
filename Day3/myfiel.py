# -*- coding:utf-8 -*-



f = open('test.log', 'r+', encoding='utf-8')
print(f.tell())
ret = f.read(2)  # 按字符读,python3的改进
print(ret)
print(f.tell())  # 查看当前指针的位置(按字节)
print(f.readable())

# f.seek(5)  # 指定指针位置
# f.truncate()  # 只截取指针前面的字符,保存在文件里
# f.close()




