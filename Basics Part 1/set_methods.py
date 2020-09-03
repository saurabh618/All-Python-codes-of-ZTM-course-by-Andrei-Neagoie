# -*- coding: utf-8 -*-
"""
Created on Sun Aug 16 12:15:33 2020

@author: saura
"""
# this is very similar to Venn diagrams.

my_set = {1,2,3,4,5}
your_set = {4,5,6,7,8,9,10}

# .difference()
# .discard()
# .difference_update()
# .intersection()
# .isdisjoint()
# .issubset()
# .issuperset()
# .union()

print("\ndifference")
print(my_set.difference(your_set))
print(my_set)

print("\ndiscard")
print(my_set.discard(5))
print(my_set)

print("\ndifference_update")
print(my_set.difference_update(your_set))
print(my_set)

my_set = {1,2,3,4,5}

print("\nintersection")
print(my_set.intersection(your_set))
print(my_set & your_set)

print("\nisdisjoint")
print(my_set.isdisjoint(your_set))
my_set = {1,2,3}
print(my_set.isdisjoint(your_set))

print("\nissubset")
print(my_set.issubset(your_set))
my_set = {4,6,8}
print(my_set.issubset(your_set))

print("\nissuperset")
print(my_set.issuperset(your_set))
print(your_set.issuperset(my_set))

print("\nunion")
my_set = {1,2,3,4,5}
print(my_set.union(your_set))
# or
print(my_set | your_set)