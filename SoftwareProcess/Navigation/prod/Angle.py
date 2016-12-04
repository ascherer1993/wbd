'''
    Created on 9/8/2016
    Edited on: 9/10/2016, 9/11/2016

    @author: Aaron Scherer
'''

import re
import math

class Angle():
    # Constructor
    def __init__(self):
        self.angle = 0.0
        self.hemisphere = None
        pass
    
    # Sets angle of Angle object using a float or integer sent to the method
    def setDegrees(self, degrees = None, hemisphere = None):
        if degrees == None:
            degrees = 0.0
        if hemisphere != None:
            self.hemisphere = hemisphere
        # Raises error if the parameter is of the wrong type
        if not isinstance(degrees, float) and not isinstance(degrees, int) :
            raise ValueError("Angle.setDegrees:  The parameter provided was not a integer or a float")
        
        # Rounds to 1 decimal place
        degrees *= 60
        degrees = round(degrees, 1) / 60
        self.angle = float(degrees) % 360
        return self.angle
    
        pass
    
    # Sets angle of the Angle object using a string specified in a certain format
    def setDegreesAndMinutes(self, angleString):
        
        angleString = angleString.strip()  # This was done to strip out white space before the regular expression
        
        # For this project I got to learn regex! 
        # Below, the string parameter is checked to make sure that it matches very specific requirements.
        # I then find all instances of those requirements in the string, and make sure it matches the original string.
        # If it does, the parameter is in the right format and can be used
        regex = "^(-?[0-9]+d[0-9]+\.?[0-9]?)?"  #    xdy.y : x is any positive or negative number that represents the degrees and the y's are the minutes
        regexMatch = re.findall(regex, angleString)
        
        # Checks to make sure there is only one exact match
        if angleString == "" or len(regexMatch) != 1 or len(regexMatch[0]) != len(angleString) :
            raise ValueError("Angle.setDegreesAndMinutes:  The correct format was not provided. Please provide a format that matches #d# or #d#.#")
        
        # Splits string at the symbol d
        newString = angleString.split('d')
        
        # Converts from minutes into decimal to store
        minuteInDecimal = float(newString[1]) / 60
        # Stores one decimal place mod 360
        floatedDegrees = float(newString[0])
        
        # This handles negative degrees
        if floatedDegrees < 0 :
            self.angle = (floatedDegrees - minuteInDecimal) % 360
        else :    
            self.angle = (floatedDegrees + minuteInDecimal) % 360
        return self.angle
        
        pass
    
    # Sets angle of the Angle object using a string specified in a certain format
    def setDegreesAndMinutesAllowNegatives(self, angleString):
        
        angleString = angleString.strip()  # This was done to strip out white space before the regular expression
        
        # For this project I got to learn regex! 
        # Below, the string parameter is checked to make sure that it matches very specific requirements.
        # I then find all instances of those requirements in the string, and make sure it matches the original string.
        # If it does, the parameter is in the right format and can be used
        regex = "^(-?[0-9]+d[0-9]+\.?[0-9]?)?"  #    xdy.y : x is any positive or negative number that represents the degrees and the y's are the minutes
        regexMatch = re.findall(regex, angleString)
        
        # Checks to make sure there is only one exact match
        if angleString == "" or len(regexMatch) != 1 or len(regexMatch[0]) != len(angleString) :
            raise ValueError("Angle.setDegreesAndMinutes:  The correct format was not provided. Please provide a format that matches #d# or #d#.#")
        
        # Splits string at the symbol d
        newString = angleString.split('d')
        
        # Converts from minutes into decimal to store
        minuteInDecimal = float(newString[1]) / 60
        # Stores one decimal place mod 360
        floatedDegrees = float(newString[0])
        
        # This handles negative degrees
        if floatedDegrees < 0 :
            self.angle = floatedDegrees - minuteInDecimal
        else :    
            self.angle = floatedDegrees + minuteInDecimal
        return self.angle
    
    def setHemisphere(self, hemisphere):
        self.hemisphere = hemisphere
        return True
    
    # Adds an angle to this angle object, stores the value, and returns the result
    def add(self, angle= None):
        if angle == None:
            raise ValueError("Angle.add:  A parameter was not provided.")
        # Raises an error if the parameter is of the wrong type
        if not isinstance(angle, Angle) :
            raise ValueError("Angle.add:  The parameter you have provided is not an instance of the Angle class.")
        
        # Rounds to 1 decimal place
        self.angle = round((self.angle + angle.angle) % 360, 1)
        return self.angle
        pass
    
    # Subtracts an angle from this angle object, stores the value, and returns the result.
    def subtract(self, angle= None):
        if angle == None:
            raise ValueError("Angle.subtract:  A parameter was not provided.")
        # Raises an error if the parameter is of the wrong type
        if not isinstance(angle, Angle) :
            raise ValueError("Angle.subtract:  The parameter you have provided is not an instance of the Angle class.")
        
        # Rounds to 1 decimal place
        self.angle = round((self.angle - angle.angle) % 360, 1)
        return self.angle
        pass
    
    # Compares this objects angle to the angle sent in as a parameter and returns results based on the angles.
    def compare(self, angle = None):
        if angle == None:
            raise ValueError("Angle.compare:  A parameter was not provided.")
        
        # Raises an error if the parameter is of the wrong type
        if not isinstance(angle, Angle) :
            raise ValueError("Angle.compare:  The parameter you have provided is not an instance of the Angle class.")
        
        # Return results
        try :
            if self.angle < angle.angle :
                return -1
            elif self.angle == angle.angle :
                return 0
            elif self.angle > angle.angle :
                return 1
        except :
            raise ValueError("Angle.compare:  The two angles could not be compared. The value must have been stored incorrectly.")
        pass
    
    # Returns the angle in string form
    def getString(self):
        # Raises an error if the parameter is of the wrong type
        if isinstance(self.angle, int) :
            self.angle = float(self.angle)
        elif not isinstance(self.angle, float) :
            raise ValueError("Angle.getString:  The angle has not been stored properly in this object")
        
        # Splits the angle into two parts in order to calculate minutes
        degreesArray = str(self.angle).split('.')
        
        # Rounds to one decimal place    
        decimalInMinuteForm = round(float('.' + degreesArray[1]) * 60, 1)
        # Constructs string
        returnString = str(degreesArray[0]) + "d" + str(decimalInMinuteForm)
        if self.hemisphere != None:
            returnString = returnString + self.hemisphere
        return returnString
        
        pass
    
    # Returns angle in decimal form
    def getDegrees(self):
        # Raises an error if the parameter is of the wrong type
        if isinstance(self.angle, int) :
            self.angle = float(self.angle)
        elif not isinstance(self.angle, float) :
            raise ValueError("Angle.getString:  The angle has not been stored properly in this object")

        return self.angle
        pass

    def getHemisphere(self):
        return self.hemisphere

    def getTangent(self):
        angleInRads = math.pi * (self.angle/180)
        return math.tan(angleInRads)
    
    def getInRadians(self, degreeAngle = None):
        if degreeAngle == None:
            return math.pi * (self.angle/180)
        else:
            return math.pi * (degreeAngle/180)
    
    def getSine(self):
        angleInRads = math.pi * (self.angle/180)
        return math.sin(angleInRads)
    
    def getCosine(self):
        angleInRads = math.pi * (self.angle/180)
        return math.cos(angleInRads)
    
    def getArcSine(self):
        angleInRads = math.pi * (self.angle/180)
        return math.asin(angleInRads)
    
    def getArcCosine(self):
        angleInRads = math.pi * (self.angle/180)
        return math.acos(angleInRads)