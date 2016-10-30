'''
Created on Oct 30, 2016

@author: Aaron
'''

import Navigation.prod.Sighting as S
import Navigation.prod.Angle as A

class StarsList():
    
    def __init__(self, txtFile):
        self.starsList = []
        try :
            self.fileName = txtFile
        except:
            raise ValueError("StarsList.__init__:  The txt file could not be loaded correctly. The file may not exist or something else may have gone wrong.")
        pass
    
    def getStar(self):
        #closest, earlier if not on the date but between two
        pass
    
    def getSiderealHourAngle(self, sighting):
        siderealHourAngle = A.Angle();
        #first number
        pass
    
    def getStarDeclination(self, sighting):
        siderealHourAngle = A.Angle();
        #second number
        pass