# -*- coding: utf-8 -*-
"""
Created on Mon Aug 17 14:26:01 2020

@author: saura
"""
# *args and **kwargs

def super_func(*args, **kwargs):    # we can actually name these parameters anything we want, 
                                    # but its a good practice to give the same name only.
    print(args)
    print(type(args)) 	# class tuple
    print(*args)
    # print(type(*args)) 	# gives error

    print(kwargs)
    # print(**kwargs) 	# gives error
    print(kwargs.keys())
    print(kwargs.values())
    print(type(kwargs)) 	# class dict

    total = 0
    for items in kwargs.values():
        total += items

    return sum(args) + total

print(super_func(1,2,3,4,5, num1 = 5, num2 = 10))

# Rules for the order of parameters
# positional parameters, *args, default parameters, **kwargs
# for eg.
# def super_func2(name, *args, age = 10, **kwargs):