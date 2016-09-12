'''
    Created on 9/10/2016
    Edited on: 9/11/2016

    @author: Aaron Scherer
'''
import unittest
import Navigation.prod.Angle as Angle 

class Test(unittest.TestCase):

    

    def setUp(self):
        # Creates objects
        self.angleObject1 = Angle.Angle()
        self.angleObject2 = Angle.Angle()
        self.angleObject3 = Angle.Angle()
        self.angleObject4 = Angle.Angle()
        self.angleObject2.angle = 20
        self.angleObject3.angle = -40
        self.angleObject4.angle = 20
        pass


    def tearDown(self):
        # Resets objects
        self.angleObject1 = None
        self.angleObject2 = None
        self.angleObject3 = None
        self.angleObject4 = None
        pass


    def test100_010_isInstanceOfAngle(self):
        self.assertIsInstance(Angle.Angle(), Angle.Angle)
        pass

    def test101_010_setDegreesSuccess(self):
        # Type checking
        self.assert_(isinstance(self.angleObject1.setDegrees(10), float))
        
        # Value checking
        self.assert_(self.angleObject1.setDegrees(25) == 25, "Did not set angle correctly")
        self.assert_(self.angleObject1.setDegrees(25.1) == 25.1, "Did not set angle correctly")
        self.assert_(self.angleObject1.setDegrees(375) == 15, "Did not set angle correctly")
        self.assert_(self.angleObject1.setDegrees(-15) == 345, "Did not set angle correctly")
#         print(angleObject.getDegrees())
        pass
    
    def test101_020_setDegreesFail(self):
        # Type checking
        self.assertRaises(ValueError, self.angleObject1.setDegrees, "25")

        pass
 
    def test102_010_setDegreesAndMinutesSuccess(self):
        # Type checking
        self.assert_(isinstance(self.angleObject1.setDegreesAndMinutes("10d0.0"), float))
        
        # Value checking
        self.assert_(self.angleObject1.setDegreesAndMinutes("25d6.0") == 25.1, "Did not set angle correctly")
        self.assert_(self.angleObject1.setDegreesAndMinutes("0d0") == 0, "Did not set angle correctly")
        self.assert_(self.angleObject1.setDegreesAndMinutes("-10d6") == 349.9, "Did not set angle correctly")
        pass
    
    def test102_020_setDegreesAndMinutesFail(self):
        self.assertRaises(ValueError, self.angleObject1.setDegreesAndMinutes, "25d10y")
        self.assertRaises(ValueError, self.angleObject1.setDegreesAndMinutes, "25d")
        self.assertRaises(ValueError, self.angleObject1.setDegreesAndMinutes, "2")
        self.assertRaises(ValueError, self.angleObject1.setDegreesAndMinutes, "5.5d14")
        self.assertRaises(ValueError, self.angleObject1.setDegreesAndMinutes, "xd10")
        self.assertRaises(ValueError, self.angleObject1.setDegreesAndMinutes, "")
        self.assertRaises(ValueError, self.angleObject1.setDegreesAndMinutes, "d14")
        pass
    
    def test103_010_addSuccess(self):
        # Type checking
        self.assert_(isinstance(self.angleObject1.add(self.angleObject2), float))
        
        # Resets for next test
        self.angleObject1 = Angle.Angle()
        
        # Value checking
        self.assert_(self.angleObject1.add(self.angleObject2) == 20, "The two angles were not added correctly")
        self.assert_(self.angleObject2.add(self.angleObject3) == 340, "The two angles were not added correctly")
        pass
    
    def test103_010_addFail(self):
        self.assertRaises(ValueError, self.angleObject1.add, 8)
        self.assertRaises(ValueError, self.angleObject1.add, "test")
        self.assertRaises(ValueError, self.angleObject1.add, "24d14")
        pass
    
    def test104_010_subtractSuccess(self):
        # Type checking
        self.assert_(isinstance(self.angleObject1.subtract(self.angleObject2), float))
        
        # Resets for next test
        self.angleObject1 = Angle.Angle()
        
        # Value checking
        self.assert_(self.angleObject1.subtract(self.angleObject2) == 340, "There was an error in the calculations")
        self.assert_(self.angleObject2.subtract(self.angleObject4) == 0, "There was an error in the calculations")
        pass
    
    def test104_020_subtractFail(self):
        self.assertRaises(ValueError, self.angleObject1.subtract, 8)
        self.assertRaises(ValueError, self.angleObject1.subtract, "test")
        pass
    
    def test105_010_compareSuccess(self):
        # Type checking
        self.assert_(isinstance(self.angleObject1.compare(self.angleObject2), int))
        
        # Value checking
        self.assert_(self.angleObject1.compare(self.angleObject2) == -1, "There was an error in the calculations")
        self.assert_(self.angleObject2.compare(self.angleObject3) == 1, "There was an error in the calculations")
        self.assert_(self.angleObject2.compare(self.angleObject4) == 0, "There was an error in the calculations")
        pass
    
    def test105_020_compareFail(self):
        self.assertRaises(ValueError, self.angleObject1.compare, 8)
        self.assertRaises(ValueError, self.angleObject1.compare, "test")
        pass
    
    def test106_010_getStringTestSuccess(self):
        # Type checking
        self.assert_(isinstance(self.angleObject1.getString(), str))
        
        # Value checking
        self.assert_(self.angleObject1.getString() == "0d0.0", "Your method must be broken")
        self.assert_(self.angleObject2.getString() == "20d0.0", "Your method must be broken")
        
        pass
    def test106_020_getStringTestFail(self):
        # No good way to test
        
        pass

    
    def test107_010_getDegreesTestSuccess(self):
        # Type checking
        self.assert_(isinstance(self.angleObject1.getDegrees(), float))
        
        # Value checking
        self.assert_(self.angleObject1.getDegrees() == 0, "Your method must be broken")
        self.assert_(self.angleObject2.getDegrees() == 20, "Your method must be broken")
        
        pass
    
    def test107_020_getDegreesTestFail(self):
        # no good way to test
        
        pass

if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.test100_010_setDegrees']
    unittest.main()
