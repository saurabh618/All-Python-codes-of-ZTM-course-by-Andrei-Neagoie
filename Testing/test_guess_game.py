# -*- coding: utf-8 -*-
"""
Created on Mon Aug 24 13:45:14 2020

@author: saura
"""
import unittest
import guess_game

class testGame(unittest.TestCase):
    def test_game(self):
        result = guess_game.run_guess(5,5)
        self.assertTrue(result)
        
    def test_game2(self):
        result = guess_game.run_guess(0,5)
        self.assertFalse(result)        
        
    def test_game3(self):
        result = guess_game.run_guess(15,4)
        self.assertFalse(result)
                
if __name__ == '__main__':
    unittest.main()   
    