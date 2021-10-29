import unittest
import cylinder

class cylinderTest(unittest.TestCase):

    #passing tests

    #Surface Area Tests
    def test_surfaceArea1(self):
        assert(cylinder.surfaceArea(5, 10) == 471.24)

    #Volume Tests    
    def test_volume1(self):
        assert(cylinder.volume(5, 10) == 785.4)

    #Lateral Surface Area tests
    def test_latSurfaceArea1(self):
        assert(cylinder.latSurfaceArea(5, 10) == 314.16)

    #Top and bottom area tests
    def test_topOrBottom1(self):
        assert(cylinder.topOrBottom(5) == 78.54)   

    

if __name__ == '__main__':
    unittest.main()