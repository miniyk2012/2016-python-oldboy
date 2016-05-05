# __author__ = '111'
# -*- coding: utf-8 -*-

class A:
    """
    Test A
    """
    n = 'A'
    def f2(self):
        print('f2 from A')

class B(A):
    n = 'B'
    def f1(self):
        print('from B')
    # def f2(self):
    #     print('f2 from B')

class C(A):
    n = 'C'
    def f2(self):
        print('f2 from C')
class D(B, C):
    """
    Test C
    """
    pass

    def __del__(self):
        print('del')
# c = C()
# c.__del__()
d = D()
d.f2()
print(d.__doc__)
print(d.__module__)
d.__del__()
d.f1()
