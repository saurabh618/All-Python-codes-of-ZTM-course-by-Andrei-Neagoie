# -*- coding: utf-8 -*-
"""
Created on Sat Aug 15 19:28:17 2020

@author: saura
"""
quote = "to be or not to be"
print(quote.capitalize())
print(quote)    # notice that the original message is unchanged, becuase strings are immutable
quote = quote.capitalize()
print(quote)
print(len(quote)) # len() is a function and not a string method
print(quote.upper())
print(quote.find("not"))
print(quote.replace("be","me"))




