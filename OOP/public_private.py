# -*- coding: utf-8 -*-
"""
Created on Tue Aug 18 12:23:05 2020

@author: saura
"""
class PlayerCharacter:
    def __init__(self, name, age):
        self.name = name  
        self.age = age
            
    def run(self):
        print(f"run {self.name}")
       
player1 = PlayerCharacter("Rohan", 22)
player2 = PlayerCharacter("Mohan", 20)

player1.name = "!!!!"
player1.run = "BOOOO"

print(player1.name)
print(player1.run)

print(player2.name)
print(player2.run())

'''
Here the user has overwritten the class attributes and methods.
Which we would ideally don't want users to do.
However for other users, like player2, all the orginal attributes and methods functionality is intact.
Hence there is a need for Private attributes and methods, so the user cannot modify them.

But in Python the concept of Private is not there, so we have to work around that. 

So, we can use:
    class PlayerCharacter:
        def __init__(self, name, age):
            self._name = name  
            self._age = age
            
    player1 = PlayerCharacter("Rohan", 22)
    player1.name = "!!!!" 

The user can still modify the attribute, by using 'player1._name = "!!!!"', but we are just letting him know
that '_name' is a private variable, and you should not change it.
            
It's a naming convention to start a private variable with '_' (an underscore), 
so other users will get to know about it.
Similarly we don't ever modify 'dunder' methods, they start and ends with two underscores (for eg. __init__)
        
'''