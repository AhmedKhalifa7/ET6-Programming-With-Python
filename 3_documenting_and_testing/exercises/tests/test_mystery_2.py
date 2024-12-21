#!/user/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 20/12/2024

@author: Ahmed Khalifa
"""
import unittest

from ..length import length

class TestLength(unittest.TestCase):
    """ Test the length function """
 
    def test_empty_list(self):
        """It should evaluate [] to 0"""
        actual = length([])
        expected = 0
        self.assertEqual(actual, expected)

    def test_list_with_one_element(self):
        """It should evaluate [3] to 1"""
        actual = length([3])
        expected = 1
        self.assertEqual(actual, expected)

    def test_list_with_duplicate_elements(self):
        """It should evaluate [3,3] to 2"""
        actual = length([3, 3])
        expected = 2
        self.assertEqual(actual, expected)
        
    def test_list_with_10_elements(self):
        """It should evaluate [1,2,4,5,6,7,8,0,0,4] to 10"""
        actual = length([1,2,4,5,6,7,8,0,0,4])
        expected = 10
        self.assertEqual(actual, expected)
        
    #def test_if_parameter_is_not_a_list(self):
        #assert isinstance(length(a), list)
