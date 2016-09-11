from test.test_typechecks import Integer
import re

class Angle():
    def __init__(self):
        self.angle = 0.0
        pass
    
    def setDegrees(self, degrees):
        if not isinstance(degrees, float) and not isinstance(degrees, int) :
            raise ValueError("Angle.setDegrees:  The parameter provided was not a integer or a float")
        self.angle = round(degrees % 360, 1)
        return self.angle
    
        pass
    
    def setDegreesAndMinutes(self, angleString):
        
        angleString = angleString.strip() #This was done to strip out white space before the regular expression
        
        #For this project I got to learn regex! 
        #Below, the string parameter is checked to make sure that it matches very specific requirements
        #I then find all instances of those requirements in the string, and make sure it matches the original string.
        #If it does, the parameter is in the right format and can be used
        regex = "^(-?[0-9]+d[0-9]+\.?[0-9]?)?" #    xdy.y  x is any positive or negative number that represents the degrees and the y's are the minutes
        regexMatch = re.findall(regex, angleString)
        
        #checks to make sure there is only one exact match
        if len(regexMatch) != 1 or len(regexMatch[0]) != len(angleString) :
            raise ValueError("Angle.setDegreesAndMinutes:  The correct format was not provided. Please provide a format that matches #d# or #d#.#")
        
        # splits string at the symbol d
        newString = angleString.split('d')
        
        #converts from minutes into decimal to store
        minuteInDecimal = float(newString[1])/60
        #stores one decimal place mod 360
        floatedDegrees = float(newString[0])
        
        #this handles negative degrees
        if floatedDegrees < 0 :
            self.angle = round((floatedDegrees - minuteInDecimal) % 360, 1)
        else :    
            self.angle = round((floatedDegrees + minuteInDecimal) % 360, 1)
        return self.angle
        
        pass
    
    def add(self, angle):
        if not isinstance(angle, Angle) :
            raise ValueError("Angle.add:  The parameter you have provided is not an instance of the Angle class.")
        self.angle = round((self.angle + angle.angle) % 360, 1)
        return self.angle
        pass
    
    def subtract(self, angle):
        if not isinstance(angle, Angle) :
            raise ValueError("Angle.subtract:  The parameter you have provided is not an instance of the Angle class.")
        self.angle = round((self.angle - angle.angle) % 360, 1)
        return self.angle
        pass
    
    def compare(self, angle):
        if not isinstance(angle, Angle) :
            raise ValueError("Angle.compare:  The parameter you have provided is not an instance of the Angle class.")
        try :
            if self.angle < angle.angle :
                return -1
            elif self.angle == angle.angle :
                return 0
            elif self.angle > angle.angle :
                return 1
        except :
            raise ValueError("Angle.compare:  The two angles could not be compared")
        pass
    
    def getString(self):
        if isinstance(self.angle, int) :
            self.angle = float(self.angle)
        elif not isinstance(self.angle, float) :
            raise ValueError("Angle.getString:  The angle has not been stored properly in this object")
        
        degreesArray = str(self.angle).split('.')
            
        decimalInMinuteForm = round(float('.' + degreesArray[1]) * 60, 1)
        returnString = str(degreesArray[0]) + "d" + str(decimalInMinuteForm)
        return returnString
        
        pass
    
    def getDegrees(self):
        if isinstance(self.angle, int) :
            self.angle = float(self.angle)
        elif not isinstance(self.angle, float) :
            raise ValueError("Angle.getString:  The angle has not been stored properly in this object")

        return self.angle
        pass