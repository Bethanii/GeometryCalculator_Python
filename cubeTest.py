import unittest
import cube

class coneTest(unittest.TestCase):

    #passing tests
    
    #Surface Area Tests
    def test_surfaceArea1(self):
        assert(cube.surfaceArea(5, 10) == 254.16)

    #Volume Tests    
    def test_volume1(self):
        assert(cube.volume(5, 10) == 261.8)

    #Lateral Surface Area Tests
    def test_latSurfaceArea1(self):
        assert(cube.latSurfaceArea(5, 10) == 175.62)
        
    #failing test
    def test_volumeFail(self):
       assert(cube.volume(5, 10) == 0)

if __name__ == '__main__':
    unittest.main()