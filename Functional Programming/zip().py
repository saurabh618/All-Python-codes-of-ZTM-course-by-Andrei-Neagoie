# -*- coding: utf-8 -*-
"""
Created on Wed Aug 19 11:54:19 2020

@author: saura
"""
li1 = [1,2,3]
set1 = {4,5,6}
tuple1 = (7,8,9)

print(zip(li1, set1, tuple1))
print(list(zip(li1, set1, tuple1)))     # combines the items sequence wise into a sequence of tuples
print(li1, set1, tuple1)

'''
use the same no.s of items in all the iterables, otherwise it can ruin the sequence.
'''