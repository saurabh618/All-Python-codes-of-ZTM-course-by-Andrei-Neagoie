# -*- coding: utf-8 -*-
"""
Created on Wed Aug 19 12:11:32 2020

@author: saura
"""

from functools import reduce

def accumulator(acc, item):
    print(f'acc: {acc}, item: {item}')
    return acc+item

my_list = [1,2,3,4,5]
print(reduce(accumulator, my_list))     # by default takes '0' as the 3rd argument
print(reduce(accumulator, my_list, 10)) 
print(my_list)

'''
acc is nothing but the return of the last iteration.
'''