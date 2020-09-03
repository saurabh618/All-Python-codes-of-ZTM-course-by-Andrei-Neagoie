# -*- coding: utf-8 -*-
"""
Created on Mon Aug 17 15:24:53 2020

@author: saura
"""
total = 0

def count():
    global total 
    total += 1  # here we are referenced total before assignment, hence we have declare 'global total' first 
    return total

count()
count()
count()

print(total)

# i += 1 	# this gives error, similaryly we have declare total first in the count() function
