#! /usr/bin/python
#
# Test class for shape handler from facoty.
#
# Author: Ganesh Girase <ganeshgirase@gmail.com>

import unittest
import lib.shapes_factory

from lib.shapes_factory import ShapesFactory

class TestShapesFactory(unittest.TestCase):
  """
  Unit test methods for Shape Factory which pass
  respective shape handlers.
  """
  def test_shape_handler(self):
    # Test for triangle type shape
    obj = ShapesFactory()
    shape_type = "Triangle"
    handler = obj.get_shape_handler("Triangle")
    # Test for shape handler
    assert handler.__class__.__name__ == shape_type, \
      "Shape factory return wrong handler !!"

if __name__ == "__main__":
  unittest.main()

