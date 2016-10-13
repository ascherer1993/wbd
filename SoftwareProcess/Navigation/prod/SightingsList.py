'''
Created on Oct 12, 2016

@author: Aaron
'''

import Navigation.prod.Sighting as Sighting
import xml.etree.ElementTree as ET

class SightingsList():
    def __init__(self, xmlFile):
        self.sightingsList = []
        XMLDOM = ET.parse('xmlFile')
        fix = XMLDOM.getroot()
        
        for child in fix:
            self.sightingsList.append(self.extractSighting(child))
        
        pass
    
    def getSightingsList(self):
        return self.sightingsList
        pass
        
    def buildDOM(self):
        pass
    
    def extractSighting(self, xmlSighting):
        pass
    
    def extractElement(self):
        pass