import unittest
import equilateralTriangle

class equilateralTriangleTest(unittest.TestCase):

    #passing tests

    #Area Tests
    def test_Area1(self):
        assert(equilateralTriangle.area(5) == 10.83)

    #Perimeter Tests    
    def test_perimeter1(self):
        assert(equilateralTriangle.perimeter(5) == 15)

    #Semi Perimeter Tests
    def test_semiPerimeter1(self):
        assert(equilateralTriangle.semiPerimeter(5) == 7.5)

    #Altitude Tests
    def test_Altitude1(self):
        assert(equilateralTriangle.altitude(5) == 4.33) 

if __name__ == '__main__':
    unittest.main()