'''
Created on Oct 12, 2016

@author: Aaron Scherer
'''

import Navigation.prod.SightingsList as SightingsList
import Navigation.prod.AriesEntriesList as AriesEntriesList
import Navigation.prod.StarsList as StarsList
import Navigation.prod.LogFile as LogFile
import Navigation.prod.Angle as Angle
import Navigation.prod.ApproximateLocation as ApproximateLocation
import os.path
import math as Math

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
            self.AriesEntriesList = None
            self.StarsList = None
            
            
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
        
        self.logFileInstance.writeToLogEntry("Sighting file:\t" + os.path.abspath('../Resources/' + sightingFile))
        
        returnPath = os.path.abspath('../Resources/' + sightingFile)
        return returnPath
    
    def setAriesFile(self, ariesFile = None):
        if ariesFile == None:
            raise ValueError("Fix.setAriesFile:  setAriesFile requires a file name.")
        
        if not isinstance(ariesFile, str):
            raise ValueError("Fix.setAriesFile:  The parameter you have provided is not of type string.")

        if len(ariesFile) < 1:
            raise ValueError("Fix.setAriesFile:  The parameter you have provided is not a long enough filename.")
        
        try:
            fileNameSplit = ariesFile.split('.')
            if fileNameSplit[1] != 'txt':
                raise ValueError("Fix.setAriesFile:  The filename you have provided does not have the extension \'.txt\'.")
            
            
            if not os.path.isfile('../Resources/' + ariesFile):
                raise ValueError("Fix.setAriesFile:  The specified file could not be found.")
            
            self.AriesEntriesList = AriesEntriesList.AriesEntriesList(ariesFile)
            
        except:
            raise ValueError("Fix.setAriesFile:  The filename you have provided is not valid or the file could not be modified for an unknown reason.")
        
        returnPath = os.path.abspath('../Resources/' + ariesFile)
        self.logFileInstance.writeToLogEntry("Aries file:\t" + returnPath)
        return returnPath
    
    def setStarFile(self, starFile = None):
        if starFile == None:
            raise ValueError("Fix.setStarFile:  setAriesFile requires a file name.")
        
        if not isinstance(starFile, str):
            raise ValueError("Fix.setStarFile:  The parameter you have provided is not of type string.")

        if len(starFile) < 1:
            raise ValueError("Fix.setStarFile:  The parameter you have provided is not a long enough filename.")
        
        try:
            fileNameSplit = starFile.split('.')
            if fileNameSplit[1] != 'txt':
                raise ValueError("Fix.setStarFile:  The filename you have provided does not have the extension \'.txt\'.")
            
            
            if not os.path.isfile('../Resources/' + starFile):
                raise ValueError("Fix.setStarFile:  The specified file could not be found.")
            
            self.StarsList = StarsList.StarsList(starFile)
            
        except:
            raise ValueError("Fix.setStarFile:  The filename you have provided is not valid or the file could not be modified for an unknown reason.")
        
        returnPath = os.path.abspath('../Resources/' + starFile)
        self.logFileInstance.writeToLogEntry("Star file:\t" + returnPath)
        return returnPath
    
    
    def getSightings(self, assumedLatitude = None, assumedLongitude = None):
        if self.SightingList == None or self.AriesEntriesList == None or self.StarsList == None:
            raise ValueError("Fix.getSightings:  The sightings file, aries file, or star file has not been set.")
        
        assumedLatitudeAngle = None
        assumedLongitudeAngle = None
        returnTuple = ("0d0.0", "0d0.0")
        
        try:
            if assumedLatitude != None:
                if assumedLatitude.lower()[0] == 'n' or assumedLatitude.lower()[0] == 's':
                    assumedLatitudeAngle = Angle.Angle()
                    assumedLatitudeAngle.setDegrees(0, assumedLatitude[0])
                    assumedLatitudeAngle.setDegreesAndMinutes(assumedLatitude[1:])
                else:
                    if assumedLatitude[0] != '0':
                        raise ValueError("Fix.getSightings:  Your assumed latitude did not follow the requirements.")
                    else:
                        assumedLatitudeAngle = Angle.Angle()
                        assumedLatitudeAngle.setDegreesAndMinutes(assumedLatitude)
                        
            if assumedLatitude != None:
                assumedLongitudeAngle = Angle.Angle()
                assumedLongitudeAngle.setDegreesAndMinutes(assumedLongitude)
        except:
            raise ValueError("Fix.getSightings:  There was an issue with one of the parameters included.")
        
            
        try:
            
            returnTuple = self.writeSightingsToLog(self.SightingList.getSightingsList(), assumedLatitudeAngle, assumedLongitudeAngle)
            
        except:
            raise ValueError("Fix.getSightings:  There was a problem loading in the file.")
        
        self.logFileInstance.writeToLogEntry("End of sighting file:\t" + self.SightingList.getFileName())
        return returnTuple
        pass
    
    def writeSightingsToLog(self, sightings, assumedLatitude = None, assumedLongitude = None):
        failedSightings = 0
        approximateLatitude = Angle.Angle()
        approximateLongitude = Angle.Angle()
        
        latitudeTotal = 0
        longitudeTotal = 0
        
        for sighting in sightings:
            try:
                
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
                
                
                star = self.StarsList.getStar(sighting)
                
                geographicPositionLatitude = star.getGeographicPositionLatitude().getString()
                siderealHourAngle = star.getSiderealHourAngle() 
                GWH = self.AriesEntriesList.getGreenWichHourAngle(sighting)
                geographicPositionLongitudeInDecimal = siderealHourAngle.getDegrees() + GWH.getDegrees()
                geographicPositionLongitude = Angle.Angle()
                geographicPositionLongitude.setDegrees(geographicPositionLongitudeInDecimal)
                geographicPositionLongitudeString = geographicPositionLongitude.getString()
                
                if assumedLatitude == None and assumedLongitude == None:
                    self.logFileInstance.writeToLogEntry(body + "\t" + date + "\t" + time + "\t" + adjustedAltitudeString + "\t" + geographicPositionLatitude + "\t" + geographicPositionLongitudeString)
                
                else:
                    distanceAdjustmentAngle = ApproximateLocation.ApproximateLocation.getDistanceAdjustmentAngle(geographicPositionLatitude, geographicPositionLongitude, assumedLatitude, assumedLongitude, adjustedAltitude)
                    azimuthAdjustment = ApproximateLocation.ApproximateLocation.getAzimuthAdjustmentAngle(geographicPositionLatitude, geographicPositionLongitude, assumedLatitude, assumedLongitude, adjustedAltitude)
                    azimuthAdjustmentString = azimuthAdjustment.getString().strip()
                
                    latitudeTotal = latitudeTotal + (distanceAdjustmentAngle * Math.cos(azimuthAdjustment.getInRadians()))
                    longitudeTotal = longitudeTotal + (distanceAdjustmentAngle * Math.sin(azimuthAdjustment.getInRadians()))
                
                    self.logFileInstance.writeToLogEntry(body + "\t" + date + "\t" + time + "\t" + adjustedAltitudeString + "\t" + geographicPositionLatitude + "\t" + geographicPositionLongitudeString +
                                                     "\t" + assumedLatitude.getString() + "\t" + assumedLongitude.getString() + "\t" + str(distanceAdjustmentAngle).strip() + "\t" + azimuthAdjustmentString)
                    
            except:
                failedSightings = failedSightings + 1
        
        
        if assumedLatitude != None and assumedLongitude != None:
            approximateLatitudeValue = assumedLatitude.getDegrees() + latitudeTotal/60
            approximateLatitude.setDegrees(approximateLatitudeValue, assumedLatitude.getHemisphere())
            
            approximateLongitudeValue = assumedLongitude.getDegrees() + longitudeTotal/60
            approximateLongitude.setDegrees(approximateLongitudeValue)
                
        self.logFileInstance.writeToLogEntry("Sighting errors:\t" + str(failedSightings + self.SightingList.getFailedLoadCount()))
        #self.logFileInstance.writeToLogEntry("Approximate latitude:\t" + approximateLatitude.getString() + "\t" + approximateLongitude.getString())
        
        if assumedLatitude != None and assumedLongitude != None:
            return (approximateLatitude.getString(), approximateLongitude.getString())
        
        pass  