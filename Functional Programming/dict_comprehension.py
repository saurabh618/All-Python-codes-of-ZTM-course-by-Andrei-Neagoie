# -*- coding: utf-8 -*-
"""
Created on Wed Aug 19 14:16:38 2020

@author: saura
"""
my_dict = {num:num**2 for num in range(1,11)}
print(my_dict)

random_dict = {
    'a': 1,
    'b': 2,
    'c': 3,
    'd': 4
    }

my_new_dict = {k:v**2 for k,v in random_dict.items()}
print(my_new_dict)

my_new_dict2 = {k:v**2 for k,v in random_dict.items() if v % 2 == 0}
print(my_new_dict2)
