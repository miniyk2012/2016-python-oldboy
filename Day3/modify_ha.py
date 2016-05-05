# -*- coding:utf-8 -*-



"""
这是第三周作业,作业题目见http://www.cnblogs.com/wupeiqi/articles/4950799.html
"""
import json, os


def main():

    prompt = """1、获取ha记录
2、增加ha记录
3、删除ha记录\n"""
    choice = input(prompt)
    f_origin = open("haproxy.cfg", 'r')
    if choice == '1':
        read = input('请输入backend：')
        ret = readRecord(f_origin, "backend "+read.strip())
        print(ret)
    elif choice =='2':
        read = input('请输入要新加的记录：')
        read_dict = json.loads(read)
        addRecord(f_origin, read_dict)
    else:
        read = input('请输入要删除的记录：')
        read_dict = json.loads(read)
        deleteRecord(f_origin, read_dict)
    f_origin.close()

def findBackendPosition(f, backend, position=0):
    """
    函数返回backend第一条纪录所在的起始位置, 如果不存在,返回-1
    :param f:
    :param backend:
    :param position: 搜索的起始位置,默认为0
    :return:
    """
    f.seek(position)
    start_position = position
    while True:
        line = f.readline()
        if line.strip() == backend:
            return f.tell()
        if start_position == f.tell():
            return -1
        start_position = f.tell()

def findEndPosition(f, position):
    """
    函数返回下一个节点的起始位置(或者是空行的起始位置,或者是节点名的起始位置),并返回改节点下有几条纪录
    :param f: 文件对象
    :param position: 某个节点的起始位置
    :return: (endPosition, record_count)
    """
    f.seek(position)
    end_position = position
    record_count = 0
    while True:
        line = f.readline()
        if line.strip() == "":  # 遇到文件末尾或空行
            return end_position, record_count
        if line.startswith(" "):
            record_count += 1
            end_position = f.tell()
        else:
            return end_position, record_count

def readFile(f, start_postion, end_position):
    f.seek(start_postion)
    ret = ""
    while f.tell() < end_position:
        ret += f.readline()
    return ret

def readRecord(f, backend, position=0):
    """
    读取backend,输出到终端
    :param f:
    :param backend:
    :param position:
    :return:
    """
    start_p = findBackendPosition(f, backend)
    if start_p == -1:
        print('不存在这样的backend')
        return
    end_p = findEndPosition(f, start_p)
    ret = readFile(f, start_p, end_p[0])
    return ret

def addRecord(f, read_dict, position=0):
    """
    增加一条纪录
    :param f:
    :param read_dict:
    :param position:
    :return:
    """
    new_f = open('haproxy_new.cfg', 'w')
    website = read_dict['backend']
    start_p = findBackendPosition(f, 'backend '+website)
    record_dict = read_dict['record']
    record_format = "server {server} {server} weight {weight} maxconn {maxconn}".format(**record_dict)
    if start_p != -1:
        end_p = findEndPosition(f, start_p)
        ret = readRecord(f, 'backend '+website)
        ret += "        "+record_format + '\n'
        f.seek(0)
        before = f.read(start_p)
        f.seek(end_p[0])
        remain = f.read()
        ret = before + ret + remain
        new_f.write(ret)
    else:
        ret = "backend " + website + '\n'
        ret += "        "+record_format + '\n'
        f.seek(0)
        ret = f.read() +'\n' + ret
        new_f.write(ret)
    new_f.close()
    os.rename('haproxy_new.cfg', 'haproxy.cfg')

def deleteRecord(f, read_dict):
    """
    删除一条纪录
    :param f:
    :param read_dict:
    :return:
    """
    new_f = open('haproxy_new.cfg', 'w')
    website = read_dict['backend']
    start_p = findBackendPosition(f, 'backend '+website)
    record_dict = read_dict['record']
    record_format = "server {server} {server} weight {weight} maxconn {maxconn}".format(**record_dict)
    end_p = findEndPosition(f, start_p)
    ret = readRecord(f, 'backend '+website)
    recordlist = [item.strip() for item in ret.split('\n')]
    recordlist.remove(record_format)
    middle = "        " + "\n        ".join(recordlist)
    f.seek(0)
    before = f.read(start_p)
    f.seek(end_p[0])
    remain = f.read()
    ret = before + middle + remain
    new_f.write(ret)
    new_f.close()
    os.rename('haproxy_new.cfg', 'haproxy.cfg')
    # 删除空行,以后再重构吧...
    new_f = open('haproxy.cfg', 'r')
    start_p = findBackendPosition(new_f, 'backend '+website)
    end_p = findEndPosition(new_f, start_p)
    if end_p[1] == 0:
        start = findStartPosition(new_f, 'backend '+website)
        new_f.seek(0)
        before = new_f.read(start)
        ret = before+remain
        # print(ret)
        new_f.close()
        new_f = open('haproxy_new.cfg', 'w')
        new_f.write(ret)
        new_f.close()
        os.rename('haproxy_new.cfg', 'haproxy.cfg')

def findStartPosition(f, backend, position=0):
    """
    函数返回backend所在的起始位置, 如果不存在,返回-1
    :param f:
    :param backend:
    :param position: 搜索的起始位置,默认为0
    :return:
    """
    f.seek(position)
    start_position = position
    while True:
        line = f.readline()
        if line.strip() == backend:
            return start_position
        if start_position == f.tell():
            return -1
        start_position = f.tell()

def test():
    f = open("haproxy.cfg", 'r')
    # start_p = findBackendPosition(f, 'defaults')
    # # print(start_p)
    # end_p = findEndPosition(f, start_p)
    # # print(end_p)
    # ret = readFile(f, start_p, end_p[0])
    # print(ret, end='')
    read = '{"backend": "test.oldboy.org","record":{"server": "100.1.7.91","weight": 20,"maxconn": 3000}}'
    # read_dict = json.loads(read)
    # ret = addRecord(f, read_dict)

# {"backend": "test.oldboy.org","record":{"server": "100.1.7.9","weight": 20,"maxconn": 30}}

if __name__ == '__main__':
    main()