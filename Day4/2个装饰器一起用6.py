def w1(func):
    def inner(*args,**kwargs):
        # 验证1
        # 验证2
        # 验证3
        print('w1')
        return func(*args,**kwargs)
    return inner
 
def w2(func):
    def inner(*args,**kwargs):
        # 验证1
        # 验证2
        # 验证3
        print('w2')
        return func(*args,**kwargs)
    return inner
 


@w1
@w2
def f1(arg1,arg2,arg3):
    print('f1')
    return 5

ret = f1(*[1,2,3])
print(ret)