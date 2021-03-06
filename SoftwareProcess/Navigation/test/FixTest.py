import unittest
import uuid
import os
import Navigation.prod.Fix as F
import Navigation.prod.Sighting as Sighting
import Navigation.prod.Angle as Angle
import Navigation.prod.LogFile as LogFile
import Navigation.prod.SightingsList as SightingsList
import xml.etree.ElementTree as ET

class TestFix(unittest.TestCase):
    
    def setUp(self):
        self.className = "Fix."
        self.logStartString = "Start of log"
        self.logSightingString = "Start of sighting file"
        
        # set default log file name
        self.DEFAULT_LOG_FILE = "log.txt"
        if(os.path.isfile(self.DEFAULT_LOG_FILE)):
            os.remove(self.DEFAULT_LOG_FILE)
            
        # generate random log file name
        self.RANDOM_LOG_FILE = "log" + str(uuid.uuid4())[-12:] + ".txt"
        
        
        self.fix = F.Fix()
        self.sighting = Sighting.Sighting("BodyName", "2016-03-15", "23:15:01", "60d0.0",  10, 70, 1200, "Natural");
        
        
        self.height_1 = 10
        self.pressure_1 = 1200
        self.temperature_1 = 70
        self.altitude_1 = "60d0.0"
        self.horizon_1 = "natural"
        self.horizon_2 = "artificial"
    

# 100 Constructor
#    Analysis
#        inputs:
#            logFile: string, optional, unvalidated, len >= 1
#        outputs:
#            returns:  instance of Fix
#            also:    writes "Start of log" to log file
#
#    Happy tests:
#        logFile:  
#            omitted  -> Fix()
#            new logfile  -> Fix("randomName.txt")
#            existing logfile  -> Fix("myLog.txt") (assuming myLog.txt exits)
#    Sad tests:
#        logFile:
#            nonstring -> Fix(42)
#            length error -> Fix("")
#            
    def test100_010_ShouldConstructFix(self):
        'Fix.__init__'
        self.assertIsInstance(F.Fix(), F.Fix, 
                              "Major error:  Fix not created")
         
    def test100_020_ShouldConstructFixWithDefaultFile(self):
        theFix = F.Fix()
        try:
            theLogFile = open(self.DEFAULT_LOG_FILE, 'r')
            entry = theLogFile.readline()
            del theLogFile
            self.assertNotEquals(-1, entry.find("Start of log"), 
                                 "Minor:  first line of log is incorrect")
        except IOError:
            self.fail()
        self.assertIsInstance(theFix, F.Fix, 
                              "Major:  log file failed to create")
        
    def test100_025_ShouldConstructWithKeywordParm(self):
        try:
            theFix = F.Fix(logFile=self.RANDOM_LOG_FILE)
            self.assertTrue(True)
        except:
            self.fail("Minor: incorrect keyword specified")
            self.cleanup()
 
         
    def test100_030_ShouldConstructFixWithNamedFile(self):
        theFix = F.Fix(self.RANDOM_LOG_FILE)
        try:
            theLogFile = open(self.RANDOM_LOG_FILE, 'r')
            entry = theLogFile.readline()
            del theLogFile
            self.assertNotEquals(-1, entry.find(self.logStartString), 
                                 "Minor:  first line of log is incorrect")
        except IOError:
            self.fail()
        self.assertIsInstance(theFix, F.Fix, "major:  log file failed to create")
        self.cleanup()  
        
    def test100_040_ShouldConstructFixWithExistingFile(self):
        theFix = F.Fix(self.RANDOM_LOG_FILE)
        theFix = F.Fix(self.RANDOM_LOG_FILE)
        try:
            theLogFile = open(self.RANDOM_LOG_FILE, 'r')
            numberOfExpectedEntries = 2
            for _ in range(numberOfExpectedEntries):
                entry = theLogFile.readline()
                self.assertNotEquals(-1, entry.find(self.logStartString), 
                                     "Minor:  first line of log is incorrect")
            theLogFile.close()
        except IOError:
            self.fail()
        self.assertIsInstance(theFix, F.Fix, 
                              "Major:  log file failed to create")
        self.cleanup()  
        
    def test100_910_ShouldRaiseExceptionOnFileNameLength(self):
        expectedDiag = self.className + "__init__:"
        with self.assertRaises(ValueError) as context:
            F.Fix("")
        self.assertEquals(expectedDiag, context.exception.args[0][0:len(expectedDiag)], 
                          "Minor:  failure to check for log file name length")  
        
    def test100_920_ShouldRaiseExceptionOnNonStringFile(self):
        expectedDiag = self.className + "__init__:"
        with self.assertRaises(ValueError) as context:
            F.Fix(42)
        self.assertEquals(expectedDiag, context.exception.args[0][0:len(expectedDiag)], 
                          "Minor:  failure to check for non-string log file name")  
        
        
# 200 setSightingFile
#    Analysis
#        inputs:
#            sightingFile: string, mandatory, unvalidated, format = f.xml (len(f) >= 1)
#        outputs:
#            returns:  string with file name
#            also:    writes "Start of sighting file f.xml" to log file
#
#    Happy tests:
#        sightingFile:  
#            legal file name  -> setSightingFile("sightingFile.xml")  
#    Sad tests:
#        sightingFile:
#            nonstring -> setSightinghFile(42)
#            length error -> setSightingFile(".xml")
#            nonXML -> setSightingFile("sightingFile.txt")
#            missing -> setSightingFile()
#            nonexistent file -> setSightingFile("missing.xml")
    def test200_010_ShouldConstructWithKeywordParm(self):
        'Minor:  '
        theFix = F.Fix(logFile=self.RANDOM_LOG_FILE)
        try:
            result = theFix.setSightingFile("CA02_200_ValidStarSightingFile.xml")
            self.assertEquals(result, "CA02_200_ValidStarSightingFile.xml")
        except:
            self.fail("Minor: incorrect keyword specified in setSighting parm")
        self.cleanup()   

    def test200_020_ShouldSetValidSightingFile(self):
        theFix = F.Fix()
        result = theFix.setSightingFile("CA02_200_ValidStarSightingFile.xml")
        self.assertEquals(result,"CA02_200_ValidStarSightingFile.xml")
        theLogFile = open(self.DEFAULT_LOG_FILE, "r")
        logFileContents = theLogFile.readlines()
        self.assertNotEquals(-1, logFileContents[-1].find(self.logSightingString), 
                             "Minor:  first setSighting logged entry is incorrect")
        theLogFile.close()
        
    def test200_910_ShouldRaiseExceptionOnNonStringFileName(self):
        expectedDiag = self.className + "setSightingFile:"
        theFix = F.Fix()
        with self.assertRaises(ValueError) as context:
            theFix.setSightingFile(42)
        self.assertEquals(expectedDiag, context.exception.args[0][0:len(expectedDiag)],
                          "Minor:  failure to check for non-string sighting file name")  
        
    def test200_920_ShouldRaiseExceptionOnFileLengthError(self):
        expectedDiag = self.className + "setSightingFile:"
        theFix = F.Fix()
        with self.assertRaises(ValueError) as context:
            theFix.setSightingFile(".xml")
        self.assertEquals(expectedDiag, context.exception.args[0][0:len(expectedDiag)],
                          "Minor:  failure to check for .GE. 1 sighting file name") 
        
    def test200_930_ShouldRaiseExceptionOnNonXmlFile1(self):
        expectedDiag = self.className + "setSightingFile:"
        theFix = F.Fix()
        with self.assertRaises(ValueError) as context:
            theFix.setSightingFile("sighting.")
        self.assertEquals(expectedDiag, context.exception.args[0][0:len(expectedDiag)],
                          "Minor:  failure to check for non.xml sighting file extension")
        
    def test200_940_ShouldRaiseExceptionOnNonXmlFile2(self):
        expectedDiag = self.className + "setSightingFile:"
        theFix = F.Fix()
        with self.assertRaises(ValueError) as context:
            theFix.setSightingFile("xml")
        self.assertEquals(expectedDiag, context.exception.args[0][0:len(expectedDiag)],
                          "Minor:  failure to delineate between sighting file name and extension") 
        
    def test200_950_SholdRaiseExceptionOnMissingFileName(self):
        expectedDiag = self.className + "setSightingFile:"
        theFix = F.Fix()
        with self.assertRaises(ValueError) as context:
            theFix.setSightingFile()
        self.assertEquals(expectedDiag, context.exception.args[0][0:len(expectedDiag)],
                          "Major:  failure to check for missing sighting file")       
        
           
    def test200_960_SholdRaiseExceptionOnMissingFile(self):
        expectedDiag = self.className + "setSightingFile:"
        theFix = F.Fix()
        with self.assertRaises(ValueError) as context:
            theFix.setSightingFile(self.RANDOM_LOG_FILE+".xml")
        self.assertEquals(expectedDiag, context.exception.args[0][0:len(expectedDiag)],
                          "Major:  failure to check for missing sighting file") 
        
# 300 getSightings
#    Analysis
#        inputs:
#            via parm:  none
#            via file:  xml description of sighting
#        outputs:
#            returns:    ("0d0.0", "0d0.0")
#            via file:    writes body /t date /t time /t adjusted altitude in sorted order
#        entry criterion:
#            setSightingsFile must be called first
#
#    Happy tests:
#        sighting file 
#            valid file with any sightings -> should return ("0d0.0", "0d0.0")
#            valid file with mixed indentation -> should not indicate any errors
#            valid file with one sighting  -> should log one star body
#            valid file with multiple sightings -> should log star bodies in sorted order
#            valid file with multiple sightings at same date/time -> should log star bodies in order sorted by body 
#            valid file with zero sightings -> should not log any star bodies
#            valid file with extraneous tag -> should log star(s) without problem
#        sighting file contents
#            valid body with natural horizon -> should calculate altitude with dip
#            valid body with artificial horizon -> should calculate altitude without dip
#            valid body with default values -> should calculate altitude with height=0, temperature=72, pressure=1010, horizon-natural
#    Sad tests:
#        sightingFile:
#            sighting file not previously set
#            sighting file with invalid mandatory tag (one of each:  fix, body, date, time, observation)
#            sighting file with invalid tag value (one of each:  date, time, observation, height, temperature, pressure, horizon)

    def test300_010_ShouldIgnoreMixedIndentation(self):
        testFile = "CA02_300_GenericValidStarSightingFile.xml"
        expectedResult = ("0d0.0", "0d0.0")
        theFix = F.Fix()
        theFix.setSightingFile(testFile)
        result = theFix.getSightings()
        self.assertTupleEqual(expectedResult, result, 
                              "Minor:  incorrect return value from getSightings")

    def test300_020_ShouldIgnoreMixedIndentation(self):
        testFile = "CA02_300_ValidWithMixedIndentation.xml"
        theFix = F.Fix()
        theFix.setSightingFile(testFile)
        try:
            theFix.getSightings()
            self.assertTrue(True)
        except:
            self.fail("Major: getSightings failed on valid file with mixed indentation")  

    def test300_030_ShouldLogOneSighting(self):
        testFile = "CA02_300_ValidOneStarSighting.xml"
        targetStringList = ["Aldebaran", "2016-03-01", "23:40:01"]
        theFix = F.Fix(self.RANDOM_LOG_FILE)
        theFix.setSightingFile(testFile)
        theFix.getSightings()
        
        theLogFile = open(self.RANDOM_LOG_FILE, "r")
        logFileContents = theLogFile.readlines()
        theLogFile.close()
        
        sightingCount = 0
        for logEntryNumber in range(0, len(logFileContents)):
            if(logFileContents[logEntryNumber].find(targetStringList[0]) > -1):
                sightingCount += 1
                for target in targetStringList:
                    self.assertNotEquals(-1, logFileContents[logEntryNumber].find(target), 
                                         "Major:  Log entry is not correct for getSightings")
        self.assertEquals(1, sightingCount)
        self.cleanup()  
        
    def test300_040_ShouldLogMultipleSightingsInTimeOrder(self):       
        testFile = "CA02_300_ValidMultipleStarSighting.xml"
        targetStringList = [
            ["Sirius", "2016-03-01", "00:05:05"],
            ["Canopus", "2016-03-02", "23:40:01"]
            ]
        theFix = F.Fix(self.RANDOM_LOG_FILE)
        theFix.setSightingFile(testFile)
        theFix.getSightings()
        
        theLogFile = open(self.RANDOM_LOG_FILE, "r")
        logFileContents = theLogFile.readlines()
        theLogFile.close()
        
        # find entry with first star
        entryIndex = self.indexInList(targetStringList[0][0], logFileContents)
        self.assertLess(-1, entryIndex, 
                           "failure to find " + targetStringList[0][0] +  " in log")
        for index in range(entryIndex+1, len(targetStringList)):
            entryIndex += 1
            if(not(targetStringList[index][0] in logFileContents[entryIndex])):
                self.fail("failure to find star in log")
        self.cleanup()  

    def test300_050_ShouldLogMultipleSightingsWithSameDateTime(self):       
        testFile = "CA02_300_ValidMultipleStarSightingSameDateTime.xml"
        targetStringList = [
            ["Acrux", "2016-03-01", "00:05:05"],
            ["Sirius", "2016-03-01", "00:05:05"],
            ["Canopus", "2016-03-02", "23:40:01"]
            ]
        theFix = F.Fix(self.RANDOM_LOG_FILE)
        theFix.setSightingFile(testFile)
        theFix.getSightings()
        
        theLogFile = open(self.RANDOM_LOG_FILE, "r")
        logFileContents = theLogFile.readlines()
        theLogFile.close()
        
        # find entry with first star
        entryIndex = self.indexInList(targetStringList[0][0], logFileContents)
        self.assertLess(-1, entryIndex, 
                           "failure to find " + targetStringList[0][0] +  " in log")
        for index in range(entryIndex+1, len(targetStringList)):
            entryIndex += 1
            if(not(targetStringList[index][0] in logFileContents[entryIndex])):
                self.fail("failure to find star in log")
        self.cleanup()   

    def test300_060_ShouldHandleNoSightings(self):       
        testFile = "CA02_300_ValidWithNoSightings.xml"
        targetString1 = "End of sighting file"
        targetString2 = "Start of sighting file"
        
        theFix = F.Fix(self.RANDOM_LOG_FILE)
        theFix.setSightingFile(testFile)
        theFix.getSightings()
        
        theLogFile = open(self.RANDOM_LOG_FILE, "r")
        logFileContents = theLogFile.readlines()
        theLogFile.close()
        
        endOfSightingFileIndex = self.indexInList(targetString1, logFileContents)
        self.assertLess(-1,endOfSightingFileIndex,
                           "log file does not contain 'end of sighting file' entry")
        self.assertLess(1, endOfSightingFileIndex,
                           "log file does not contain sufficient entries")
        self.assertTrue((targetString2 in logFileContents[endOfSightingFileIndex - 1]))
        self.cleanup()   
        
    def test300_070_ShouldIgnoreExtraneousTags(self):       
        testFile = "CA02_300_ValidWithExtraneousTags.xml"
        targetStringList = [
            ["Sirius", "2016-03-01", "00:05:05"],
            ]
        theFix = F.Fix(self.RANDOM_LOG_FILE)
        theFix.setSightingFile(testFile)
        theFix.getSightings()
        
        theLogFile = open(self.RANDOM_LOG_FILE, "r")
        logFileContents = theLogFile.readlines()
        theLogFile.close()
        
        # find entry with first star
        entryIndex = self.indexInList(targetStringList[0][0], logFileContents)
        self.assertLess(-1, entryIndex, 
                           "failure to find " + targetStringList[0][0] +  " in log")
        for index in range(entryIndex+1, len(targetStringList)):
            entryIndex += 1
            if(not(targetStringList[index][0] in logFileContents[entryIndex])):
                self.fail("failure to find star in log")
        self.cleanup()    


    def test300_080_ShouldLogStarWithNaturalHorizon(self):
        testFile = "CA02_300_ValidOneStarNaturalHorizon.xml"
        targetStringList = ["Hadar", "2016-03-01", "23:40:01", "29d55.7"]
        theFix = F.Fix(self.RANDOM_LOG_FILE)
        theFix.setSightingFile(testFile)
        theFix.getSightings()
        
        theLogFile = open(self.RANDOM_LOG_FILE, "r")
        logFileContents = theLogFile.readlines()
        theLogFile.close()
        
        sightingCount = 0
        for logEntryNumber in range(0, len(logFileContents)):
            if(logFileContents[logEntryNumber].find(targetStringList[0]) > -1):
                sightingCount += 1
                for target in targetStringList:
                    self.assertNotEquals(-1, logFileContents[logEntryNumber].find(target), 
                                         "Major:  Log entry is not correct for getSightings")
        self.assertEquals(1, sightingCount)
        self.cleanup()  


    def test300_080_ShouldLogStarWithArtificialHorizon(self):
        testFile = "CA02_300_ValidOneStarArtificialHorizon.xml"
        targetStringList = ["Hadar", "2016-03-01", "23:40:01", "29d55.7"]
        theFix = F.Fix(self.RANDOM_LOG_FILE)
        theFix.setSightingFile(testFile)
        theFix.getSightings()
        
        theLogFile = open(self.RANDOM_LOG_FILE, "r")
        logFileContents = theLogFile.readlines()
        theLogFile.close()
        
        sightingCount = 0
        for logEntryNumber in range(0, len(logFileContents)):
            if(logFileContents[logEntryNumber].find(targetStringList[0]) > -1):
                sightingCount += 1
                for target in targetStringList:
                    self.assertNotEquals(-1, logFileContents[logEntryNumber].find(target), 
                                         "Major:  Log entry is not correct for getSightings")
        self.assertEquals(1, sightingCount)
        self.cleanup()  
        
        
    def test300_090_ShouldLogStarWithDefaultSightingValues(self):
        testFile = "CA02_300_ValidOneStarWithDefaultValues.xml"
        targetStringList = ["Hadar", "2016-03-01", "23:40:01", "29d59.9"]
        theFix = F.Fix(self.RANDOM_LOG_FILE)
        theFix.setSightingFile(testFile)
        theFix.getSightings()
        
        theLogFile = open(self.RANDOM_LOG_FILE, "r")
        logFileContents = theLogFile.readlines()
        theLogFile.close()
        
        sightingCount = 0
        for logEntryNumber in range(0, len(logFileContents)):
            if(logFileContents[logEntryNumber].find(targetStringList[0]) > -1):
                sightingCount += 1
                for target in targetStringList:
                    self.assertNotEquals(-1, logFileContents[logEntryNumber].find(target), 
                                         "Major:  Log entry is not correct for getSightings")
        self.assertEquals(1, sightingCount)
        self.cleanup()  

    def test300_910_ShouldRaiseExceptionOnNotSettingSightingsFile(self):
        expectedDiag = self.className + "getSightings:"
        theFix = F.Fix()
        with self.assertRaises(ValueError) as context:
            theFix.getSightings()
        self.assertEquals(expectedDiag, context.exception.args[0][0:len(expectedDiag)],
                          "Major:  failure to set sighting file before getSightings()")   
        
    def test300_920_ShouldRaiseExceptionOnMissingMandatoryTag(self):
        expectedDiag = self.className + "getSightings:"
        theFix = F.Fix()
        with self.assertRaises(ValueError) as context:
            theFix.setSightingFile("CA02_300_InvalidWithMissingMandatoryTags.xml")
            theFix.getSightings()
        self.assertEquals(expectedDiag, context.exception.args[0][0:len(expectedDiag)],
                          "Major:  failure to check for missing mandatory tag")   
        
    def test300_930_ShouldRaiseExceptionOnInvalidBody(self):
        expectedDiag = self.className + "getSightings:"
        theFix = F.Fix()
        with self.assertRaises(ValueError) as context:
            theFix.setSightingFile("CA02_300_InvalidBody.xml")
            theFix.getSightings()
        self.assertEquals(expectedDiag, context.exception.args[0][0:len(expectedDiag)],
                          "Major:  failure to check for invalid body")    
        
    def test300_940_ShouldRaiseExceptionOnInvalidDate(self):
        expectedDiag = self.className + "getSightings:"
        theFix = F.Fix()
        with self.assertRaises(ValueError) as context:
            theFix.setSightingFile("CA02_300_InvalidDate.xml")
            theFix.getSightings()
        self.assertEquals(expectedDiag, context.exception.args[0][0:len(expectedDiag)],
                          "Major:  failure to check for invalid body") 
        
    def test300_950_ShouldRaiseExceptionOnInvalidTime(self):
        expectedDiag = self.className + "getSightings:"
        theFix = F.Fix()
        with self.assertRaises(ValueError) as context:
            theFix.setSightingFile("CA02_300_InvalidTime.xml")
            theFix.getSightings()
        self.assertEquals(expectedDiag, context.exception.args[0][0:len(expectedDiag)],
                          "Major:  failure to check for invalid body")    
        
    def test300_960_ShouldRaiseExceptionOnInvalidObservation(self):
        expectedDiag = self.className + "getSightings:"
        theFix = F.Fix()
        with self.assertRaises(ValueError) as context:
            theFix.setSightingFile("CA02_300_InvalidObservation.xml")
            theFix.getSightings()
        self.assertEquals(expectedDiag, context.exception.args[0][0:len(expectedDiag)],
                          "Major:  failure to check for invalid body")       
        
    def test300_970_ShouldRaiseExceptionOnInvalidHeight(self):
        expectedDiag = self.className + "getSightings:"
        theFix = F.Fix()
        with self.assertRaises(ValueError) as context:
            theFix.setSightingFile("CA02_300_InvalidHeight.xml")
            theFix.getSightings()
        self.assertEquals(expectedDiag, context.exception.args[0][0:len(expectedDiag)],
                          "Major:  failure to check for invalid body" )
        
    def test300_980_ShouldRaiseExceptionOnInvalidTemperature(self):
        expectedDiag = self.className + "getSightings:"
        theFix = F.Fix()
        with self.assertRaises(ValueError) as context:
            theFix.setSightingFile("CA02_300_InvalidTemperature.xml")
            theFix.getSightings()
        self.assertEquals(expectedDiag, context.exception.args[0][0:len(expectedDiag)],
                          "Major:  failure to check for invalid body" )
        
    def test300_990_ShouldRaiseExceptionOnInvalidPressure(self):
        expectedDiag = self.className + "getSightings:"
        theFix = F.Fix()
        with self.assertRaises(ValueError) as context:
            theFix.setSightingFile("CA02_300_InvalidPressure.xml")
            theFix.getSightings()
        self.assertEquals(expectedDiag, context.exception.args[0][0:len(expectedDiag)],
                          "Major:  failure to check for invalid body" )
        
    def test300_995_ShouldRaiseExceptionOnInvalidHorizon(self):
        expectedDiag = self.className + "getSightings:"
        theFix = F.Fix()
        with self.assertRaises(ValueError) as context:
            theFix.setSightingFile("CA02_300_InvalidHorizon.xml")
            theFix.getSightings()
        self.assertEquals(expectedDiag, context.exception.args[0][0:len(expectedDiag)],
                          "Major:  failure to check for invalid body" )
        
               


    

#  helper methods
    def indexInList(self, target, searchList):
        for index in range(len(searchList)):
            if(target in searchList[index]):
                return index
        return -1
    
    def cleanup(self):
        if(os.path.isfile(self.RANDOM_LOG_FILE)):
            os.remove(self.RANDOM_LOG_FILE)  
            
            
            
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
        self.assertAlmostEqual(adjustedAltitude, 59.93822, 3)

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
        self.assertAlmostEqual(dip, -.05112, 3)


    def test410_020_CalculateDipWithArtificial(self):
        dip = self.sighting._calculateDip(self.height_1, self.horizon_2)
        self.assertEqual(dip, 0)

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
#                nominal case: _CalculateRefraction()
#            Sad path
#                none

    def test420_010_CalculateRefraction(self):
        altitudeAngle = Angle.Angle()
        altitudeAngle.setDegreesAndMinutes(self.altitude_1)
        refraction = self.sighting._calculateRefraction(self.pressure_1, self.temperature_1, altitudeAngle)
        # Calculated by hand
        self.assertAlmostEqual(refraction, -.0106475, 5)
        
        
    
#500s will be used for SightingsList    
    
#    Unit Test: 500_010
#        Analysis - Constructor and getSightingsList
#            inputs
#                filename
#            outputs
#                none
#            state change
#                none
#
#            Happy path
#                nominal case: SightingsList()
#            Sad path
#                File does not exist

    def test500_010_CreateSightingsList(self):
        sightingsListObject = SightingsList.SightingsList("sightingFile.xml")
        sightingList = sightingsListObject.getSightingsList()
        self.assertEqual(len(sightingList), 2)
        
#    Unit Test: 510_010
#        Analysis - _extractSighting
#            inputs
#                xml node
#            outputs
#                Sighting object
#            state change
#                none
#
#            Happy path
#                nominal case: _extractSighting()
#            Sad path
#                none, already validated

    def test510_010_ShouldCreateSighting(self):
        sightingsListObject = SightingsList.SightingsList("sightingFile.xml")
        XMLDOM = ET.parse("../Resources/sightingFile.xml")
        fix = XMLDOM.getroot()
        sightings = []
        for sighting in fix:
            sightings.append(sightingsListObject._extractSighting(sighting))
        for sighting in sightings:
            self.assertIsInstance(sighting, Sighting.Sighting)
        pass
    
    
#600s will be used for logFile    
    
#    Unit Test: 600_010
#        Analysis - Constructor
#            inputs
#                filename - optional
#            outputs
#                none
#            state change
#                change to log file or creation of log file
#
#            Happy path
#                nominal case: LogFile()
#            Sad path
#                bad filename

    def test600_010_ShouldModifyLogFile(self):
        logFile = LogFile.LogFile("test.txt")
        self.assertIsInstance(logFile, LogFile.LogFile)
        self.assertTrue(os.path.isfile('../Resources/' + 'test.txt'))
        pass
        
    def test600_910_BadFileName(self):
        with self.assertRaises(ValueError):
            LogFile.LogFile("test.txsdft")

#    Unit Test: 610_010
#        Analysis - Write To log
#            inputs
#                filename - optional
#            outputs
#                none
#            state change
#                Log has a new entry
#
#            Happy path
#                nominal case: writeToLogEntry()
#            Sad path
#                bad filename

# I have not thought of an easy way to test these types of things. I can always parse the file looking for the new entry, 
# but this might be something i implement at a future date
# also, if 600_010_SHouldModifyLogFile() doesn't break, it is likely that this worked as most likely a value error would occur if not