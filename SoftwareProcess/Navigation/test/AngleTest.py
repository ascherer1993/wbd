'''
Created on Sep 11, 2016

@author: Aaron
'''
import unittest
import Navigation.prod.Angle as angle 
from test.test_typechecks import Integer

class Test(unittest.TestCase):

    

    def setUp(self):
        self.angleObject1 = angle.Angle()
        self.angleObject2 = angle.Angle()
        self.angleObject3 = angle.Angle()
        self.angleObject2.angle = 20
        self.angleObject3.angle = -40
        pass


    def tearDown(self):
        self.angleObject1 = None
        self.angleObject2 = None
        self.angleObject3 = None
        pass


    def test100_010_isInstanceOfAngle(self):
        self.assertIsInstance(angle.Angle(), angle.Angle)
        pass

    def test101_010_setDegreesSuccess(self):
        #Type checking
        self.assert_(isinstance(self.angleObject1.setDegrees(10), float))
        
        #Value checking
        self.assert_(self.angleObject1.setDegrees(25) == 25, "Did not set angle correctly")
        self.assert_(self.angleObject1.setDegrees(25.1) == 25.1, "Did not set angle correctly")
        self.assert_(self.angleObject1.setDegrees(375) == 15, "Did not set angle correctly")
        self.assert_(self.angleObject1.setDegrees(-15) == 345, "Did not set angle correctly")
#         print(angleObject.getDegrees())
        pass
    
    def test101_020_setDegreesFail(self):
        self.assertRaises(ValueError, self.angleObject1.setDegrees, "25")
        pass
 
    def test102_010_setDegreesAndMinutesSuccess(self):
        self.assert_(self.angleObject1.setDegreesAndMinutes("25d6.0") == 25.1, "Did not set angle correctly")
        self.assert_(self.angleObject1.setDegreesAndMinutes("0d0") == 0, "Did not set angle correctly")
        pass
    
    def test102_020_setDegreesAndMinutesFail(self):
        self.assertRaises(ValueError, self.angleObject1.setDegreesAndMinutes, "25d10y")
        self.assertRaises(ValueError, self.angleObject1.setDegreesAndMinutes, "25d")
        self.assertRaises(ValueError, self.angleObject1.setDegreesAndMinutes, "2")
        self.assertRaises(ValueError, self.angleObject1.setDegreesAndMinutes, "5.5d14")
        pass
    
    def test103_010_addSuccess(self):
        self.assert_(self.angleObject1.add(self.angleObject2) == 20, "Did not set angle correctly")
        pass
    
    def test103_010_addFail(self):
        pass
    
    def test104_010_subtractSuccess(self):
        self.assert_(self.angleObject1.setDegrees(-15) == 345, "Did not set angle correctly")
        pass
    
    def test104_020_subtractFail(self):
        pass
    
    def test105_010_getStringTestSuccess(self):
        self.assert_(self.angleObject1.setDegrees(-15) == 345, "Did not set angle correctly")
        
        # Setting angle without using the method is for testing purposes, as those methods are checked elsewhere
        self.angleObject1.angle = 25
        self.assert_(self.angleObject1.getString() == "25d0.0", "Your method must be broken")
        
        self.angleObject1.angle = 25.8        
        self.assert_(self.angleObject1.getString() == "25d48.0", "Your method must be broken")
        
        pass
    def test105_020_getStringTestFail(self):
        self.assert_(self.angleObject1.getString() == "0d0.0", "Your method must be broken")
        
        # Setting angle without using the method is for testing purposes, as those methods are checked elsewhere
        self.angleObject1.angle = 25
        self.assert_(self.angleObject1.getString() == "25d0.0", "Your method must be broken")
        
        self.angleObject1.angle = 25.8        
        self.assert_(self.angleObject1.getString() == "25d48.0", "Your method must be broken")
        
        pass

    
    def test106_010_getDegreesTestSuccess(self):
        self.assert_(self.angleObject1.setDegrees(-15) == 345, "Did not set angle correctly")
        
        # Setting angle without using the method is for testing purposes, as those methods are checked elsewhere        
        self.angleObject1.angle = 25
        self.assert_(self.angleObject1.getDegrees() == 25, "Your method must be broken")
        
        self.angleObject1.angle = 25.8        
        self.assert_(self.angleObject1.getDegrees() == 25.8, "Your method must be broken")
        
        pass
    
    def test106_020_getDegreesTestFail(self):
        self.assert_(self.angleObject1.getDegrees() == 0, "Your method must be broken")
        
        # Setting angle without using the method is for testing purposes, as those methods are checked elsewhere        
        self.angleObject1.angle = 25
        self.assert_(self.angleObject1.getDegrees() == 25, "Your method must be broken")
        
        self.angleObject1.angle = 25.8        
        self.assert_(self.angleObject1.getDegrees() == 25.8, "Your method must be broken")
        
        pass

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.test100_010_setDegrees']
    unittest.main()