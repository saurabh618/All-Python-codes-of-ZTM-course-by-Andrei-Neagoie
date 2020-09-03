# -*- coding: utf-8 -*-
"""
Created on Sun Aug 16 11:10:07 2020

@author: saura
"""
user = {
        "name": "john",
        "sex": "M",
        "age": 20
        }

print("john" in user.items())
print("sex" in user)

print("john" in user.values())
print("sex" in user.keys())

print(user.items())     # returns a list containing a tuple for each key value pair

print(user.clear())
print(user)


user2 = {
        "name": "pepy",
        "sex": "F",
        "age": 45
        }

print(user2.pop("age"))
print(user2)

print(user2.update({"sex": "M"}))
print(user2)

print(user2.update({"size": 32}))
print(user2)

print(user2.popitem())  # it randomly pops an item
print(user2)

print(user2.keys())
print(user2.values())


user3 = {
        'age': 45, 
        'username': "john", 
        'weapons': ["gun"], 
        'is_active': True,
        'clan': "army"
        }

user3['weapons'].append('shield')
user3["weapons"] = user3["weapons"] + ["pistol"]
print(user3)