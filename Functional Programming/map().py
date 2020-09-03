# -*- coding: utf-8 -*-
"""
Created on Wed Aug 19 11:39:00 2020

@author: saura
"""
def multiply_by2(item):
    return item*2

my_list = [5,8,9]

print(map(multiply_by2, my_list))   # it returns a map object, which then we can convert to a list/tuple/set
print(list(map(multiply_by2, my_list))) # notice that we just write the function name without the curly braces
print(my_list)

'''
notice that map is not modifying anything, and creating a new list. 
it is also using separate data and function to work upon them.
it's a nice concept of Functional programming and pure function.
'''
