'''
Created on Dec 2, 2016

@author: Aaron
'''
import unittest
import uuid
import os
import Navigation.prod.Fix as F
import Navigation.prod.ApproximateLocation as AL
import Navigation.prod.Angle as Angle


class Test(unittest.TestCase):


    @classmethod
    def setUpClass(cls):
        cls.className = "Fix."
        cls.logStartString = "Log file:"
        cls.starSightingString = "Sighting file:"
        cls.starSightingErrorString = "Sighting errors:"
        cls.ariesFileString = "Aries file:"
        cls.starFileString = "Star file:"
        cls.DEFAULT_LOG_FILE = "log.txt"
        cls.ariesFileName = "CA03_Valid_Aries.txt"
        cls.starFileName = "CA03_Valid_Stars.txt"
        cls.testToFileMap = [
            ["validStarSightingFile", "CA02_200_ValidStarSightingFile.xml"],
            ["validAriesFile", "CA03_Valid_Aries.txt"],           
            ["validStarFile", "CA03_Valid_Stars.txt"], 
            ["genericValidStarSightingFile", "CA02_300_GenericValidStarSightingFile.xml"], 
            ["genericValidSightingFileWithMixedIndentation", "CA02_300_ValidWithMixedIndentation.xml"],
            ["validOneStarSighting", "CA02_300_ValidOneStarSighting.xml"],
            ["validMultipleStarSighting", "CA02_300_ValidMultipleStarSighting.xml"],
            ["validMultipleStarSightingSameDateTime", "CA02_300_ValidMultipleStarSightingSameDateTime.xml"],
            ["validWithNoSightings", "CA02_300_ValidWithNoSightings.xml"],
            ["validWithExtraneousTags", "CA02_300_ValidWithExtraneousTags.xml"],
            ["validOneStarNaturalHorizon","CA02_300_ValidOneStarNaturalHorizon.xml"],
            ["validOneStarArtificialHorizon", "CA02_300_ValidOneStarArtificialHorizon.xml"],
            ["validOneStarWithDefaultValues", "CA02_300_ValidOneStarWithDefaultValues.xml"],
            ["invalidWithMissingMandatoryTags","CA02_300_InvalidWithMissingMandatoryTags.xml"],
            ["invalidBodyTag","CA02_300_InvalidBody.xml"],
            ["invalidDateTag","CA02_300_InvalidDate.xml"],
            ["invalidTimeTag","CA02_300_InvalidTime.xml"],
            ["invalidObservationTag","CA02_300_InvalidObservation.xml"],
            ["invalidHeightTag","CA02_300_InvalidHeight.xml"],
            ["invalidTemperatureTag", "CA02_300_InvalidTemperature.xml"],
            ["invalidPressureTag","CA02_300_InvalidPressure.xml"],
            ["invalidHorizonTag","CA02_300_InvalidHorizon.xml"],
            ["validLatLon", "CA03_300_ValidStarLatLon.xml"],
            ["validLatLonInterpolated", "CA03_300_ValidStarLatLonInterpolationRequired.xml"]
            ]  



        
#----------          
    def setUp(self):
        if(os.path.isfile(self.DEFAULT_LOG_FILE)):
            os.remove(self.DEFAULT_LOG_FILE) 
        # generate random log file name
        self.RANDOM_LOG_FILE = "log" + str(uuid.uuid4())[-12:] + ".txt"
        self.deleteNamedLogFlag = False
    
    def tearDown(self):
        if(self.deleteNamedLogFlag):
            try:
                if(os.path.isfile(self.RANDOM_LOG_FILE)):
                    os.remove(self.RANDOM_LOG_FILE)  
            except:
                pass


#==================== Fix.getSightings ====================
# 100 getSightings
#    Analysis
#        inputs:
#            assumedLatitude: string, optional, has form h0d0.0 or 0d0.0, len >= 1        regression
#            assumedLongitude: string, optional, has form h0d0.0 or 0d0.0, len >= 1        regression
#        outputs:
#            returns:  tuple containing assumed values                               regression
#|           also:    writes "Log file: " + writes all sightings and caluclations to log     new to CA05
#        Entry criterion:
#            setSightingsFile must be called first#

#    Happy tests:
#        logFile:  
#            test 010:    omit parm and receive back values
#            test 020:    Parameters at 0d0.0        
#            test 030:    north hemisphere                
#            test 040:    south hemisphere        
#            test 050:    non zero latitude
#            test 060:    Correct final values
#            existing logfile  -> Fix("myLog.txt") (assuming myLog.txt exits)
#    Sad tests:
#        logFile:
#            test 910:    out of range
#            test 920:    invalid specifications (not h0d0.0)
#            test 930:    files not set
#
#    NOTE: Previous tests check for a lot of the reading in so i will not touch it in this test file
#    
#+++++++++++++++++++ Happy Path Tests ++++++++++++++++++++  
#----------      

    def test100_010_ShouldReceiveEmptyParameters(self):
        'parse sighting file that valid tags'
        testFile = self.mapFileToTest("genericValidStarSightingFile")
        #expectedResult = ("0d0.0", "0d0.0")
        theFix = F.Fix()
        theFix.setSightingFile(testFile)
        theFix.setStarFile(self.starFileName)
        theFix.setAriesFile(self.ariesFileName)
        result = theFix.getSightings()
        
    def test100_020_ShouldReceiveValidParametersAtEquator(self):
        'parse sighting file that valid tags'
        testFile = self.mapFileToTest("genericValidStarSightingFile")
        #expectedResult = ("0d0.0", "0d0.0")
        theFix = F.Fix()
        theFix.setSightingFile(testFile)
        theFix.setStarFile(self.starFileName)
        theFix.setAriesFile(self.ariesFileName)
        result = theFix.getSightings("0d0.0", "0d0.0")

    def test100_030_ShouldReceiveValidParametersInNHem(self):
        'parse sighting file that valid tags'
        testFile = self.mapFileToTest("genericValidStarSightingFile")
        #expectedResult = ("0d0.0", "0d0.0")
        theFix = F.Fix()
        theFix.setSightingFile(testFile)
        theFix.setStarFile(self.starFileName)
        theFix.setAriesFile(self.ariesFileName)
        result = theFix.getSightings("N15d0.0", "0d0.0")

    def test100_040_ShouldReceiveValidParametersInSHem(self):
        'parse sighting file that valid tags'
        testFile = self.mapFileToTest("genericValidStarSightingFile")
        #expectedResult = ("0d0.0", "0d0.0")
        theFix = F.Fix()
        theFix.setSightingFile(testFile)
        theFix.setStarFile(self.starFileName)
        theFix.setAriesFile(self.ariesFileName)
        result = theFix.getSightings("S15d0.0", "0d0.0")
        
    def test100_050_ShouldReceiveValidParametersWithNonZeroLong(self):
        'parse sighting file that valid tags'
        testFile = self.mapFileToTest("genericValidStarSightingFile")
        #expectedResult = ("0d0.0", "0d0.0")
        theFix = F.Fix()
        theFix.setSightingFile(testFile)
        theFix.setStarFile(self.starFileName)
        theFix.setAriesFile(self.ariesFileName)
        result = theFix.getSightings("0d0.0", "15d0.0")
        
        
    def test100_060_ShouldReturnCorrectValues(self):
        'parse sighting file that valid tags'
        testFile = self.mapFileToTest("genericValidStarSightingFile")
        expectedResult = ("N29d6.8", "82d52.9")
        theFix = F.Fix()
        theFix.setSightingFile(testFile)
        theFix.setStarFile(self.starFileName)
        theFix.setAriesFile(self.ariesFileName)
        result = theFix.getSightings("N27d59.5", "88d33.4")
        self.assertTupleEqual(expectedResult, result, 
                              "Minor:  incorrect return value from getSightings")



    def test100_910_ShouldReturnErrorOnInvalidAssumedLatitudeAtEquator(self):
        testFile = self.mapFileToTest("genericValidStarSightingFile")
        expectedResult = ("N29d6.8", "82d52.9")
        theFix = F.Fix()
        theFix.setSightingFile(testFile)
        theFix.setStarFile(self.starFileName)
        theFix.setAriesFile(self.ariesFileName)       
        with self.assertRaises(ValueError) as context:
            result = theFix.getSightings("27d59.5", "88d33.4")

    def test100_910_ShouldReturnErrorOnInvalidAssumedLatitudeNotAtEquator(self):
        testFile = self.mapFileToTest("genericValidStarSightingFile")
        expectedResult = ("N29d6.8", "82d52.9")
        theFix = F.Fix()
        theFix.setSightingFile(testFile)
        theFix.setStarFile(self.starFileName)
        theFix.setAriesFile(self.ariesFileName)       
        with self.assertRaises(ValueError) as context:
            result = theFix.getSightings("N0d0.0", "88d33.4")
#==================== Unit tests ====================
# 200 ApproximateLocation
# These most likely will not have sad cases because they should all be internal and always send the right info



#    getDistanceAdjustment
#        inputs:
#            geographicPositionLongitude: Angle object        regression
#            geographicPositionLatitude: Angle object        regression
#            assumedLongitude: Angle object        regression
#            assumedLatitude: Angle object        regression
#            adjustedAltitude: Angle object        regression
#            
#        outputs:
#            returns:  Angle object representing distance adjustment                             regression


    def test200_010_ShouldReturnDistanceAdjustment(self):
        # expectedResult = 104.384859
        expectedResult = 11168
        
        geographicPositionLatitude = Angle.Angle()
        geographicPositionLatitude.setDegrees(200)
        
        geographicPositionLongitude = Angle.Angle()
        geographicPositionLongitude.setDegrees(100)
        
        assumedLatitude = Angle.Angle()
        assumedLatitude.setDegrees(150)
        
        assumedLongitude = Angle.Angle()
        assumedLongitude.setDegrees(50)
    
        
        adjustedAltitude = Angle.Angle()
        adjustedAltitude.setDegrees(125)
        
        result = AL.ApproximateLocation.getDistanceAdjustmentAngle(geographicPositionLatitude, geographicPositionLongitude, assumedLatitude, assumedLongitude, adjustedAltitude)
        self.assertAlmostEqual(expectedResult, result, 2)


#    getAzimuthAdjustment 
#        inputs:
#            geographicPositionLongitude: Angle object        regression
#            geographicPositionLatitude: Angle object        regression
#            assumedLongitude: Angle object        regression
#            assumedLatitude: Angle object        regression
#            adjustedAltitude: Angle object        regression
#            
#        outputs:
#            returns:  Angle object representing distance adjustment                             regression

    def test200_020_ShouldReturnAzimuthAdjustment(self):
        expectedResult = 83.23455
        
        geographicPositionLatitude = Angle.Angle()
        geographicPositionLatitude.setDegrees(200)
        
        geographicPositionLongitude = Angle.Angle()
        geographicPositionLongitude.setDegrees(100)
        
        assumedLatitude = Angle.Angle()
        assumedLatitude.setDegrees(150)
        
        assumedLongitude = Angle.Angle()
        assumedLongitude.setDegrees(50)
    
        
        adjustedAltitude = Angle.Angle()
        adjustedAltitude.setDegrees(125)
        
        result = AL.ApproximateLocation.getAzimuthAdjustmentAngle(geographicPositionLatitude, geographicPositionLongitude, assumedLatitude, assumedLongitude, adjustedAltitude)
        self.assertAlmostEqual(expectedResult, result.getDegrees(), 2)

#  helper methods
    def indexInList(self, target, searchList):
        for index in range(len(searchList)):
            if(target in searchList[index]):
                return index
        return -1
    
    def mapFileToTest(self, target):
        for item in self.testToFileMap:
            if(item[0] == target):
                return item[1]
        return None

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()