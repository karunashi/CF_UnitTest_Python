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
        Customer.set_balance(self, 50.6)

    def testBalanceSetup(self):
        """ Test case to check that method, set_balance, works """
        Customer.set_balance(self, 10.34)
        self.assertEqual(self.balance, 10.34)

    def testWithdrawNeg(self):
        """ Test case to check if negative values work for withdrawing. """
        withdrawNeg_1 = Customer.withdraw(self, -10)

        self.assertEqual(withdrawNeg_1, 40.6)
        """ AssertionError: 60.6 != 40.6, perhaps disallow negative numbers when inputting values into withdraw to only be integers (no negatives)"""

    def testWithdrawCheckErr(self):
        """ Check withdrawal with numbers with decimals and also if the error check for Runtime Error works. """
        Withdraw_1 = Customer.withdraw(self, 30.6)
        Withdraw_2 = Customer.withdraw(self, 5.5)

        self.assertEqual(Withdraw_1, 20)
        self.assertEqual(Withdraw_2, 14.5)

        self.assertRaises(RuntimeError, Customer.withdraw, self, 14.51)

    """ This method should check if withdrawal that exceeds the current amount of 14.5 should trigger the RuntimeError, which if it does, shouldn't fail the test use the method below instead as suggested by documentation
        with self.assertRaises(RuntimeError):
            Customer.withdraw(self, 20)   """

    def testDeposit(self):
        Deposit_1 = Customer.deposit(self, 10)
        Deposit_2 = Customer.deposit(self, -10.3)
        Deposit_3 = Customer.deposit(self, 5.3)

        self.assertEqual(Deposit_1, 60.6)
        self.assertEqual(Deposit_2, 50.3)
        self.assertEqual(Deposit_3, 55.6)
        """Deposit_3 seems to give AssertionError:  55.599999999999994 != 55.6"""


    def tearDown(self):
    	return
    	""" Ending test case"""

if __name__ == "__main__":
    unittest.main()