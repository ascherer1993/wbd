'''
Created on Oct 12, 2016

@author: Aaron
'''

import math
import Navigation.prod.Angle as Angle

class Sighting():
    
    def __init__(self, body, date, time, observation, height, temperature, pressure, horizon):
        self.body = body
        self.date = date
        self.time = time
        self.observation = Angle.Angle()
        self.observation.setDegreesAndMinutes(observation)
        self.height = height
        self.temperature = temperature
        self.pressure = pressure
        self.horizon = horizon
        pass
    
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
    
    def getHorizon(self):
        return self.horizon
    
    def getAdjustedAltitude(self):
        dip = self._calculateDip(self.height, self.horizon)
        refraction = self._calculateRefraction(self.pressure, self.temperature, self.observation)
        return self.observation.getDegrees() + dip + refraction
    
    def _calculateDip(self, height, horizon):
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