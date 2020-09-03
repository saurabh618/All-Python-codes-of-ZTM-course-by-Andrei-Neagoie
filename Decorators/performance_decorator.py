# -*- coding: utf-8 -*-
"""
Created on Wed Aug 19 17:44:13 2020

@author: saura
"""
from time import time

def performance(fn):
    def wrap_fn(*args, **kwargs):
        t1 = time()
        fn(*args, **kwargs)
        t2 = time()
        print(f'It took {t2-t1} sec')
    return wrap_fn

@performance
def long_fn():
    for i in range(10000000):
        i*5

long_fn()        
