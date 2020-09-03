# -*- coding: utf-8 -*-
"""
Created on Wed Aug 19 13:51:49 2020

@author: saura
"""
my_list = []

for item in 'hello':
    my_list.append(item)

print(my_list)

my_list1 = [item for item in 'Saurabh']
print(my_list1)

my_list2 = [num**2 for num in range(1,11)]
print(my_list2)

# only even squares
my_set = {num**2 for num in range(1,11) if num**2 % 2 == 0}
print(my_set)
# remember that set don't contain duplicate values
