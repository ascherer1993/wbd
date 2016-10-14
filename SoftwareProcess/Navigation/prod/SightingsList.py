'''
Created on Oct 12, 2016

@author: Aaron
'''

import Navigation.prod.Sighting as Sighting
import xml.etree.ElementTree as ET

class SightingsList():
    
    def __init__(self, xmlFile):
        self.sightingsList = []
        pathPrefix = '../Resources/'
        XMLDOM = ET.parse(pathPrefix + xmlFile)
        fix = XMLDOM.getroot()
        
        for sighting in fix:
            self.sightingsList.append(self._extractSighting(sighting))
        pass
    
    def getSightingsList(self):
        return self.sightingsList
        pass
    
    def _extractSighting(self, xmlSighting):
        body = xmlSighting.find("body").text
        date = xmlSighting.find("date").text
        time = xmlSighting.find("time").text
        observation = xmlSighting.find("observation").text
        height = xmlSighting.find("height").text
        temperature = xmlSighting.find("temperature").text
        pressure = xmlSighting.find("pressure").text
        horizon = xmlSighting.find("horizon").text
        
        return Sighting.Sighting(body, date, time, observation, height, temperature, pressure, horizon)
    
