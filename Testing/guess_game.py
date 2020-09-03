# -*- coding: utf-8 -*-
"""
Created on Mon Aug 24 13:44:51 2020

@author: saura
"""
import random

def run_guess(guess, answer):
    if  0 < guess < 11:
        if guess == answer:
            print('you are a genius!')
            return True
    else:
        print('hey bozo, I said 1~10')
        return False

if __name__ == '__main__':      # so that the game don't start while testing.
    answer = random.randint(1, 10)
    while True:
        try:
            guess = int(input('guess a number 1~10:  '))
            if (run_guess(guess, answer)):
                break
        except ValueError:
            print('please enter a number')
            continue

'''
we test a function at a time.
that is why it is called unit testing.
hence we try to make pure functions and test them.
'''