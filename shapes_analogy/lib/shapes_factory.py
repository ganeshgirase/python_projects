#! /usr/bin/python
# Author: Ganesh Girase <ganeshgirase@gmail.com>
#
# Decide type of shape operation needed and
# pass object of same type from shapes factory.

import lib.exceptions.shapes_error
import lib.shapes.triangle

from lib.exceptions.shapes_error import UnsupportedOperations
from lib.shapes.triangle import Triangle

class ShapesFactory(object):
  """
  Factory class for all available shapes
  """
  def __init__(self):
    """
    Initialization method for Shapes factory class.
    """
    pass

  def get_shape_handler(self, shape_type):
    """
    On basis of shape type, user wanto to play with,
    pass respective shape handler.
    Args:
      shape_type(str): Type of shape for you need handler.
    Returns:
      shape_handler(object): Object of shape handler class.
    Raises:
      UnsupportedOperations: if shape_type isn't supported.
    """
    # TODO
    # This also can be achieved using below two ways
    #  1. Use __import__ method to load all shapes within shapes directory.
    #  2. Using __metaclass__ to auto register any new shape defined under 
    #     shapes directory.
    if shape_type.upper() == "TRIANGLE":
      shape_handler = Triangle()
    else:
      err_msg = "Operations for shape %s isn't supported" %(shape_type)
      raise UnsupportedOperations(err_msg)
    return shape_handler
