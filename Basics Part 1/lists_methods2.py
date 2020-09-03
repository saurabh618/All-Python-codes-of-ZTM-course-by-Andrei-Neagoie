# -*- coding: utf-8 -*-
"""
Created on Sat Aug 15 21:02:10 2020

@author: saura
"""
li = ['a','b','c','d','e','d']
print(li.index('d')) # if that value is not there in the list, then it will throw an error and program will stop running.

# lookup:start:stop
print(li.index('d',0,5))

print('a' in li) # we use this to avoid the error.
print('x' in li)

name = 'saurabh'
print('b' in name) # we can use this with strings as well

print(li.count('d'))

