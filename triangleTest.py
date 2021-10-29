import unittest
import triangle

class cuboidTest(unittest.TestCase):

    #passing tests

    #Perimeter Tests
    def test_Perimeter1(self):
        assert(triangle.perimeter(7, 5, 6) == 18)

    #Semi Perimeter Tests    
    def test_semiPerimeter1(self):
        assert(triangle.semiPerimeter(7, 5, 6) == 9)

    #Area Tests
    def test_Area1(self):
        assert(triangle.area(7, 5, 6) == 14.7)

if __name__ == '__main__':
    unittest.main()