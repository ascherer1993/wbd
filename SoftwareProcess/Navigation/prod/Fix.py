'''
Created on Oct 12, 2016

@author: Aaron
'''

import Navigation.prod.SightingsList as SightingsList
import Navigation.prod.LogFile as LogFile
import Navigation.prod.Angle as Angle
import os.path

class Fix():
    def __init__(self, logFile = None):
        
        if logFile == None:
            logFile = "log.txt"
            
        if not isinstance(logFile, str):
            raise ValueError("Fix.__init__:  The parameter you have provided is not of type string.")
        
        if len(logFile) < 1:
            raise ValueError("Fix.__init__:  The parameter you have provided is not a long enough filename.")
        
        try:
            fileNameSplit = logFile.split('.')
            if fileNameSplit[1] != 'txt':
                raise ValueError("LogFile.__init__:  The filename you have provided does not have the extension \'.txt\'.")
            
            
            self.logFileInstance = LogFile.LogFile(logFile)
            self.SightingList = None
            
            
        except:
            raise ValueError("Fix.__init__:  The filename you have provided is not valid or the file could not be modified for an unknown reason.")

        pass
    
    def setSightingFile(self, sightingFile = None):
        if sightingFile == None:
            raise ValueError("Fix.setSightingFile:  setSightingFile requires a file name.")
        
        if not isinstance(sightingFile, str):
            raise ValueError("Fix.setSightingFile:  The parameter you have provided is not of type string.")

        if len(sightingFile) < 1:
            raise ValueError("Fix.setSightingFile:  The parameter you have provided is not a long enough filename.")
        
        try:
            fileNameSplit = sightingFile.split('.')
            if fileNameSplit[1] != 'xml':
                raise ValueError("Fix.setSightingFile:  The filename you have provided does not have the extension \'.xml\'.")
            
            
            if not os.path.isfile('../Resources/' + sightingFile):
                raise ValueError("Fix.setSightingFile:  The specified file could not be found.")
            
            self.SightingList = SightingsList.SightingsList(sightingFile)
            
        except:
            raise ValueError("Fix.setSightingFile:  The filename you have provided is not valid or the file could not be modified for an unknown reason.")
        
        self.logFileInstance.writeToLogEntry("Start of sighting file:\t" + sightingFile)
        
        return sightingFile
        pass
    
    def getSightings(self):
        try:
            
            self.writeSightingsToLog(self.SightingList.getSightingsList())
            
        except:
            raise ValueError("Fix.getSightings:  There was a problem loading in the file.")
        
        self.logFileInstance.writeToLogEntry("End of sighting file:\t" + self.SightingList.getFileName())
        approximateLatitude = "0d0.0"
        approximateLongitude = "0d0.0"
        return (approximateLatitude, approximateLongitude)
        pass
    
    def writeSightingsToLog(self, sightings):
        for sighting in sightings:
            adjustedAltitude = Angle.Angle()
            adjustedAltitudeValue = sighting.getAdjustedAltitude()
            if adjustedAltitudeValue != False:
                adjustedAltitude.setDegrees(adjustedAltitudeValue)
                adjustedAltitudeString = adjustedAltitude.getString().strip()
            else:
                adjustedAltitudeString = "NA"
            adjustedAltitude.setDegrees(sighting.getAdjustedAltitude())
            body = sighting.getBody().strip()
            date = sighting.getDate().strip()
            time = sighting.getTime().strip()
            adjustedAltitudeString = adjustedAltitude.getString().strip()
            
            self.logFileInstance.writeToLogEntry(body + "\t" + date + "\t" + time + "\t" + adjustedAltitudeString)
        pass  