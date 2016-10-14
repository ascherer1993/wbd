'''
Created on Oct 12, 2016

@author: Aaron
'''

import Navigation.prod.SightingsList as SightingsList
import Navigation.prod.LogFile as LogFile

class Fix():
    def __init__(self, logFile = None):
        if logFile == None:
            logFile = "log.txt"
            
        if not isinstance(logFile, str):
            raise ValueError("Fix.__init__:  The parameter you have provided is not of type string.")
        
        if len(logFile) < 1:
            raise ValueError("Fix.__init__:  The parameter you have provided is not a long enough filename.")
        
        try:
            fileNameSplit = logFile.split('.')
            if fileNameSplit[1] != 'txt':
                raise ValueError("LogFile.__init__:  The filename you have provided does not have the extension \'.txt\'.")
            
            self.logFileInstance = LogFile.LogFile(logFile)
            
        except:
            raise ValueError("Fix.__init__:  The filename you have provided is not valid or the file could not be modified for an unknown reason.")
        pass
    
    def setSightingFile(self, sightingFile):
        return True
        pass
    
    def getSightings(self):
        
        sl = SightingsList();
        approximateLatitude = "0d0.0"
        approximateLongitude = "0d0.0"
        return (approximateLatitude, approximateLongitude)
        pass