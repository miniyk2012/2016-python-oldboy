我的博客地址：http://blog.csdn.net/miniykyk/article/details/50591765
作业：购物小程序
    程序启动后,要求用户输入购物预算,然后打印购物菜单,菜单格式如下:
    0 Macbook Air 7999
    1 Starbucks Coffee 33
    2 Iphone 6 plus 5188
脚本名：
    shopping_cart.py
说明：
    # 本段代码首先要求消费者输入总金额
    # 然后展示商品信息和价格，提升消费者选择商品代号
    # 消费者可以输入代号购买商品，也可以按‘q’退出
    # 当消费者余额不足以购买某商品时，给出余额不足提示信息
    # 消费者退出后，显示已购买商品和消费总额，所剩余额
测试例子：
    Enter your Money:20000
    Welcome to the JD shop!
    0 Macbook Air 7999
    1 Starbucks Coffee 33
    2 Iphone 6 plus 5188
    q buy and quit
    which one do you want?:2
    you buy a Iphone 6 plus
    0 Macbook Air 7999
    1 Starbucks Coffee 33
    2 Iphone 6 plus 5188
    q buy and quit
    which one do you want?:1
    you buy a Starbucks Coffee
    0 Macbook Air 7999
    1 Starbucks Coffee 33
    2 Iphone 6 plus 5188
    q buy and quit
    which one do you want?:1
    you buy a Starbucks Coffee
    0 Macbook Air 7999
    1 Starbucks Coffee 33
    2 Iphone 6 plus 5188
    q buy and quit
    which one do you want?:1
    you buy a Starbucks Coffee
    0 Macbook Air 7999
    1 Starbucks Coffee 33
    2 Iphone 6 plus 5188
    q buy and quit
    which one do you want?:1
    you buy a Starbucks Coffee
    0 Macbook Air 7999
    1 Starbucks Coffee 33
    2 Iphone 6 plus 5188
    q buy and quit
    which one do you want?:2
    you buy a Iphone 6 plus
    0 Macbook Air 7999
    1 Starbucks Coffee 33
    2 Iphone 6 plus 5188
    q buy and quit
    which one do you want?:0
    you buy a Macbook Air
    0 Macbook Air 7999
    1 Starbucks Coffee 33
    2 Iphone 6 plus 5188
    q buy and quit
    which one do you want?:0
    sorry, your balance is insufficient
    0 Macbook Air 7999
    1 Starbucks Coffee 33
    2 Iphone 6 plus 5188
    q buy and quit
    which one do you want?:1
    you buy a Starbucks Coffee
    0 Macbook Air 7999
    1 Starbucks Coffee 33
    2 Iphone 6 plus 5188
    q buy and quit
    which one do you want?:2
    sorry, your balance is insufficient
    0 Macbook Air 7999
    1 Starbucks Coffee 33
    2 Iphone 6 plus 5188
    q buy and quit
    which one do you want?:q
    you buy 1 number of Macbook Air
    you buy 5 number of Starbucks Coffee
    you buy 2 number of Iphone 6 plus
    your total comsume is 18540 yuan
    your left money is 1460 yuan
    Bye bye