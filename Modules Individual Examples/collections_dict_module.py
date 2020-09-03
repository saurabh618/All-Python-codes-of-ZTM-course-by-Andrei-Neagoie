# -*- coding: utf-8 -*-
"""
Created on Sat Aug 22 18:19:43 2020

@author: saura
"""
from collections import Counter, defaultdict, OrderedDict

li = [1,2,3,4,5,2,3,1,2,2,2,2,7]
sentence = "Helloooo!!! How are you!!"
print(Counter(li))
print(Counter(sentence)) 
# count the no. of occurence of each iterable, and store them in a dict format, 
# with highest count to lowest count order


my_dict = {'a': 1, 'b': 2}
# print(my_dict['c'])     # this gives error

# defaultdict takes the first argument as a callable object (it is a function that can be called)
my_default_dict = defaultdict(int, {'a': 1, 'b': 2})
print(int())
print(my_default_dict['c'])

my_default_dict2 = defaultdict(lambda : 5, {'a': 1, 'b': 2})
print(my_default_dict2['c'])

my_default_dict3 = defaultdict(lambda : "Does not exist", {'a': 1, 'b': 2})
print(my_default_dict3['c'])


d = dict()
d['a'] = 4
d['b'] = 45

d2 = dict()
d2['b'] = 45
d2['a'] = 4

d3 = dict()
d3['b'] = 45
d3['a'] = 4

print(d == d2)      # Order doesn't matter here
print(d2 == d3)     


dict1 = OrderedDict()
dict1['a'] = 4
dict1['b'] = 45

dict2 = OrderedDict()
dict2['b'] = 45
dict2['a'] = 4

dict3 = OrderedDict()
dict3['b'] = 45
dict3['a'] = 4

print(dict1 == dict2)   # different order, hence False
print(dict2 == dict3)   # same order, hence True
