'''
Created on Oct 12, 2016

@author: Aaron
'''
import unittest
import Navigation.prod.Fix as Fix

class Test(unittest.TestCase):


    def setUp(self):
        self.fix = Fix.Fix()
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
    def test100_010_ShouldCreateInstanceOfFix(self):
        self.assertIsInstance(Fix.Fix(), Fix.Fix)
        # note:   At this point, we don't any way of verifying the value of the angle.
        #         We'll be able to so when we construct tests for the getters


    #    Acceptance Test: 200
#        Analysis - setSightingsFile
#            inputs
#                name of file
#            outputs
#                boolean representing whether file is new or not
#            state change
#                writes to log file
#
#            Happy path
#                nominal case: setSightingsFile(filename)
#            Sad path
#                filename is not valid
#                file cannot be created or appended to 


    def test200_010_ShouldCreateOrAppendToLog(self):
        test = self.fix.setSightingFile("Hello")
        self.assertIsInstance(test, bool)
        # note:   At this point, we don't any way of verifying the value of the angle.
        #         We'll be able to so when we construct tests for the getters


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()