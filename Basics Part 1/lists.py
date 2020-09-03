# -*- coding: utf-8 -*-
"""
Created on Sat Aug 15 19:54:30 2020

@author: saura
"""
li = [1, 2.5, "hello", True]
print(li)

amazon_cart = [
    "laptop",
    "book",
    "phone",
    "pen",
    "key"
   ]
# start:stop:stepover
print(amazon_cart[0])
print(amazon_cart[::-1])
print(amazon_cart[0:2])
print(amazon_cart)

print("\nPart-2")
new_cart = amazon_cart # here we are actually passing the address of the old list, 
                       # and not copying and storing the list in new location.
new_cart[0] = "PC" # lists are mutable, unlike strings which are immutable.
print(amazon_cart) # notice that the old list is also modified.
print(new_cart)

print("\nPart-3")
flipkart_cart = amazon_cart[:] # here we are actually copying the whole list to another location or we can use .copy()
flipkart_cart[0] = "headphones"
print(amazon_cart)
print(flipkart_cart)

print("\nPart-4")
my_list = [1,2,3]
bonus = my_list + [5]
my_list[0] = 'z'
print(my_list)
print(bonus)