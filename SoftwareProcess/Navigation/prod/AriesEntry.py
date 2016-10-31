'''
Created on Oct 30, 2016

@author: Aaron
'''
import math
import Navigation.prod.Angle as A
import time as T
import datetime

class AriesEntry():
    
    def __init__(self, date, hour, greenwichHourAngle):
        self.date = date
        
        self.hour = hour
        
        self.greenwichHourAngle = A.Angle()
        self.greenwichHourAngle.setDegreesAndMinutesAllowNegatives(greenwichHourAngle)
        
    def getHour(self):
        return self.hour
    
    def getDate(self):
        return self.date
    
    def getGHA(self):
        return self.greenwichHourAngle
    
    