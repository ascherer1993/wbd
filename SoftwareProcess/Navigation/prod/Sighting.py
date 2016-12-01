'''
Created on Oct 12, 2016

@author: Aaron
'''

import math
import Navigation.prod.Angle as Angle
import time as T
import datetime

class Sighting():
    
    def __init__(self, body, date, time, observation, height, temperature, pressure, horizon):
        self.body = body
        
        if not self._isDateFormat(date):
            raise ValueError("Sighting._init_:  Date is not valid.")
        self.date = date
        
        if not self._isTimeFormat(time):
            raise ValueError("Sighting._init_:  Time is not valid.")
        self.time = time
        
        self.observation = Angle.Angle()
        self.observation.setDegreesAndMinutes(observation)
        self.height = height
        
        if temperature != None and not isinstance(temperature, int):
            raise ValueError("Sighting._init_:  Temperature must be an int.")
        if temperature != None and temperature < -20 or temperature > 120:
            raise ValueError("Sighting._init_:  Temperature must be GE -20 degrees and LE to 120 degrees.")
        self.temperature = temperature
        
        if pressure != None and not isinstance(pressure, int):
            raise ValueError("Sighting._init_:  Pressure must be an int.")
        self.pressure = pressure
        
        if (horizon.lower() != "artificial" and horizon.lower() != "natural"):
            raise ValueError("Sighting._init_:  Horizon has a bad value.")
        
        self.horizon = horizon
        pass
    
    #I got this Nadia Alramli in her response found at from http://stackoverflow.com/questions/1322464/python-time-format-check/1322524
    def _isTimeFormat(self, timeIn):
        try:
            T.strptime(timeIn, '%H:%M:%S')
            return True
        except ValueError:
            return False

    def _isDateFormat(self, dateIn):
        try:
            datetime.datetime.strptime(dateIn, '%Y-%m-%d')
            return True
        except ValueError:
            return False

    
    def getBody(self):
        return self.body
    
    def getDate(self):
        return self.date
    
    def getTime(self):
        return self.time
    
    def getObservation(self):
        return self.observation
    
    def getHeight(self):
        return self.height
    
    def getTemperature(self):
        return self.temperature
    
    def getPressure(self):
        return self.pressure
    
    def getHorizon(self):
        return self.horizon
    
    def getAdjustedAltitude(self):
        if self.height == None or self.pressure == None or self.temperature == None:
            return False
        dip = self._calculateDip(self.height, self.horizon)
        refraction = self._calculateRefraction(self.pressure, self.temperature, self.observation)
        return self.observation.getDegrees() + dip + refraction
    
    def _calculateDip(self, height, horizon):
        if not isinstance(height, float) and not isinstance(height, int) :
            raise ValueError("Sighting._calculateDip:  The parameter provided for height was not a integer or a float")
        if not isinstance(horizon, str):
            raise ValueError("Sighting._calculateDip:  The parameter provided for horizon was not a string")
        horizon = horizon.lower()
        if horizon == "natural":
            dip = (-.97 * math.sqrt(height)) / 60
        elif horizon == "artificial":
            dip = 0
        else:
            raise ValueError("Sighting._calculateDip:  horizon is not a valid horizon type")
        return dip
    
    def _calculateRefraction(self, pressure, temperature, altitude):
        tempInCelsius = self._calculateTempInCelsius(temperature)
#         anAngle = Angle()
#         anAngle.setDegrees(altitude)
#         tangentOfAltitude = anAngle.getTangent()
        tangentOfAltitude = altitude.getTangent()
        return (-.00452 * pressure)/(273 + tempInCelsius)/tangentOfAltitude
    
    # This could probably be moved into some utility class
    def _calculateTempInCelsius(self, tempInFahrenheit):
        return (tempInFahrenheit - 32) * (5.0/9)