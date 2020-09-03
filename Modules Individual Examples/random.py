# -*- coding: utf-8 -*-
"""
Created on Sat Aug 22 13:20:18 2020

@author: saura
"""
import random

print(random)
# print(dir(random))
# print(help(random))

print(random.random())
print(random.randint(1, 100))
print(random.choice('saurabh'))     # We can pass any iterator, like a list for example
print(random.choice([1,2,3,4,5,6,7,8,9]))

my_list = '[1,2,3,4,5]'
random.shuffle(my_list)
print(my_list)
