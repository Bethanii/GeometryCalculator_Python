import unittest
import cone

class coneTest(unittest.TestCase):

    #Slant Tests
    def test_slant1(self):
        assert(cone.slant(5, 10) == 11.18)
    
    #Surface Area Tests
    def test_surfaceArea1(self):
        assert(cone.surfaceArea(5, 10) == 254.16)

    #Volume Tests    
    def test_volume1(self):
        assert(cone.volume(5, 10) == 261.8)

    #Lateral Surface Area Tests
    def test_latSurfaceArea1(self):
        assert(cone.latSurfaceArea(5, 10) == 175.62)

if __name__ == '__main__':
    unittest.main()