import unittest
import trapezoid

class trapezoidTest(unittest.TestCase):

    #passing tests

    #Area Tests
    def test_Area1(self):
        assert(trapezoid.area(5, 10, 15) == 112.5)

    #Median Tests    
    def test_Median1(self):
        assert(trapezoid.median(5, 10) == 15)

if __name__ == '__main__':
    unittest.main()