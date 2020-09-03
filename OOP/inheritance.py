# -*- coding: utf-8 -*-
"""
Created on Tue Aug 18 13:23:35 2020

@author: saura
"""
class User():
    def signed_in(self):
        print("User is logged in.")
        
class Wizard(User):
    def __init__(self, name, power):
        self.name = name
        self.power = power
     
    def attack(self):
        print(f"{self.name} is attacking with {self.power} power.")
        
class Archer(User):
    pass

wizard1 = Wizard("John", 50)
archer1 = Archer()

print(wizard1.signed_in())
print(wizard1.attack())

print(archer1.signed_in())
