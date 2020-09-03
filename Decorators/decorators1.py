# -*- coding: utf-8 -*-
"""
Created on Wed Aug 19 16:41:53 2020

@author: saura
"""
def hello():
    print("hello!")
    
greet = hello

del hello   
# here the function is not deleted, just the keyword, because greet is still pointing to the function memory
# and python has not deleted it
#(hello()  # this will give error, because it has been deleted
print(greet)
greet()
