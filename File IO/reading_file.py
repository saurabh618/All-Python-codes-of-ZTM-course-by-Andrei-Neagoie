# -*- coding: utf-8 -*-
"""
Created on Sun Aug 23 12:38:53 2020

@author: saura
"""
my_file = open('test.txt')
print(my_file)
print(my_file.read())

print(my_file.read())   # it won't be printing anything. because the cursor is at the end of the file.

print("Seek 0")
my_file.seek(0)     # we reset the cursor to the initial position.

print(my_file.read())   # and so we can now read the file from the initial position till end.

print("Seek 0")
my_file.seek(0)

print(my_file.readline())   # reads a line and stop the cursor
print(my_file.readline())
print(my_file.readline())
print(my_file.readline())

print("Seek 0")
my_file.seek(0)

print(my_file.readlines()) # store all the lines in a list
print(my_file.readlines())

my_file.close()
