import unittest
import cuboid

class cuboidTest(unittest.TestCase):

    #passing tests

    #Surface Area Tests
    def test_surfaceArea1(self):
        assert(cuboid.surfaceArea(15, 10, 5) == 550)

    #Volume Tests    
    def test_volume1(self):
        assert(cuboid.volume(15, 10, 5) == 750)

    #Lateral Surface Area Tests
    def test_latSurfaceArea(self):
        assert(cuboid.latSurfaceArea(15, 10, 5) == 250)
        
    #failing test
    def test_volumeFail(self):
       assert(cuboid.volume(15, 10, 5) == 0)

if __name__ == '__main__':
    unittest.main()