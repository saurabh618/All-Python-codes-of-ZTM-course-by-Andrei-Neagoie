# -*- coding: utf-8 -*-
"""
Created on Wed Aug 19 11:29:05 2020

@author: saura
"""
def multiply_by2(li):
    new_li = []
    for item in li:
        new_li.append(item)
    return new_li

print(multiply_by2([5,6,8]))

'''
If we define 'new_li' outside the function, or print something inside the function, then it is no longer
a pure function.
'''
