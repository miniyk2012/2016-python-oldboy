# -*- coding:utf-8 -*-



def __init__(self, age):
    self.age = age

def say(self):
    print(self.age)

MyShinyClass = type('MyShinyClass', (), {'name': 'alex', "say": say, "__init__": __init__}) # returns a class object

a = MyShinyClass(40)
a.say()
