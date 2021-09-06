# -*- coding: utf-8 -*

class Person(object):
    def __init__(self, name = None, age = None):
        self.name = name
        self.age = age


P = Person("小明", "24")
P.sex = "male"
