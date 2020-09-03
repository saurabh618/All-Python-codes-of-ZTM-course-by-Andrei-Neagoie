# -*- coding: utf-8 -*-
"""
Created on Sun Aug 16 10:58:07 2020

@author: saura
"""
user = {
        "name": "john",
        "sex": "M",
        "age": 20
        }

# print(user["height"]) # this will give us error, as height doesn't exit in the dictionary.

print(user.get("height"))

print(user.get("height", 6)) # if the key value pair doesn't exit, then it will write the default value.
print(user)

# new way to create a dictionary
user2 = dict(name = "saurabh", age = 25)
print(user2)
print(user2["name"])
