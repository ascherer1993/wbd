from test.test_typechecks import Integer
class Angle():
    def __init__(self):
        self.angle = 0
        pass
    
    def setDegrees(self, degrees):
        if not isinstance(degrees, float) and not isinstance(degrees, int) :
            raise ValueError("Angle.setDegrees:  The parameter provided was not a integer or float")
        self.angle = degrees % 360
        return self.angle
        #returns angle as degrees and portions of degrees as a single floating point number mod 360
        pass
    
    def setDegreesAndMinutes(self, angleString):
        if 'd' in angleString:
            newString = angleString.split("d")
            if (len(newString) != 2 and not newString[1].isdigit()) :
                raise ValueError("Angle.setDegreesAndMinutes:  The correct format was not provided. #d#.#")
            
            
            minuteLength = len(newString[1])
            
            if '.' in newString[1] :
                periodPosition = newString[1].index('.')
                if periodPosition != minuteLength - 2 and periodPosition != -1 :
                    raise ValueError("Angle.setDegreesAndMinutes:  The correct format was not provided. #d#.#")
            else :
                i = 1
            
            minuteInDecimal = float(newString[1])/60
            self.angle = float(newString[0]) + minuteInDecimal
        else :
            return ValueError("Angle.setDegreesAndMinutes:  The correct format was not provided. #d#.#")
        
        return self.angle
        # split on 'd', 45d10.1
        #returns angle as degrees and portions of degrees as a single floating point number mod 360
        #pass
    
    def add(self, angle):
        #returns angle as degrees and portions of degrees as a single floating point number mod 360
        pass
    
    def subtract(self, angle):
        #returns angle as degrees and portions of degrees as a single floating point number mod 360
        pass
    
    def compare(self, angle):
        # -1 if less than parameter
        # 0 if equal
        # 1 if greater than parameter
        pass
    
    def getString(self):
        if '.' in self.angle :
            degreesArray = self.angle.split('.')
            
            decimalInMinuteForm = degreesArray[1] * 60
            self.angle = degreesArray[0] + decimalInMinuteForm
            return self.angle
        else :
            return self.angle
        
        pass
    
    def getDegrees(self):
        #returns angle as degrees and portions of degrees as a single floating point number mod 360
        return self.angle
        pass