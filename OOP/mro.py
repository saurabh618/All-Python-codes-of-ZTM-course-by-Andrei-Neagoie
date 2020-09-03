# -*- coding: utf-8 -*-
"""
Created on Tue Aug 18 20:43:40 2020

@author: saura
"""
# Method Resolution Order
# it tells the order of the preferences for classes

class A:
    num = 10

class B(A):
    pass

class C(A):
    num = 1

class D(B,C):     
    pass

print(D.num)

print(D.mro())
print(D.__mro__)
# both the above are same
