'''
Created on Oct 12, 2016

@author: Aaron
'''

class Sighting():
    
    def __init__(self, body, date, time, observation, height, temperature, horizon):
        self.body = body
        self.date = date
        self.time = time
        self.observation = observation
        self.height = height
        self.temperature = temperature
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
        pass
    
    def _calculateDip(self):
        pass
    
    def _calculateRefraction(self):
        pass