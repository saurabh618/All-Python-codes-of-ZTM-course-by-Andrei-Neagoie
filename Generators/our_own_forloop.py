# -*- coding: utf-8 -*-
"""
Created on Thu Aug 20 12:50:31 2020

@author: saura
"""
def my_own_forloop(iterable):
    iterator = iter(iterable)
    while True:
        try:
            print(iterator)
            print(next(iterator))
        except StopIteration:
            break

my_own_forloop([1,2,3,4,5])
