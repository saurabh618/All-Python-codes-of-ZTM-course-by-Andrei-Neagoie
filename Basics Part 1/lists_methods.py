# -*- coding: utf-8 -*-
"""
Created on Sat Aug 15 20:40:14 2020

@author: saura
"""
print("\nappend")
li = [1,2,3,4,5]
new_li = li.append(100)
print(li)
print(new_li)

print("\ninsert")
new_li = li.insert(2,2000)
print(li)
print(new_li)

print("\nextend")
new_li = li.extend([45,"hello"])
print(li)
print(new_li)

print("\npop")
new_li = li.pop()
print(li)
print(new_li)

print("\npop")
new_li = li.pop(0)
print(li)
print(new_li)

print("\nremove")
new_li = li.remove(2000)
print(li)
print(new_li)

print("\nclear")
new_li = li.clear()
print(li)
print(new_li)
