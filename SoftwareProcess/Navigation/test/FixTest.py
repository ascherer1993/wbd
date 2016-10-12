'''
Created on Oct 12, 2016

@author: Aaron
'''
import unittest
import Navigation.prod.Fix as Fix

class Test(unittest.TestCase):


    def setUp(self):
        pass


    def tearDown(self):
        pass


    #    Acceptance Test: 100
#        Analysis - Contructor
#            inputs
#                none
#            outputs
#                instance of Angle
#            state change
#                value is set to 0d0
#
#            Happy path
#                nominal case:  Angle()
#            Sad path
#                none*
#
#               *if we _really_ wanted to be complete, we would test for presence of a parm
#
#    Happy path
    def test100_010_ShouldCreateInstanceOfAngle(self):
        self.assertIsInstance(Fix.Fix(), Fix.Fix)
        # note:   At this point, we don't any way of verifying the value of the angle.
        #         We'll be able to so when we construct tests for the getters


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()