# -*- coding: utf-8 -*-
"""
Created on Sun Aug 23 17:22:13 2020

@author: saura
"""
import re

string = "this is a really cool string really!"

a = re.search('really',string)
print(a)

# the below 4 commands will give error if the searching string does not exist.
print(a.span())
print(a.start())
print(a.end())
print(a.group())

pattern = re.compile('really')

b = pattern.search(string)
c = pattern.findall(string)

pattern = re.compile('this is a really cool string really!')
d = pattern.fullmatch('this is a really cool string really!')
e = pattern.fullmatch('hello this is a really cool string really!')    # this should be exact match, otherwise returns none

pattern = re.compile('really')
f = pattern.match('really cool feature')    # it starts matching from the first character otherwise returns none
g = pattern.match('yo really')

print(f"b: {b}")
print(f"c: {c}")
print(f"d: {d}")
print(f"e: {e}")
print(f"f: {f}")
print(f"g: {g}")
