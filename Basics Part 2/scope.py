# -*- coding: utf-8 -*-
"""
Created on Mon Aug 17 15:12:29 2020

@author: saura
"""
a = 1

def parent_func():
    #a = 10
    # total = 0
    def local_func():
        return a
        return sum  # here it will check what is the value of sum, locally, then parent, then globally and finally in the built in function
    return local_func()

print(parent_func())
print(a)

# print(total)    # this will produce an error, as 'total' is undefined.

# scope of a function remains inside the function only.

#1 - start with local
#2 - parent local
#3 - global
#4 - built in python functions