'''
Created on Oct 30, 2016

@author: Aaron
'''

import Navigation.prod.Sighting as S
import Navigation.prod.Angle as A
import Navigation.prod.Star as Star
import time as T
import datetime

class StarsList():
    
    def __init__(self, txtFile):
        self.starsList = []
        try :
            fileNameSplit = txtFile.split('.')
            if fileNameSplit[1] != 'txt':
                raise ValueError("StarsList.__init__:  The filename you have provided does not have the extension \'.txt\'.")
            
            self.fileName = txtFile
        except:
            raise ValueError("StarsList.__init__:  The txt file could not be loaded correctly. The file may not exist or something else may have gone wrong.")
        pass
    
    def getStar(self, sighting):
        #closest, earlier if not on the date but between two
        try:
            self.createStarList()
            for star in self.starsList:
                if star.getBody() == sighting.getBody():
                    starDate = star.getDate()
                    dateArray = starDate.split('/')
                    dateArray[2] = "20" + dateArray[2]
                    starDate = dateArray[0] + '/' + dateArray[1] + '/' + dateArray[2]
                    if self._isDateFormat(starDate):
                        starDate = datetime.datetime.strptime(starDate, '%m/%d/%Y')
                        sightingDate = datetime.datetime.strptime(sighting.getDate(), '%Y-%m-%d')
                        if starDate == sightingDate:
                            return star
                    else:
                        raise ValueError("StarsList.getStar:  A date was in the wrong format")
            return -1
        except:
            raise ValueError("StarsList.getStar:  There was a problem reading from the file")

    
    def createStarList(self):
        try:
            self.starsList = []
            pathPrefix = '../Resources/'
            path = pathPrefix + self.fileName
            for fileLine in open(path,'r'):
                if fileLine != "":
                    lineArray = fileLine.split("\t")
                    ariesEntry = Star.Star(lineArray[0], lineArray[1], lineArray[2], lineArray[3])
                    self.starsList.append(ariesEntry)
        except:
            raise ValueError("AriesSightingsList.createAriesSightingList:  The txt file could not be loaded correctly. The file may not exist or something else may have gone wrong.")


    def getStarsFileName(self):
        return self.fileName    
    
    #I got this Nadia Alramli in her response found at from http://stackoverflow.com/questions/1322464/python-time-format-check/1322524
    def _isTimeFormat(self, timeIn):
        try:
            T.strptime(timeIn, '%H:%M:%S')
            return True
        except ValueError:
            return False

    def _isDateFormat(self, dateIn):
        try:
            datetime.datetime.strptime(dateIn, '%m/%d/%Y')
            return True
        except ValueError:
            return False