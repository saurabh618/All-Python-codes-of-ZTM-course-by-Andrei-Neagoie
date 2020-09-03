# -*- coding: utf-8 -*-
"""
Created on Sun Aug 16 12:30:51 2020

@author: saura
"""
a = True
b = False
if a and b:
    print("Both a and b are true")
elif a:
    print("Only a is true")
elif b:
    print("Only b is true")
else:
    print("Both a and b are false")
