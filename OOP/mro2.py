# -*- coding: utf-8 -*-
"""
Created on Tue Aug 18 21:04:09 2020

@author: saura
"""
class X:pass
class Y:pass
class Z:pass
class A(X,Y):pass
class B(Y,Z):pass
class M(B,A,Z):pass

print(M.mro())

# avoid using this in codes, because MRO rules are very confusing to understand.
