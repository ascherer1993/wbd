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
        try :
            XMLDOM = ET.parse(pathPrefix + xmlFile)
            fix = XMLDOM.getroot()
            
            for sighting in fix:
                self.sightingsList.append(self._extractSighting(sighting))
                
            #sorts array by date
            self.sightingsList = sorted(self.sightingsList, key=lambda x: x.date, reverse = False)
        except:
            raise ValueError("SightingsList.__init__:  The xml file could not be loaded correctly. The file may not exist or something else may have gone wrong.")
        pass
    
    def getSightingsList(self):
        return self.sightingsList
        pass
    
    def _extractSighting(self, xmlSighting):
        height = ""
        temperature = ""
        pressure = ""
        horizon = "Natural"
        
        try:
            
            body = xmlSighting.find("body").text
            
            date = xmlSighting.find("date").text
            
            time = xmlSighting.find("time").text
            
            observation = xmlSighting.find("observation").text
            
        except:
            raise ValueError("SightingsList._extractSighting:  The xml file did not contain a mandatory tag (body, date, time, or observation)")
            

        try:
            if xmlSighting.find("height") != None:
                height = float(xmlSighting.find("height").text)
                
            if xmlSighting.find("temperature") != None:
                temperature = float(xmlSighting.find("temperature").text)
                
            if xmlSighting.find("pressure") != None:
                pressure = float(xmlSighting.find("pressure").text)
                
            if xmlSighting.find("horizon") != None:
                horizon = str(xmlSighting.find("horizon").text)
        
        
            
        except:
            raise ValueError("SightingsList._extractSighting:  There was an error in one of the tags")

    
        return Sighting.Sighting(body, date, time, observation, height, temperature, pressure, horizon)
    
