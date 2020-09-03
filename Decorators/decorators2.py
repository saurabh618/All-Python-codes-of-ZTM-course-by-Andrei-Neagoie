# -*- coding: utf-8 -*-
"""
Created on Wed Aug 19 16:57:31 2020

@author: saura
"""
def hello(func):
    func()
    
def greet():
    print("Hello!")
    
hello(greet)

# this example shows us that functions can also be used as variables.
