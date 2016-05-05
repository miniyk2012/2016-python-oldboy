# -*- coding:utf-8 -*-


class Role(object):
    ac = None  # 类属性,防弹衣
    members = 0

    def __init__(self, name, role, weapon, life_value):
        self.name = name  # 成员属性
        self.role = role
        self.weapon = weapon
        self.life_value = life_value
        Role.members += 1

    def buy_weapon(self, weapon):
        print("%s is buying [%s]" %(self.name, weapon))
        self.weapon = weapon
        print('ac:', self.ac)

print('Role.ac: ', Role.ac)
# Role的实例
# 把一个抽象的类变成一个具体的对象的过程,叫实例化
p1 = Role('alex', 'Police', 'B15', 90)
p2 = Role('ChunYun', 'Police', 'B11', 100)
t1 = Role('ChunYun', 'Terrorist', 'B11', 100)
t2 = Role('ChunYun', 'Terrorist', 'B11', 100)
p1.buy_weapon('AK47')  # Role.buy_weapon(p1, 'AK47')
p2.buy_weapon('B51')
print('%s\'s weapon is %s' % (p1.name, p1.weapon))
print('%s\'s weapon is %s' % (p2.name, p2.weapon))

print('P1\'ac:', p1.ac)
print('P2\'ac:', p2.ac)

p1.ac = 'China Brand'
p2.ac = 'US Brand'
Role.ac = "Japan Brand"
print('p1', p1.ac)
print('p2', p2.ac)
print('t1', t1.ac)
print('t2', t2.ac)
print(Role.ac)

# print(Role.weapon)
Role.weapon = 'XD'
print('p1', p1.weapon)
print('p2', p2.weapon)
print('t1', t1.weapon)
print('t2', t2.weapon)
print('Role', Role.weapon)

print(p1.members)
print(Role.members)
