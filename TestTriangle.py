import unittest
from Triangle import classifyTriangle

# filepath: c:\Spurthi\Stevens\Classes\Junior Year Spring\SSW - 567\hw-06b\test_TestTriangle.py

class TestTriangles(unittest.TestCase):

    def testRightTriangleA(self): 
        self.assertEqual(classifyTriangle(3, 4, 5), 'Right', '3, 4, 5 is a Right triangle')

    def testRightTriangleB(self): 
        self.assertEqual(classifyTriangle(5, 3, 4), 'Right', '5, 3, 4 is a Right triangle')
        
    def testEquilateralTriangles(self): 
        self.assertEqual(classifyTriangle(1, 1, 1), 'Equilateral', '1, 1, 1 should be equilateral')

    def testIsoscelesTriangle(self):
        self.assertEqual(classifyTriangle(2, 2, 3), 'Isosceles', '2, 2, 3 should be isosceles')

    def testScaleneTriangle(self):
        self.assertEqual(classifyTriangle(3, 4, 6), 'Scalene', '3, 4, 6 should be scalene')

    def testInvalidTriangleA(self):
        self.assertEqual(classifyTriangle(0, 0, 0), 'InvalidInput', '0, 0, 0 should be invalid')

    def testInvalidTriangleB(self):
        self.assertEqual(classifyTriangle(-1, 2, 3), 'InvalidInput', '-1, 2, 3 should be invalid')

    def testNotATriangle(self):
        self.assertEqual(classifyTriangle(1, 10, 12), 'NotATriangle', '1, 10, 12 should not form a triangle')

if __name__ == '__main__':
    unittest.main()