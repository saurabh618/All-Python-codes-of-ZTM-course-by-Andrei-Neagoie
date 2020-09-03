# -*- coding: utf-8 -*-
"""
Created on Thu Aug 20 10:44:36 2020

@author: saura
"""
def division_fn(num1, num2):
    try: 
        return num1/num2
    except (ZeroDivisionError, TypeError) as err:
        print(f'error: {err}')

print(division_fn(1,'0'))
print(division_fn(1,0))
print(division_fn(1,4))
