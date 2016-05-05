# -*- coding:utf-8 -*-

# don't make your programs have too many layers
# if you do have that many layers, try to use the funciton feature.

break_flag1 = False
break_flag2 = False
break_flag3 = False

while not break_flag1:
    print('the first layer is running...')
    option = input(">>>[b:back, q:quit, c:continue]")
    if option == 'q':
        break_flag1 = True
    elif option == 'b':
        break_flag1 = True
    else:
        break_flag2, break_flag3 = False, False  # continue
    while not (break_flag2 or break_flag1):
        print('the second layer is running...')
        option = input(">>>[b:back, q:quit, c:continue]")
        if option == 'b':
            break_flag2 = True
        elif option == 'q':
            break_flag1 = True
        else:
            break_flag3 = False  # continue
        while not (break_flag1 or break_flag2 or break_flag3):
            print('the third layer is running...')
            option = input(">>>[b:back, q:quit, c:continue]")
            if option == 'b':
                break_flag3 = True
            elif option == 'q':
                break_flag1 = True