'''
Created on Oct 30, 2016

@author: Aaron
'''

import Navigation.prod.Sighting as S
import Navigation.prod.Angle as A
import Navigation.prod.AriesEntry as AE
import time as T
import datetime
from Navigation.prod.Sighting import Sighting

class AriesEntriesList():
    
    def __init__(self, txtFile):
        self.ariesEntriesList = []
        try :
            fileNameSplit = txtFile.split('.')
            if fileNameSplit[1] != 'txt':
                raise ValueError("AriesEntriesList.__init__:  The filename you have provided does not have the extension \'.txt\'.")
            
            self.fileName = txtFile
        except:
            raise ValueError("AriesSightingsList.__init__:  The txt file could not be loaded correctly. The file may not exist or something else may have gone wrong.")
        pass
    
    def getGreenWichHourAngle(self, sighting):
        sighting1 = sighting
        self.createAriesSightingList()
        GHA1 = self._getGreenWichHourAngleFromFile(sighting1)
        
        #sightingTimeArray = sighting.getTime().split(':')
        sightingDatetime = sighting.getDateTime()
        
        #Adds 1 hour
        sighting2Datetime = sightingDatetime + datetime.timedelta(0, 3600)
#         newHourValue = int(sightingTimeArray[0]) + datetime.timedelta(0,3)
#         if newHourValue == 24:
#             dateToChange = sighting.getDate()
#             dateSplit = dateToChange.split('/')
#             dateSplit[2] = dateSplit[2] 
            
        #sightingTwoTime = str(newHourValue) + ":" + sightingTimeArray[1] + ":" + sightingTimeArray[2]
        
        sighting2 = S.Sighting(sighting.getBody(), sighting2Datetime.strftime('%Y-%m-%d'), sighting2Datetime.strftime('%H:%M:%S'), sighting.getObservation().getString(), sighting.getHeight(), sighting.getTemperature(), sighting.getPressure(), sighting.getHorizon())
        GHA2 = self._getGreenWichHourAngleFromFile(sighting2)
        
        entry = self._getClosestEntry(sighting)
        seconds = self._calculateSecondsSinceSighting(sighting, entry)
        
        newAngle = GHA2.getDegrees() - GHA1.getDegrees()
        
        returnValue = GHA1.getDegrees() + abs(newAngle) * (seconds / 3600.0)
        returnAngle = A.Angle()
        returnAngle.setDegrees(returnValue)
        
        return returnAngle
    
    def createAriesSightingList(self):
        try:
            self.ariesEntriesList = []
            pathPrefix = '../Resources/'
            path = pathPrefix + self.fileName
            for fileLine in open(path,'r'):
                if fileLine != "":
                    lineArray = fileLine.split("\t")
                    ariesEntry = AE.AriesEntry(lineArray[0], int(lineArray[1]), lineArray[2])
                    self.ariesEntriesList.append(ariesEntry)
                else:
                    raise ValueError("AriesSightingsList.createAriesSightingList:  A date was in the wrong format")
        except:
            raise ValueError("AriesSightingsList.createAriesSightingList:  The txt file could not be loaded correctly. The file may not exist or something else may have gone wrong.")
        
    
    def getAriesFileName(self):
        return self.fileName    
    
    def _getGreenWichHourAngleFromFile(self, sighting):
        try:
            ariesEntry = self._getClosestEntry(sighting)
            return ariesEntry.getGHA()
        except:
            raise ValueError("AriesSightingsList.getGreenWichHourAngleFromFile:  Finding the closest result")
        
        pass
    
    def _getClosestEntry(self, sighting):
        try:
            for ariesEntry in self.ariesEntriesList:
                ariesDate = ariesEntry.getDate()
                dateArray = ariesDate.split('/')
                dateArray[2] = "20" + dateArray[2]
                ariesDate = dateArray[0] + '/' + dateArray[1] + '/' + dateArray[2]
                if self._isDateFormat(ariesDate):
                    ariesDate = datetime.datetime.strptime(ariesDate, '%m/%d/%Y')
                    sightingDate = datetime.datetime.strptime(sighting.getDate(), '%Y-%m-%d')
                    if ariesDate == sightingDate:
                        sightingTime = sighting.getTime()
                        sightingTimeArray = sightingTime.split(':')
                        if int(sightingTimeArray[0]) == ariesEntry.getHour():
                            return ariesEntry
            return -1
        except:
            raise ValueError("AriesSightingsList._getClosestEntry:  There was a problem reading from the file")
    
    

    
    def _calculateAriesGreenWichHourAngle(self, gwh1, gwh2, seconds):
        pass
    
    def _calculateSecondsSinceSighting(self, sighting, entry):
        sightingTime = sighting.getTime()
        sightingTimeArray = sightingTime.split(':')
        sightingTotalSeconds = int(sightingTimeArray[0])*3600 + int(sightingTimeArray[1])*60 + int(sightingTimeArray[2])
        entryHour = entry.getHour()
        entryTotalSeconds = int(entryHour)*3600
        
        totalSeconds = sightingTotalSeconds - entryTotalSeconds
        return totalSeconds
    
    
    #I got this Nadia Alramli in her response found at from http://stackoverflow.com/questions/1322464/python-time-format-check/1322524
    def _isTimeFormat(self, timeIn):
        try:
            T.strptime(timeIn, '%H:%M:%S')
            return True
        except ValueError:
            return False

    def _isDateFormat(self, dateIn):
        try:
            datetime.datetime.strptime(dateIn, '%m/%d/%Y')
            return True
        except ValueError:
            return False