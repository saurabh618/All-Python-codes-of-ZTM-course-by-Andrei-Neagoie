# -*- coding: utf-8 -*-
"""
Created on Thu Aug 20 11:14:15 2020

@author: saura
"""
# here we are generating our own generator function, just like a range().

def generator_fn(num):
    print("check")
    #yield 
    for i in range(num):
        print("****")
        yield i*2
        print("####")

g = generator_fn(3)
print(g)
print(next(g))
print(next(g))
print(next(g))
#print(next(g))  # StopIteration error
print(g)

for item in generator_fn(5): 
    print(item)
    
# here it goes to the generator_fn(), gets the 'i' value, pauses the function, until called for the 2nd time, 
# and so on, it doesn't store all the no.s in the memory (just the most recent one).

'''
'yield' pauses the function and comes back to it when we do something to it, which is called 'next'.

if there is the keyword 'yield' written inside the function, then python recognises that its a 
generator function, and won't run the function until the function is being iterated.
'''
