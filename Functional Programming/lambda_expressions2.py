# -*- coding: utf-8 -*-
"""
Created on Wed Aug 19 12:57:45 2020

@author: saura
"""

a = [(0,2),(4,4),(10,-1),(5,3)]

a.sort(key=lambda x:x[1], reverse=False)
print(a)
