# -*- coding: utf-8 -*-
"""
Created on Wed Aug 19 17:13:30 2020

@author: saura
"""
def my_decorator(func):
    def wrap_func():
        print("***********")
        func()
        print("***********")
    return wrap_func

@my_decorator
def hello():
    print("Hello!")

hello()

# using decorator is same as doing the below:
# my_decorator(hello)()
