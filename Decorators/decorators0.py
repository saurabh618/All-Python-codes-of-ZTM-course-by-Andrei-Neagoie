# -*- coding: utf-8 -*-
"""
Created on Wed Aug 19 17:31:49 2020

@author: saura
"""
def my_decorator(func):
    def wrap_func(*args, **kwargs):
        func(*args, **kwargs)
    return wrap_func

@my_decorator
def hello(name, age):
    print(f"Hello {name}, your age is {age}.")
    
@my_decorator   
def logged_in(username):
    print(f"{username} is logged in.")

hello("saurabh", 21)
logged_in("saurabh")

# using decorator is same as doing the below:
# my_decorator(hello)()
