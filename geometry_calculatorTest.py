import unittest
from geometry_calculator import userSelection
import sphere, cone, cylinder, cube, triangle, trapezoid, cuboid, equilateralTriangle
from unittest import mock

class mainTest(unittest.TestCase):

  #Testing if selection 1 equals sphere
  def test_selection1(self):
    assert(sphere.selection() == userSelection(1))

  #testing if selection 2 equals cylinder
  def test_selection2(self):
    assert(cylinder.selection() == userSelection(2))
        
  #testing if selection 3 equals cone
  def test_selection3(self):
    assert(cone.selection() == userSelection(3))

  #testing if selection 4 equals cube    
  def test_selection4(self):
    assert(cube.selection() == userSelection(4))

  #testing if selection 5 equals triangle
  def test_selection5(self):
    assert(triangle.selection() == userSelection(5))

  #testing if selection 6 equals trapezoid
  def test_selection6(self):
    assert(trapezoid.selection() == userSelection(6))

  #testing if selection 7 equals cuboid
  def test_selection7(self):
    assert(cuboid.selection() == userSelection(7))

  #testing if selection 8 equals equilateralTriangle
  def test_selection8(self):
    assert(equilateralTriangle.selection() == userSelection(8))

#failing test 
  def test_Selection1Fail(self):
    assert(sphere.selection() == userSelection(2))
    
if __name__ == '__main__':
    unittest.main()