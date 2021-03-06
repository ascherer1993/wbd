'''
Created on Oct 30, 2016

@author: Aaron
'''
import unittest
import uuid
import os
import Navigation.prod.Fix as F
import Navigation.prod.Sighting as Sighting
import Navigation.prod.Angle as Angle
import Navigation.prod.LogFile as LogFile
import Navigation.prod.SightingsList as SightingsList
import Navigation.prod.AriesEntriesList as AriesEntriesList
import Navigation.prod.StarsList as StarsList
import Navigation.prod.AriesEntry as AriesEntry
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
        
    #  helper methods
    def indexInList(self, target, searchList):
        for index in range(len(searchList)):
            if(target in searchList[index]):
                return index
        return -1
    
    def cleanup(self):
        if(os.path.isfile(self.RANDOM_LOG_FILE)):
            os.remove(self.RANDOM_LOG_FILE)  


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
            expectedPath = 'D:\\Documents\\Programming\\Eclipse Repositories\\SoftwareProcess\\SoftwareProcess\\Navigation\\Resources\\CA02_200_ValidStarSightingFile.xml'
            result = theFix.setSightingFile("CA02_200_ValidStarSightingFile.xml")
            self.assertEquals(result, expectedPath)
        except:
            self.fail("Minor: incorrect keyword specified in setSighting parm")
        self.cleanup()   

    def test200_020_ShouldSetValidSightingFile(self):
        theFix = F.Fix()
        expectedPath = 'D:\\Documents\\Programming\\Eclipse Repositories\\SoftwareProcess\\SoftwareProcess\\Navigation\\Resources\\CA02_200_ValidStarSightingFile.xml'
        result = theFix.setSightingFile("CA02_200_ValidStarSightingFile.xml")
        self.assertEquals(result, expectedPath)
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
        theFix.setAriesFile("aries.txt")
        theFix.setStarFile('stars.txt')
        result = theFix.getSightings()
        self.assertTupleEqual(expectedResult, result, 
                              "Minor:  incorrect return value from getSightings")

    def test300_020_ShouldIgnoreMixedIndentation(self):
        testFile = "CA02_300_ValidWithMixedIndentation.xml"
        theFix = F.Fix()
        theFix.setSightingFile(testFile)
        theFix.setAriesFile("aries.txt")
        theFix.setStarFile('stars.txt')
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
        theFix.setAriesFile("aries.txt")
        theFix.setStarFile('stars.txt')
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
#         self.assertEquals(1, sightingCount)
        self.cleanup()  
        
    def test300_040_ShouldLogMultipleSightingsInTimeOrder(self):       
        testFile = "CA02_300_ValidMultipleStarSighting.xml"
        targetStringList = [
            ["Sirius", "2016-03-01", "00:05:05"],
            ["Canopus", "2016-03-02", "23:40:01"]
            ]
        theFix = F.Fix(self.RANDOM_LOG_FILE)
        theFix.setSightingFile(testFile)
        theFix.setAriesFile("aries.txt")
        theFix.setStarFile('stars.txt')
        theFix.getSightings()
        
        theLogFile = open(self.RANDOM_LOG_FILE, "r")
        logFileContents = theLogFile.readlines()
        theLogFile.close()
        
        # find entry with first star
        entryIndex = self.indexInList(targetStringList[0][0], logFileContents)
#         self.assertLess(-1, entryIndex, 
#                            "failure to find " + targetStringList[0][0] +  " in log")
#         for index in range(entryIndex+1, len(targetStringList)):
#             entryIndex += 1
#             if(not(targetStringList[index][0] in logFileContents[entryIndex])):
#                 self.fail("failure to find star in log")
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
        theFix.setAriesFile("aries.txt")
        theFix.setStarFile('stars.txt')
        theFix.getSightings()
        
        theLogFile = open(self.RANDOM_LOG_FILE, "r")
        logFileContents = theLogFile.readlines()
        theLogFile.close()
        
        # find entry with first star
        entryIndex = self.indexInList(targetStringList[0][0], logFileContents)
#         self.assertLess(-1, entryIndex, 
#                            "failure to find " + targetStringList[0][0] +  " in log")
#         for index in range(entryIndex+1, len(targetStringList)):
#             entryIndex += 1
#             if(not(targetStringList[index][0] in logFileContents[entryIndex])):
#                 self.fail("failure to find star in log")
        self.cleanup()   

    def test300_060_ShouldHandleNoSightings(self):       
        testFile = "CA02_300_ValidWithNoSightings.xml"
        targetString1 = "End of sighting file"
        targetString2 = "Start of sighting file"
        targetString3 = "Aries file:"
        targetString4 = "Star file:"
        
        theFix = F.Fix(self.RANDOM_LOG_FILE)
        theFix.setSightingFile(testFile)
        theFix.setAriesFile("aries.txt")
        theFix.setStarFile('stars.txt')
        theFix.getSightings()
        
        theLogFile = open(self.RANDOM_LOG_FILE, "r")
        logFileContents = theLogFile.readlines()
        theLogFile.close()
        
        endOfSightingFileIndex = self.indexInList(targetString1, logFileContents)
        self.assertLess(-1,endOfSightingFileIndex,
                           "log file does not contain 'end of sighting file' entry")
        self.assertLess(1, endOfSightingFileIndex,
                           "log file does not contain sufficient entries")
#         self.assertTrue((targetString2 in logFileContents[endOfSightingFileIndex - 3]))
#         self.assertTrue((targetString3 in logFileContents[endOfSightingFileIndex - 2]))
#         self.assertTrue((targetString4 in logFileContents[endOfSightingFileIndex - 1]))
        self.cleanup()   
        
    def test300_070_ShouldIgnoreExtraneousTags(self):       
        testFile = "CA02_300_ValidWithExtraneousTags.xml"
        targetStringList = [
            ["Sirius", "2016-03-01", "00:05:05"],
            ]
        theFix = F.Fix(self.RANDOM_LOG_FILE)
        theFix.setSightingFile(testFile)
        theFix.setAriesFile("aries.txt")
        theFix.setStarFile('stars.txt')
        theFix.getSightings()
        
        theLogFile = open(self.RANDOM_LOG_FILE, "r")
        logFileContents = theLogFile.readlines()
        theLogFile.close()
        
        # find entry with first star
        entryIndex = self.indexInList(targetStringList[0][0], logFileContents)
#         self.assertLess(-1, entryIndex, 
#                            "failure to find " + targetStringList[0][0] +  " in log")
        for index in range(entryIndex+1, len(targetStringList)):
            entryIndex += 1
#             if(not(targetStringList[index][0] in logFileContents[entryIndex])):
#                 self.fail("failure to find star in log")
        self.cleanup()    


    def test300_080_ShouldLogStarWithNaturalHorizon(self):
        testFile = "CA02_300_ValidOneStarNaturalHorizon.xml"
        targetStringList = ["Hadar", "2016-03-01", "23:40:01", "29d55.7"]
        theFix = F.Fix(self.RANDOM_LOG_FILE)
        theFix.setSightingFile(testFile)
        theFix.setAriesFile("aries.txt")
        theFix.setStarFile('stars.txt')
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
        #self.assertEquals(1, sightingCount)
        self.cleanup()  


    def test300_080_ShouldLogStarWithArtificialHorizon(self):
        testFile = "CA02_300_ValidOneStarArtificialHorizon.xml"
        targetStringList = ["Hadar", "2016-03-01", "23:40:01", "29d55.7"]
        theFix = F.Fix(self.RANDOM_LOG_FILE)
        theFix.setSightingFile(testFile)
        theFix.setAriesFile("aries.txt")
        theFix.setStarFile('stars.txt')
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
        #self.assertEquals(1, sightingCount)
        self.cleanup()  
        
        
    def test300_090_ShouldLogStarWithDefaultSightingValues(self):
        testFile = "CA02_300_ValidOneStarWithDefaultValues.xml"
        targetStringList = ["Hadar", "2016-03-01", "23:40:01", "29d59.9"]
        theFix = F.Fix(self.RANDOM_LOG_FILE)
        theFix.setSightingFile(testFile)
        theFix.setAriesFile("aries.txt")
        theFix.setStarFile('stars.txt')
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
        #self.assertEquals(1, sightingCount)
        self.cleanup()  

    def test300_100_ShouldWriteAltitudeAndPositionToLogFile(self):
        #chedar    01/01/17    349d38.4    56d37.7

        testFile = "CA03_300_CheckCalculatedAngles.xml"
        #9d59.9
        #sha 349d38.4 + 7d31.2
        #
        targetStringList = ["Schedar", "2017-01-01", "02:30:00", "9d54.7", "56d37.7", "357d9.6"]
        if os.path.isfile("CA03AngleWriting.txt"): 
            os.remove("CA03AngleWriting.txt") 
        theFix = F.Fix("CA03AngleWriting.txt")
        theFix.setSightingFile(testFile)
        theFix.setAriesFile("aries.txt")
        theFix.setStarFile('stars.txt')
        theFix.getSightings()
        
        theLogFile = open("CA03AngleWriting.txt", "r")
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
        pass

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
        


# 400 setAriesFile
#    Analysis
#        inputs:
#            AriesFile: string, mandatory, unvalidated, format = f.txt (len(f) >= 1)
#        outputs:
#            returns:  string with file path
#            also:    writes "Aries file: /filepath/" to log file
#
#    Happy tests:
#        ariesFile:  
#            legal file name  -> setAriesFile("ariesFile.txt")  
#    Sad tests:
#        ariesFile:
#            nonstring -> setSightinghFile(42)
#            length error -> setSightingFile(".xml")
#            nontxt -> setSightingFile("sightingFile.txt")
#            missing -> setSightingFile()
#            nonexistent file -> setSightingFile("missing.xml")
    def test400_010_ShouldConstructWithKeywordParm(self):
        'Minor:  '
        theFix = F.Fix(logFile=self.RANDOM_LOG_FILE)
        try:
            expectedPath = 'D:\\Documents\\Programming\\Eclipse Repositories\\SoftwareProcess\\SoftwareProcess\\Navigation\\Resources\\aries.txt'
            result = theFix.setAriesFile("aries.txt")
            self.assertEquals(result, expectedPath)
        except:
            self.fail("Minor: incorrect keyword specified in setStar parm")
        self.cleanup()   

    def test400_020_ShouldSetValidAriesFile(self):
        theFix = F.Fix()
        expectedPath = 'D:\\Documents\\Programming\\Eclipse Repositories\\SoftwareProcess\\SoftwareProcess\\Navigation\\Resources\\aries.txt'
        result = theFix.setAriesFile("aries.txt")
        self.assertEquals(result, expectedPath)
        theAriesFile = open("../Resources/aries.txt", "r")
        ariesFileContents = theAriesFile.readlines()
        self.assertNotEquals(-1, ariesFileContents[0].find("01/01/17\t0\t100d05.4\n"), 
                             "Minor:  first aries entry is incorrect")
        theAriesFile.close()
        
    def test400_910_ShouldRaiseExceptionOnNonStringFileName(self):
        expectedDiag = self.className + "setAriesFile:"
        theFix = F.Fix()
        with self.assertRaises(ValueError) as context:
            theFix.setAriesFile(42)
        self.assertEquals(expectedDiag, context.exception.args[0][0:len(expectedDiag)],
                          "Minor:  failure to check for non-string aries file name")
        pass  
        
    def test400_920_ShouldRaiseExceptionOnFileLengthError(self):
        expectedDiag = self.className + "setAriesFile:"
        theFix = F.Fix()
        with self.assertRaises(ValueError) as context:
            theFix.setAriesFile(".txt")
        self.assertEquals(expectedDiag, context.exception.args[0][0:len(expectedDiag)],
                          "Minor:  failure to check for .GE. 1 aries file name") 
        pass
    
    def test400_930_ShouldRaiseExceptionOnNonTxtFile1(self):
        expectedDiag = self.className + "setAriesFile:"
        theFix = F.Fix()
        with self.assertRaises(ValueError) as context:
            theFix.setAriesFile("sighting.")
        self.assertEquals(expectedDiag, context.exception.args[0][0:len(expectedDiag)],
                          "Minor:  failure to check for non.txt aries file extension")
        pass
        
    def test400_940_ShouldRaiseExceptionOnNonTxtFile2(self):
        expectedDiag = self.className + "setAriesFile:"
        theFix = F.Fix()
        with self.assertRaises(ValueError) as context:
            theFix.setAriesFile("txt")
        self.assertEquals(expectedDiag, context.exception.args[0][0:len(expectedDiag)],
                          "Minor:  failure to delineate between aries file name and extension") 
        pass
        
    def test400_950_SholdRaiseExceptionOnMissingFileName(self):
        expectedDiag = self.className + "setAriesFile:"
        theFix = F.Fix()
        with self.assertRaises(ValueError) as context:
            theFix.setAriesFile()
        self.assertEquals(expectedDiag, context.exception.args[0][0:len(expectedDiag)],
                          "Major:  failure to check for missing aries file")       
        pass
        
           
    def test400_960_SholdRaiseExceptionOnMissingFile(self):
        expectedDiag = self.className + "setAriesFile:"
        theFix = F.Fix()
        with self.assertRaises(ValueError) as context:
            theFix.setAriesFile(self.RANDOM_LOG_FILE+".txt")
        self.assertEquals(expectedDiag, context.exception.args[0][0:len(expectedDiag)],
                          "Major:  failure to check for missing aries file") 
        pass

# 500 setStarFile
#    Analysis
#        inputs:
#            AriesFile: string, mandatory, unvalidated, format = f.txt (len(f) >= 1)
#        outputs:
#            returns:  string with file path
#            also:    writes "starFile: /path/" to log file
#
#    Happy tests:
#        starFile:  
#            legal file name  -> setStarFile("starFile.txt")  
#    Sad tests:
#        starFile:
#            nonstring -> setStarFile(42)
#            length error -> setStarFile(".txt")
#            nonXML -> setStarFile("starFile.txt")
#            missing -> setStarFile()
#            nonexistent file -> setStarFile("missing.txt")
    def test500_010_ShouldConstructWithKeywordParm(self):
        'Minor:  '
        theFix = F.Fix(logFile=self.RANDOM_LOG_FILE)
        try:
            expectedPath = 'D:\\Documents\\Programming\\Eclipse Repositories\\SoftwareProcess\\SoftwareProcess\\Navigation\\Resources\\stars.txt'
            result = theFix.setStarFile("stars.txt")
            self.assertEquals(result, expectedPath)
        except:
            self.fail("Minor: incorrect keyword specified in setStar parm")
        self.cleanup()   

    def test500_020_ShouldSetValidStarFile(self):
        theFix = F.Fix()
        expectedPath = 'D:\\Documents\\Programming\\Eclipse Repositories\\SoftwareProcess\\SoftwareProcess\\Navigation\\Resources\\stars.txt'
        result = theFix.setStarFile("stars.txt")
        self.assertEquals(result, expectedPath)
        theStarFile = open("../Resources/stars.txt", "r")
        starFileContents = theStarFile.readlines()
        self.assertNotEquals(-1, starFileContents[0].find("Alpheratz\t01/01/17\t357d41.7\t29d10.9\n"), 
                             "Minor:  first setStar entry is incorrect")
        theStarFile.close()
        
    def test500_910_ShouldRaiseExceptionOnNonStringFileName(self):
        expectedDiag = self.className + "setStarFile:"
        theFix = F.Fix()
        with self.assertRaises(ValueError) as context:
            theFix.setStarFile(42)
        self.assertEquals(expectedDiag, context.exception.args[0][0:len(expectedDiag)],
                          "Minor:  failure to check for non-string star file name")
        pass  
        
    def test500_920_ShouldRaiseExceptionOnFileLengthError(self):
        expectedDiag = self.className + "setStarFile:"
        theFix = F.Fix()
        with self.assertRaises(ValueError) as context:
            theFix.setStarFile(".txt")
        self.assertEquals(expectedDiag, context.exception.args[0][0:len(expectedDiag)],
                          "Minor:  failure to check for .GE. 1 star file name") 
        pass
    
    def test500_930_ShouldRaiseExceptionOnNonTxtFile1(self):
        expectedDiag = self.className + "setStarFile:"
        theFix = F.Fix()
        with self.assertRaises(ValueError) as context:
            theFix.setStarFile("stars.")
        self.assertEquals(expectedDiag, context.exception.args[0][0:len(expectedDiag)],
                          "Minor:  failure to check for non.txt star file extension")
        pass
        
    def test500_940_ShouldRaiseExceptionOnNonTxtFile2(self):
        expectedDiag = self.className + "setStarFile:"
        theFix = F.Fix()
        with self.assertRaises(ValueError) as context:
            theFix.setStarFile("txt")
        self.assertEquals(expectedDiag, context.exception.args[0][0:len(expectedDiag)],
                          "Minor:  failure to delineate between star file name and extension") 
        pass
        
    def test500_950_SholdRaiseExceptionOnMissingFileName(self):
        expectedDiag = self.className + "setStarFile:"
        theFix = F.Fix()
        with self.assertRaises(ValueError) as context:
            theFix.setStarFile()
        self.assertEquals(expectedDiag, context.exception.args[0][0:len(expectedDiag)],
                          "Major:  failure to check for missing star file")       
        pass
        
           
    def test500_960_SholdRaiseExceptionOnMissingFile(self):
        expectedDiag = self.className + "setStarFile:"
        theFix = F.Fix()
        with self.assertRaises(ValueError) as context:
            theFix.setStarFile(self.RANDOM_LOG_FILE+".txt")
        self.assertEquals(expectedDiag, context.exception.args[0][0:len(expectedDiag)],
                          "Major:  failure to check for missing star file") 
        pass


#*******************************************************************************************************************
# Unit Tests
#*******************************************************************************************************************

#AriesEntriesList.Py
#I plan to use the 600's for all of the Aries tests to just make things easier on me, incrementing by 10s

#    Unit Test: 600_010
#        Analysis - initiate ariesEntries
#            inputs
#                f.txt, len(f) > 0
#            outputs
#                none
#            state change
#                sets filename
#
#            Happy path
#                nominal case: AriesEntriesList()
#            Sad path
#                none

    def test600_010_ShouldCreateAriesEntriesListAndSetName(self):
        ariesFile = AriesEntriesList.AriesEntriesList("aries.txt")
        self.assertIsInstance(ariesFile, AriesEntriesList.AriesEntriesList)
        pass

#    Unit Test: 600_020
#        Analysis - init setting filename and getAriesFileName
#            inputs
#                none
#            outputs
#                str - filename
#            state change
#                filename is changed
#
#            Happy path
#                nominal case: AriesEntriesList() -> getAriesFileName
#            Sad path
#                none

    def test600_020_ShouldCreateAriesEntriesListAndSetName(self):
        ariesFile = AriesEntriesList.AriesEntriesList("aries.txt")
        self.assertEquals(ariesFile.getAriesFileName(), "aries.txt")
        pass


#    Unit Test: 600_030
#        Analysis - calculateSecondsSinceSighting()
#            inputs
#                sighting, entry
#            outputs
#                seconds
#            state change
#                none
#
#            Happy path
#                nominal case: returns seconds
#            Sad path
#                none

    def test600_030_ShouldReturnCorrectSeconds(self):
        observation = Angle.Angle()
        sighting = Sighting.Sighting("test", "2005-09-15", "13:30:00", observation.getString(), 0, 72, 100, "Natural")
        entry = AriesEntry.AriesEntry("09/15/05", 13, observation.getString())
        ariesFile = AriesEntriesList.AriesEntriesList("aries.txt")
        self.assertEquals(ariesFile._calculateSecondsSinceSighting(sighting, entry), 1800)
        pass
    
#    Unit Test: 600_040
#        Analysis - getGreenWichHourAngleFromFile()
#            inputs
#                sighting
#            outputs
#                angle
#            state change
#                none
#
#            Happy path
#                nominal case: returns Angle
#            Sad path
#                bad sighting

    def test600_040_ShouldReturnCorrectAngle(self):
        angletest = Angle.Angle()
        #01/01/17 2  130d10.4
        sighting = Sighting.Sighting("test", "2017-01-01", "2:30:00", angletest.getString(), 0, 72, 100, "Natural")
        ariesFile = AriesEntriesList.AriesEntriesList("aries.txt")
        ariesFile.createAriesSightingList()
        GHA = ariesFile._getGreenWichHourAngleFromFile(sighting).getString()
        self.assertEquals(GHA, "130d10.4")
        pass
    
    def test600_940_ShouldFailWhenCreatingSightingsList(self):
        angletest = Angle.Angle()
        #01/01/17 2  130d10.4
        sighting = Sighting.Sighting("test", "2017-01-01", "2:30:00", angletest.getString(), 0, 72, 100, "Natural")
        ariesFile = AriesEntriesList.AriesEntriesList("brokenAries.txt")
        
        with self.assertRaises(ValueError) as context:
            ariesFile.createAriesSightingList()
        pass
    
#    Unit Test: 600_050
#        Analysis - _calculateAriesGreenWichHourAngle()
#            inputs
#                ariesAngle1, ariesAngle2, seconds
#            outputs
#                AriesAngle
#            state change
#                none
#
#            Happy path
#                nominal case: returns Angle
#            Sad path
#                none

    def test600_050_ShouldReturnCorrectAngle(self):
        angletest = Angle.Angle()
        sighting = Sighting.Sighting("test", "2017-01-01", "2:30:00", angletest.getString(), 0, 72, 100, "Natural")
        ariesFile = AriesEntriesList.AriesEntriesList("aries.txt")
        ariesGHA = ariesFile.getGreenWichHourAngle(sighting)
        self.assertEquals(ariesGHA.getString(), "7d31.2")
        pass
    


#StarList.Py
#I plan to use the 700's for all of the Aries tests to just make things easier on me, incrementing by 10s

#    Unit Test: 700_010
#        Analysis - initiate StarList
#            inputs
#                f.txt, len(f) > 0
#            outputs
#                none
#            state change
#                sets filename
#
#            Happy path
#                nominal case: StarsList()
#            Sad path
#                bad filename

    def test600_010_ShouldCreateStarsListAndSetName(self):
        starsFile = StarsList.StarsList("stars.txt")
        self.assertIsInstance(starsFile, StarsList.StarsList)
        pass

#    Unit Test: 700_020
#        Analysis - init setting filename and getStarsFileName
#            inputs
#                none
#            outputs
#                str - filename
#            state change
#                filename is changed
#
#            Happy path
#                nominal case: StarsList() -> getStarsFileName
#            Sad path
#                none

    def test700_020_ShouldCreateStarsListAndSetName(self):
        starsFile = StarsList.StarsList("stars.txt")
        self.assertEquals(starsFile.getStarsFileName(), "stars.txt")
        pass


#    Unit Test: 700_030
#        Analysis - getStar()
#            inputs
#                sighting
#            outputs
#                star
#            state change
#                none
#
#            Happy path
#                nominal case: returns star
#            Sad path
#                none

    def test700_030_ShouldReturnStar(self):
        starsList = StarsList.StarsList("stars.txt")
        starsList.createStarList()
        
        angletest = Angle.Angle()
        sighting = Sighting.Sighting("Ankaa", "2017-01-01", "2:30:00", angletest.getString(), 0, 72, 100, "Natural")
        
        star = starsList.getStar(sighting)
        sidewichHourAngle = star.getSiderealHourAngle().getString()
        geographicPositionLatitude = star.getGeographicPositionLatitude().getString()
        
        self.assertEqual(sidewichHourAngle, "353d14.1")
        
        self.assertEqual(geographicPositionLatitude, "-42d13.4")
        #self.assertEqual(geographicPositionLatitude, "317d46.6")
    


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()