'''
Created on Sep 11, 2016

@author: Aaron
'''
import unittest
import Navigation.prod.Angle as angle 

class Test(unittest.TestCase):

    

    def setUp(self):
        pass


    def tearDown(self):
        pass


    def test100_010_isInstanceOfAngle(self):
        self.assertIsInstance(angle.Angle(), angle.Angle)
        pass

    def test101_010_setDegrees(self):
        angleObject = angle.Angle()
#         try:
#             angleObject.setDegrees("2d5.1")
#             print(angleObject.getDegrees())
#         except ValueError as e:
#             print(e)
        self.assert_(angleObject.setDegrees(25) == 25, "Did not set angle correctly")
        self.assert_(angleObject.setDegrees(25.1) == 25.1, "Did not set angle correctly")
        self.assert_(angleObject.setDegrees(375) == 15, "Did not set angle correctly")
        self.assert_(angleObject.setDegrees(-15) == 345, "Did not set angle correctly")
#         print(angleObject.getDegrees())
        pass
    
    def test101_020_setDegreesStringCheck(self):
        angleObject = angle.Angle()
        self.assertRaises(ValueError, angleObject.setDegrees, "25")
        pass

    def test102_010_setDegreesAndMinutes(self):
        angleObject = angle.Angle()
        self.assertRaises(ValueError, angleObject.setDegreesAndMinutes, "25d10y")
        pass
    
    def test107_010_getDegreesTest(self):
        angleObject = angle.Angle()
        self.assertRaises(ValueError, angleObject.setDegreesAndMinutes, "25d10y")
        pass

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.test100_010_setDegrees']
    unittest.main()