# -*- coding: utf-8 -*-
"""
Created on Sun Aug 16 11:55:22 2020

@author: saura
"""
my_set = {1,2,3,4,5,5,5}
my_set.add(100)
my_set.add(2)
print(my_set)
# print(my_set[0])  # we cannot do this, it produces an error, because set is an unordered collection of objects
print(len(my_set))

print(5 in my_set)
print(my_set)

print(list(my_set))

new_set = my_set.copy()
print(my_set.clear())
print(my_set)
print(new_set)

my_list = [1,2,3,4,5,5,5]
print(set(my_list))     # this way we can remove the duplicate items from the list
