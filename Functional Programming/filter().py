# -*- coding: utf-8 -*-
"""
Created on Wed Aug 19 11:51:27 2020

@author: saura
"""
def only_even(item):
    return item % 2 == 0

my_list = [5,8,9,2,5,6,98,56,62]

print(filter(only_even, my_list))  
print(list(filter(only_even, my_list))) 
print(list(map(only_even, my_list))) 
print(my_list)
