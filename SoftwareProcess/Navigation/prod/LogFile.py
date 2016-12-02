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
            
            #self.filePath = '../Resources/' + fileName
            self.filePath = fileName
            
            if os.path.isfile(self.filePath):
                self.file = open(self.filePath, 'a')
            else:
                self.file = open(self.filePath, 'w')
            
            returnPath = os.path.abspath(self.filePath)
            self.file.write("Log file:\t" + returnPath + "\n")
            
            self.file.close()
            
#             self.writeToLogEntry("Start of log")
        except:
            raise ValueError("LogFile.__init__:  The filename you have provided is not valid or the file could not be modified for an unknown reason.")
    
    def writeToLogEntry(self, msg):
        message = "LOG:\t" + datetime.datetime.now().isoformat(' ') + ":\t" + msg + "\n"
        
        self.file = open(self.filePath, 'a')
        self.file.write(message)
        self.file.close()
        pass
    
    def closeFile(self):
        self.file.close()
