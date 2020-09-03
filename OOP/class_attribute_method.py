# -*- coding: utf-8 -*-
"""
Created on Tue Aug 18 11:16:03 2020

@author: saura
"""
class PlayerCharacter:
    membership = True   # Class object attribute, its an attribute of PlayerCharacter. It is a static attribute
    def __init__(self, name, age):
        if self.membership :    # or we can write: 'if PlayerCharacter.membership :'
            self.name = name  # these are dynamic attribute
            self.age = age
            
    def run(self):
        print(f"run {self.name}")
        # print(f"run {PlayerCharacter.name})   # we cannot do this

player1 = PlayerCharacter("Rohan", 22)
player2 = PlayerCharacter("Mohan", 98)

print(player1.name)
print(player1.membership)   # each of the class instace can assess the class object attribute
print(player1.run())
