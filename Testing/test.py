# -*- coding: utf-8 -*-
"""
Created on Mon Aug 24 09:44:29 2020

@author: saura
"""
import unittest
import script

class TestMain(unittest.TestCase):  # inheriting TestCase class

    def setUp(self):    # this method will run before starting all the other test methods
        print("Starting a method/test: ")
    
    def test_add(self):
        '''This is the info for this particular test'''
        test_param = 10
        result = script.add(test_param)
        self.assertEqual(result,15)
        
    def test_add2(self):
        test_param = 'random string'
        result = script.add(test_param)
        self.assertTrue(isinstance(result,ValueError))
  
    def tearDown(self):   # this method will run after every test method. Generally used to reset/cleaning up data variables.
        print("Cleaning up....")
        
        
class A:
    print("\nClass A")

if __name__ == '__main__':
    unittest.main()     # this will run the entire classes present in the file


class B:
    print("Class B")
