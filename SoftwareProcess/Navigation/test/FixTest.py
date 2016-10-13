'''
Created on Oct 12, 2016

@author: Aaron
'''
import unittest
import Navigation.prod.Fix as Fix
import Navigation.prod.Sighting as Sighting

class Test(unittest.TestCase):


    def setUp(self):
        self.fix = Fix.Fix()
        self.sighting = Sighting.Sighting();
        
        
        self.height_1 = 10
        self.pressure_1 = 50
        self.temperature_1 = 70
        self.altitude_1 = 10
        self.horizon_1 = "natural"
        self.horizon_2 = "artificial"
        pass


    def tearDown(self):
        pass


#    Acceptance Test: 100
#        Analysis - Constructor
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
        test = self.fix.setSightingFile("log.txt")
        self.assertIsInstance(test, bool)
        # note:   At this point, we don't any way of verifying the value of the angle.
        #         We'll be able to so when we construct tests for the getters
        
    def test200_910_FileNameNotValid(self):
        with self.assertRaises(ValueError):
            self.fix.setSightingFile("log.txsdft")
        # note:   At this point, we don't any way of verifying the value of the angle.
        #         We'll be able to so when we construct tests for the getters
        
    #unsure how to test file could not be created to or appended to    
        
#    Acceptance Test: 300
#        Analysis - getSightings
#            inputs
#                none
#            outputs
#                Tuple of approximate location
#            state change
#                writes to log file
#
#            Happy path
#                nominal case: getSightings()
#            Sad path
#                file cannot be appended to 


    def test300_010_ShouldReturnTuple(self):
        test = self.fix.getSightings()
        self.assertIsEqual(test, ("0d0.0", "0d0.0"))



#*******************************************************************************************************************
# Unit Tests
#*******************************************************************************************************************

#Sighting.Py
#I plan to use the 400's for all of the sightings tests to just make things easier on me, incrementing by 10s


#    Unit Test: 400_010
#        Analysis - Get adjusted Altitude
#            inputs
#                none
#            outputs
#                adjusted altitude
#            state change
#                adjusted altitude changes
#
#            Happy path
#                nominal case: getAdjustedAltitude()
#            Sad path
#                none

def test400_010_ShouldGetAdjustedAltitude(self):
        adjustedAltitude = self.sighting.getAdjustedAltitude()
        self.assertIsEqual(adjustedAltitude, 50)

#    Unit Test: 410_010
#        Analysis - Calculate Dip
#            inputs
#                height
#            outputs
#                calculated dip
#            state change
#                none
#
#            Happy path
#                nominal case: _calculateDip()
#            Sad path
#                none

def test410_010_CalculateDipWithNatural(self):
        dip = self.sighting._calculateDip(self.height_1, self.horizon_1)
        self.assertIsEqual(dip, ("0d0.0", "0d0.0"))


def test410_020_CalculateDipWithArtificial(self):
        dip = self.sighting._calculateDip(self.height_1, self.horizon_2)
        self.assertIsEqual(dip, ("0d0.0", "0d0.0"))

#    Unit Test: 420_010
#        Analysis - Calculate Refraction
#            inputs
#                height
#            outputs
#                calculated dip
#            state change
#                none
#
#            Happy path
#                nominal case: _calculateDip()
#            Sad path
#                none

def test420_010_CalculateRefraction(self):
        test = self.sighting._calculateRefraction(self.pressure_1, self.temperature_1, self.altitude_1)
        self.assertIsEqual(test, ("0d0.0", "0d0.0"))

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()