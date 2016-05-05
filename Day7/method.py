# __author__ = '111'
# -*- coding: utf-8 -*-

class Animal(object):

    hobby = 'meat'

    def __init__(self, name):
        self.name = name
        self.__num = None

    @classmethod
    def talk(cls):
        print('hobby is ', cls.hobby)

    @property
    def habit(self):
        print('%s habit is xxoo' %self.name)

    @staticmethod  # 静态方法不能访问类变量和实例变量，除非Animal.hobby
    def think(x, y):
        print('hobby is %s' % (x+y))

    @property
    def total_players(self):
        return self.__num

    @total_players.setter
    def total_players(self, num):
        self.__num = num

    @total_players.deleter
    def total_players(self):
        self.__num = None

d = Animal('Sanjiang')
d.habit
d.talk()
d.think(5, 6)
print(d.total_players)
d.total_players = 5
print(d.total_players)
del d.total_players
print(d.total_players)
d.__num = 9
d.total_players = 5
print('out', d.__num)
print(d.total_players)
print('out', d._Animal__num)  # 特例访问私有变量