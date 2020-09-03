# -*- coding: utf-8 -*-
"""
Created on Thu Aug 20 13:15:14 2020

@author: saura
"""
def fib(num):
    a = 0
    b= 1
    for i in range(num):
        yield a
        temp = a
        a = b
        b = temp + b

num = int(input("Enter a number: "))

for i in fib(num):
    print(i)
