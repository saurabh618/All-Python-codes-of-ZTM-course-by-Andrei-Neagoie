# -*- coding: utf-8 -*-
"""
Created on Mon Aug 17 14:02:18 2020

@author: saura
"""
def sum(num1, num2):
    def another_func(n1,n2):
        return n1 + n2
    return another_func 

def sum2(num1, num2):
    def another_func2(n1,n2):
        return n1 + n2
    return another_func2(num1, num2) 

print(sum(10,5))    # this will just return the address of the function
print(sum(10,5)(5,8))    # this will give arguments to the another_func

# above is same as doing:
total = sum(10,5)
print(total)
print(total(5,8))


print(sum2(10,5))

# print(another_func(45, 55))   # this will give error, becuase the function is actually undefined,
                                # and to call this function, first we will have to call the parent function.
                                # so we can get the memory location of the function.