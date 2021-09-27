import unittest
import cube

class coneTest(unittest.TestCase):

    #passing tests
    
    #Surface Area Tests
    def test_surfaceArea1(self):
        assert(cube.surfaceArea(5) == 150)

    #Volume Tests    
    def test_volume1(self):
        assert(cube.volume(5) == 125)

    #Lateral Surface Area Tests
    def test_latSurfaceArea1(self):
        assert(cube.latSurfaceArea(5) == 100)
        
    #failing test
    def test_volumeFail(self):
       assert(cube.volume(5) == 0)

if __name__ == '__main__':
    unittest.main()