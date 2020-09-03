# -*- coding: utf-8 -*-
"""
Created on Tue Aug 18 20:23:27 2020

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
    def __init__(self, name, arrows):
        self.name = name
        self.arrows = arrows
     
    def attack(self):
        print(f"{self.name} is attacking with {self.arrows} arrows.")
        
    def check_arrows(self):
        print(f"{self.arrows} arrows left.")

class HybridAttacker(Wizard, Archer):   # notice the order, in that order only it will give preference
    def __init__(self, name, power, arrows):
        Wizard.__init__(self,name,power)
        Archer.__init__(self,name,arrows)

hbot = HybridAttacker("Hydro", 50, 300)
hbot.attack()

print(hbot.name)
print(hbot.power)
print(hbot.arrows)

hbot.check_arrows()

hbot.signed_in()
