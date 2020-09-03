# -*- coding: utf-8 -*-
"""
Created on Thu Aug 20 11:06:14 2020

@author: saura
"""
try:
    age = int(input("age: "))
    age = 10/age
    raise ValueError("Ending the program")
    # raise Exception("quit")

except ValueError:
    print("Please enter a no.")