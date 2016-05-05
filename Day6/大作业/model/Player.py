# -*- coding:utf-8 -*-  


class People(object):

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def grow(self):
        """
        年龄增长一岁
        :return:
        """
        self.age += 1

    def introduction(self):
        print('hi, my name is %s, I\'m %s years old' % (self.name, self.age))



class Girl(People):

    def __init__(self, name):
        super(Girl, self).__init__(name, 0)
        self.intimacy = 10
        self.hate = 0

    def love(self, boy, money):
        self.intimacy += boy.charm + 10 * money


    def tell(self):
        print('my intimacy is %s' % self.intimacy)




class Player(People):


    def __init__(self, name):
        super(Player, self).__init__(name, 0)
        self.money = 0
        self.intelligence = 0
        self.charm = 0
        self.adult_age = 20
        self.action = 10
        self.girl = Girl('Lily')


    def decreaseAction(self, value):
        if value > self.action:
            return False
        else:
            self.action -= value
            return True


    def introduction(self):
        super(Player, self).introduction()
        print('My charm is %s, my money is %s, my intelligence is %s' % (self.charm, self.money, self.intelligence))


    def play(self):
        if self.decreaseAction(5):
            self.charm += 10
            self.money -= 100
            self.intelligence += 1
            return True
        else:
            print('no action left')
            return False


    def study(self):
        self.intelligence += 3
        return True


    def makeMoney(self):
        self.money += self.intelligence
        return True

    def pursue(self, money):
        self.girl.love(self, money)

    def makeLove(self):
        pass


P = Player('Yangkai')
P.play()
P.introduction()
G = P.girl
G.introduction()
G.grow()
G.introduction()