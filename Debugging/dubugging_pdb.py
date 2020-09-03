# -*- coding: utf-8 -*-
"""
Created on Sun Aug 23 10:21:55 2020

@author: saura
"""
import pdb

def add(n1, n2):
    return n1+n2

pdb.set_trace()
add(4, 'five')

'''
Some useful commands for pdb:
a : Print the argument list of the current function.
step: to run the current line of code, and stop at the first possible occasion
help: to list all the commands available
help <command>: to see what a command does
continue: to continue the program till the error comes
w: previous line, current line and next line content
next: Continue execution until the next line in the current function is reached or it returns.
        
We can change the variables value in the console window as well.
we can type in the variable name to get its value
'''
