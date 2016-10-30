'''
Created on Oct 30, 2016

@author: Aaron
'''

import Navigation.prod.Sighting as S
import Navigation.prod.Angle as A

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
    
    
    def getAriesFileName(self):
        pass
    
    def getRelevantAriesEntry(self):
        pass
    

    
    def calculateAriesGreenWichHourAngle(self, gwh1, gwh2, seconds):
        pass
    
    def calculateSecondsSinceSighting(self, sighting, Entry):
        pass