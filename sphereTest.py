import unittest
import sphere

class sphereTest(unittest.TestCase):

    #passing tests

    #Surface Area Tests
    def test_surfaceArea1(self):
        assert(sphere.surfaceArea(5) == 314.16)

    #Volume Tests    
    def test_volume1(self):
        assert(sphere.volume(5) == 523.6)
        
if __name__ == '__main__':
    unittest.main()