'''
Created on Dec 2, 2016

@author: Aaron
'''
import unittest
import uuid
import os
import Navigation.prod.Fix as F


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


#==================== Fix.__init__ ====================
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
#            test 020:    Parameters at 0d0.0        CA03
#            test 030:    north hemisphere                
#            test 040:    south hemisphere        CA03
#            test 050:    correct number of sightings
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

    def test300_010_ShouldReceiveEmptyParameters(self):
        'parse sighting file that valid tags'
        testFile = self.mapFileToTest("genericValidStarSightingFile")
        #expectedResult = ("0d0.0", "0d0.0")
        theFix = F.Fix()
        theFix.setSightingFile(testFile)
        theFix.setStarFile(self.starFileName)
        theFix.setAriesFile(self.ariesFileName)
        result = theFix.getSightings()
        


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