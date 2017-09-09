# -*- coding: utf-8 -*-
"""
Created on Fri Sep  8 20:46:28 2017

@author: karunashi
Initially worked on via Spyder 3.6 IDE, then moved back to Sublime 3
"""

import unittest
from sample_account import Customer

class Test(unittest.TestCase):
    def setUp(self):
        """ Setting up initial values for the test case """
        Customer.set_balance(self, 50)

    def tearDown(self):
    	""" Ending test case"""
        return

if __name__ == "__main__":
    unittest.main()