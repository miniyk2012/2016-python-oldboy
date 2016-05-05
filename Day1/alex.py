

# -*- coding:utf-8 -*-

region = {
    '北京': {
        '海淀': {
            '沙河': {'老男孩': {}},
            '天通苑': {'地铁': {}}
        },
        '朝阳': {
            '望京': {'棒子街': {}},
            '大跃城': {'美女': {}}
        },
    },
    '上海': {},
    '广州': {}
}


while True:
    for index, item in enumerate(region):
        print(index, item)  # bj .sh gz
    user_choice = input(">>>:")
    while True:
        for item2 in region[user_choice]:
            print(item2)
        user_choice2 = input(">>>:")
        while True:
            for item3 in region[user_choice][user_choice2]:
                print(item3)
            user_choice3 = input(">>>:")
            while True:
                for item4 in region[user_choice][user_choice2][user_choice3]:
                    print(item4)
                choice = input("bottom")
                break