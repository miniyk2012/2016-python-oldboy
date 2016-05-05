# -*- coding:utf-8 -*-

# 本段代码不需要使用复杂的循环就可以实现三级菜单的功能呢

tech = ('技术部', (('A技甲',), ('A技乙',), ('A技丙',)))
prod = ('产品部', (('A产甲',), ('A产乙',), ('A产丙',)))
supt = ('支持部', (('A支甲',), ('A支乙',), ('A支丙',)))
makt = ('市场部', (('B市甲',), ('B市乙',)))
sale = ('销售部', (('B销甲',), ('B销乙',), ('B销丙',)))
comA = ('companyA', (tech, prod, supt))
comB = ('companyB', (makt, sale))
root = ('root', (comA, comB))

# state保存一种状态,[0,1,None]表示选择了第一家公司的第二个部门时的状态
# [None, None, None]表示尚未选择公司的状态
# [1,None,None]表示选择了第二家公司时的状态
state = [None, None, None]


def show_items(state):
    # 该函数接收当前的状态, 展示此状态下的信息
    childs = root[1]
    depth = 0
    for index in state:
        if index != None:
            depth += 1
            childs = childs[index][1]
        else:
            # print(childs)
            for num, item in enumerate(childs):
                if state[len(state)-2] != None:
                    print(item[0], end=" ")
                else:
                    print(num, item[0])
            if state[len(state)-2] != None:
                print(end='\n')
            if depth != 0:
                print('b back')
            print('q quit')
            break



while True:
    show_items(state)
    choice = input('please choose!:')
    if choice == 'q':
        break
    index = state.index(None)
    if choice == 'b':
        del(state[index-1]) # 修改state状态
        state.insert(index-1, None)
    else:
        del(state[index])   # 修改state状态
        state.insert(index, int(choice))
