# -*- coding: utf-8 -*-
"""
Created on Thu Aug 20 12:55:26 2020

@author: saura
"""
class OurOwnRange():
    current = 0
    def __init__(self,first,last):
        self.first = first
        self.last = last
        
    def __iter__(self):
        return self
    
    def __next__(self):
        print("hehehheh")
        # if self.current < self.last:
        #     num = OurOwnRange.current
        #     OurOwnRange.current += 1
        #     return num
        # raise StopIteration
    
gen = OurOwnRange(0,10)
print(gen)

for i in gen:
    print(i)

'''
loops by default deal with StopIteration error. they have build in functionality to handle them.
'''
