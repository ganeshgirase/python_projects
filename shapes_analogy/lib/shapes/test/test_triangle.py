#! /usr/bin/python

# Test class for Triangle.

import unittest
import lib.shapes.triangle

from lib.shapes.triangle import Triangle, TriangleOperations

class TestTriangle(unittest.TestCase):
  """
  Unit test methods for Triangle and it's relative operations.
  """
  def test_triangle_type(self):
    # Test for equilateral type triangle
    assert TriangleOperations.get_triangle_type(3, 3, 3) == "equilateral", \
      "Test case failed for equilateral type of triangle !"
    # Test for equilateral type isosceles
    assert TriangleOperations.get_triangle_type(3, 4, 4) == "isosceles", \
      "Test case failed for isosceles type of triangle !"
    # Test for equilateral type scalene
    assert TriangleOperations.get_triangle_type(3, 4, 5) == "scalene", \
      "Test case failed for scalene type of triangle !"

  def test_triangle_validate_input_params(self):
    """
    Validate input parameters of Triangle shape.
    """
    obj = Triangle()
    # Test to validate triangle input parameeters 
    assert obj.validate_input_params([1, 2, 3]) == True, \
      "Failed to validate Triangle input parameters"

if __name__ == "__main__":
  unittest.main()

