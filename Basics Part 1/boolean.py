# -*- coding: utf-8 -*-
"""
Created on Sat Aug 15 19:33:39 2020

@author: saura
"""
is_cool = True
is_cool = False
print(bool(-0))
print(bool(0))
print(bool(1))
print(bool(0.5))
print(bool('0'))
print(bool('True'))
print(bool('False'))
print(bool(False))
print(bool('any random thing'))

# All values are considered "truthy" except for the following, which are "falsy":
#     None
#     False
#     0
#     0.0
#     0j
#     Decimal(0)
#     Fraction(0, 1)
#     [] - an empty list
#     {} - an empty dict
#     () - an empty tuple
#     '' - an empty str
#     b'' - an empty bytes
#     set() - an empty set
#     an empty range, like range(0)
#     objects for which
#         obj.__bool__() returns False
#         obj.__len__() returns 0
