# -*- coding:utf-8 -*-



shoppingGoods = [('Macbook Air', 7999), ('Starbucks Coffee', 33), ('Iphone 6 plus', 5188)]
shoppingList = {}

def show_goods():
    for index, item in enumerate(shoppingGoods):
        print(index, item[0], item[1])
    print('q buy and quit')

def show_shoppingList():
    comsume = 0
    for k,v in shoppingList.items():
        comsume += shoppingGoods[k][1] * v
        print('you buy %d number of %s' %(v, shoppingGoods[k][0]))
    print('your total comsume is %d yuan' %comsume)
    print('your left money is %d yuan' %totalMoney)


totalMoney = int(input("Enter your Money:"))
print("Welcome to the JD shop!")
while True:
    show_goods()
    no = input('which one do you want?:')
    if isinstance(no, str) and no == 'q':
        show_shoppingList()
        break
    no = int(no)
    if totalMoney < shoppingGoods[no][1]:
        print('sorry, your balance is insufficient')
    else:
        totalMoney -= shoppingGoods[no][1]
        shoppingList[no] = shoppingList.get(no, 0) + 1
        print('you buy a %s' %shoppingGoods[no][0])
else:
    show_shoppingList()
print('Bye bye')
