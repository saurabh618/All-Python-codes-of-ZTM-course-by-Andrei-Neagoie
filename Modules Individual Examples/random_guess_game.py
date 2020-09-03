# -*- coding: utf-8 -*-
"""
Created on Sat Aug 22 13:34:48 2020

@author: saura
"""
import sys
from random import randint

first = sys.argv[1]
last = sys.argv[2]

random_num = randint(int(first), int(last))

while True:
    user_guess = int(input("Guess the random no.: "))
    if user_guess == random_num:
        print("Congratulations, You WON!!")
        break
    else:
        print("You Lose! Guess again....")
