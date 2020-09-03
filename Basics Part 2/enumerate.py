# -*- coding: utf-8 -*-
"""
Created on Sun Aug 16 17:11:25 2020

@author: saura
"""
# we can pass any iterable to enumerate, and it will store them as separate tuple with index starting from 0.
for i in enumerate('Hello World'):
    print(i)
    
for i,j in enumerate([1,2,3,4]):
    print(i,j)

for i in enumerate((1,2,3,4,5)):
    print(i)

print(list(item for item in enumerate('123456789')))
print((i * i for i in range(8)))

print(list(enumerate('123456789')))

print(dict(list(enumerate((i * i for i in range(1,11)),1))))
