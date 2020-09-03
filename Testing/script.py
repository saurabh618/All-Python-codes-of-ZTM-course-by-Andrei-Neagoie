# -*- coding: utf-8 -*-
"""
Created on Mon Aug 24 10:09:27 2020

@author: saura
"""
def add(num):
    try: 
        return int(num) + 5
    except ValueError as err:
        return err
