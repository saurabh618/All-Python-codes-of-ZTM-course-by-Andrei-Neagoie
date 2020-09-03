# -*- coding: utf-8 -*-
"""
Created on Tue Aug 18 11:44:06 2020

@author: saura
"""
class PlayerCharacter:
    membership = True  
    def __init__(self, name, age):
        if self.membership :  
            self.name = name  
            self.age = age
            
    def run(self):
        print(f"run {self.name}")
        
    @classmethod    # we can use this method without instantiating the class
    def add_things(cls, n1, n2):
        return cls('Jojo', n1+n2)
    
    @staticmethod   # same as @classmethod, only thing is we don't pass the class as argument, and hence can't use its attribute
    def add_things2(n1, n2):
        return n1+n2

player1 = PlayerCharacter.add_things(4,5)
print(player1.name)
print(player1.age)
print(player1.membership)

print(PlayerCharacter.add_things2(45, 5))
# print(player2.membership)     # gives error
