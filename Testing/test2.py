# -*- coding: utf-8 -*-
"""
Created on Mon Aug 24 13:23:16 2020

@author: saura
"""
import unittest
import script

class TestMain(unittest.TestCase):  # inheriting TestCase class
    def test_add(self):
        test_param = 10
        result = script.add(test_param)
        self.assertEqual(result,15)
        
    def test_add2(self):
        test_param = 'random string'
        result = script.add(test_param)
        self.assertTrue(isinstance(result,ValueError))

if __name__ == '__main__':
	unittest.main()
