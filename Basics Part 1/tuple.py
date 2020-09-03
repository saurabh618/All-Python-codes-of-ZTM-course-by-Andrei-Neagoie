# -*- coding: utf-8 -*-
"""
Created on Sun Aug 16 11:33:18 2020

@author: saura
"""
my_tuple = (1,2,3,4,5,2)
print(my_tuple[0])
print(my_tuple[1:2])    # be carefull here, we also get a 'comma' when we just store a signle tuple value
print(my_tuple[0:2])
print(my_tuple[::-2])
print(2 in my_tuple)

# my_tuple[0] = 4     # it will be an error, because tuple are immutable
print(my_tuple)

print(my_tuple.count(2))
print(my_tuple.index(5))

my_dict = {
    "age": 45,
    (1,2): "hello"
    }
print(my_dict)
print(my_dict.items())   # returns key:value pair as a tuple
print(my_dict[(1,2)])

a,b,c,*other = (1,2,3,4,5,6,7,8,9)  # it stores as list if the variable has more than 1 item, otherwise as int.
print(a)
print(type(a))
print(other)
print(type(other))