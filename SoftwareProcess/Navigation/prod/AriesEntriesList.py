'''
Created on Oct 30, 2016

@author: Aaron
'''

import Navigation.prod.Sighting as S
import Navigation.prod.Angle as A
import time

class AriesEntriesList():
    
    def __init__(self, txtFile):
        self.ariesSightingsList = []
        try :
            self.fileName = txtFile
        except:
            raise ValueError("AriesSightingsList.__init__:  The txt file could not be loaded correctly. The file may not exist or something else may have gone wrong.")
        pass
    
    def getGreenWichHourAngle(self, sighting):
        pass
    
    def getGreenWichHourAngleFromFile(self, sighting):
        pass
    
    def getAriesFileName(self):
        return self.fileName
    
    def getRelevantAriesEntry(self):
        pass
    

    
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