# -*- coding: utf-8 -*-
"""
Created on Sat Aug 22 11:15:56 2020

@author: saura
"""
import utilities
import shopping.shopping_cart

print(utilities)
print(utilities.mult(4,5))
print(utilities.divide(15,3))

print(shopping)
print(shopping.shopping_cart)
print(shopping.shopping_cart.buy('apple'))

print(__name__)
if __name__ == '__main__':
    print("this is the file being run, and not getting imported.")
