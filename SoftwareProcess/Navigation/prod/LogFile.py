'''
Created on Oct 12, 2016

@author: Aaron
'''

import os.path
import datetime


class LogFile():
    '''
    classdocs
    '''
    def __init__(self, fileName = None):
        if fileName == None:
            fileName = "log.txt"
        try:
            fileNameSplit = fileName.split('.')
            if fileNameSplit[1] != 'txt':
                raise ValueError("LogFile.__init__:  The filename you have provided does not have the extension \'.txt\'.")
            
            if os.path.isfile('../Resources/' + fileName):
                self.file = open('../Resources/' + fileName, 'a')
            else:
                self.file = open('../Resources/' + fileName, 'w')
            
            
            
            self.writeToLogEntry("Start of log")
        except:
            raise ValueError("LogFile.__init__:  The filename you have provided is not valid or the file could not be modified for an unknown reason.")
    
    def writeToLogEntry(self, msg):
        message = "LOG:\t" + datetime.datetime.now().isoformat(' ') + ":\t" + msg + "\n"
        self.file.write(message)
        pass
    
    
