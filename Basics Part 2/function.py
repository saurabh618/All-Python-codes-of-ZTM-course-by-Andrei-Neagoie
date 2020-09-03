# -*- coding: utf-8 -*-
"""
Created on Mon Aug 17 10:51:53 2020

@author: saura
"""
# Positional Parameters
def say_hello(name, age):
    print(f'Hi {name}, your age is {age}')
    
# Default Parameters
def say_hello2(name="jojo", age=25):
    print(f'Hi {name}, your age is {age}')

# Positional Arguments
say_hello("saurabh", 27)

# Default Arguments
say_hello2()
say_hello2("saurabh")

# Key Arguments
say_hello(age = 89, name = "YOHO")