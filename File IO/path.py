# -*- coding: utf-8 -*-
"""
Created on Sun Aug 23 13:46:18 2020

@author: saura
"""
with open(".\happy\happy.txt", mode = 'a') as my_file:
    text = my_file.write("I am HAPPY!")
    print(text)     # it prints the no. of letters written into the file
    
    
with open("E:\\Udemy Courses\\Python - Zero to Mastery\\Exercise\\File IO\\happy\\happy.txt", mode = 'r') as my_file:
    print(my_file.read())
    
'''
we can give absolute path
or related path (wrt to the current folder)
../ means go back one folder
./ menas start from current folder

pathlib module: for windows, linex paths are different, so we can use this module so that our code works in all machines.
'''