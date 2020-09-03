# -*- coding: utf-8 -*-
"""
Created on Sun Aug 23 13:27:09 2020

@author: saura
"""
with open("happy\happy.txt", mode = 'a') as my_file:
    text = my_file.write("I am HAPPY!")
    print(text)     # it prints the no. of letters written into the file
    
    
with open("happy\happy.txt", mode = 'r') as my_file:
    print(my_file.read())
    
'''
mode = 'w' : it creates a new file and write into it. If there is an exiting file with the same name, it replaces it.
mode = 'r' : it is used to read the file
mode = 'r+' : it is used to read and write into the file. but it writes from position 0, which might replace some existing text.
mode = 'a' : it appends to the existing file. meaning writing to the file keeping the old content intact.
             if the file doesn't exist, it creates a new one.

if we don't mention the mode, by default it will be considered 'r' mode.

with 'with' we don't need to close the file manually.
'''