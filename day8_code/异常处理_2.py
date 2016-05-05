# -*- coding:utf-8 -*-  

while True:
    try:
        num1 = input('num1:')
        num2 = input('num2:')
        a = range(10)
        num1 = int(num1)
        num2 = int(num2)
        result = num1 + num2
        a[11]
    except (IndentationError, SyntaxError) as e:  # 语法错误和缩紧错误是永远抓不到的.貌似ctrl＋c也是抓不到的。
        print(e)
    except (KeyboardInterrupt, EOFError) as e:
        print(e)
    except ValueError as e:
        print('value err:', e)
    except IndexError as e:
        print('index err:', e)
    except Exception as e:  # Exception抓不到KeyboardInterrupt, EOFError, IndentationError, SyntaxError等异常
        print('出现异常，信息如下：')
        print(e)