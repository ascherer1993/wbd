'''
Created on Oct 30, 2016

@author: Aaron
'''
import math
import Navigation.prod.Angle as A
import time as T
import datetime

class Star():
    
    def __init__(self, body, date, siderealHourAngle, geographicPositionLatitude):
        self.body = body
        self.date = date
        self.siderealHourAngle = A.Angle()
        self.siderealHourAngle.setDegreesAndMinutesAllowNegatives(siderealHourAngle)
        self.geographicPositionLatitude = A.Angle()
        self.geographicPositionLatitude.setDegreesAndMinutesAllowNegatives(geographicPositionLatitude)
        
    def getBody(self):
        return self.body
    
    def getDate(self):
        return self.date
    
    def getSiderealHourAngle(self):
        return self.siderealHourAngle
    
    def getGeographicPositionLatitude(self):
        return self.geographicPositionLatitude
    
    