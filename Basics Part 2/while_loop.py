# -*- coding: utf-8 -*-
"""
Created on Sun Aug 16 17:13:44 2020

@author: saura
"""
i = 0
while i < 5:
    print(i)
    i += 1
    break
else:
    print("done")
    
while True:
    response = input("say something: ")
    if (response == 'bye'):
        break
