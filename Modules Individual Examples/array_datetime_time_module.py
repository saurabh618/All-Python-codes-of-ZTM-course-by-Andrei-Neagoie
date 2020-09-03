# -*- coding: utf-8 -*-
"""
Created on Sat Aug 22 19:16:15 2020

@author: saura
"""
import datetime
from time import time
from array import array

print(datetime.time())
# print(datetime.time(55,45,2))   # hour must be between 0 to 23
print(datetime.time(5,45,2)) 

print(datetime.date.today())

print(time())   # time in unix code

arr = array('i', [1,2,3])
print(arr)
print(arr[0])
'''
# array in python are faster than list, and takes less memory.
# the first argument is the 'typecode'
'f' = float (4 byte)
'd' = double (8 byte)
'b' = signed char (1 byte)
'i' = signed int (2 byte)
'l' = signed long (4 byte)
etc.
'''