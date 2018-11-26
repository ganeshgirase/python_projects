#! /usr/bin/python
#
# Base class for all shape class
#
# Author: Ganesh Girase <ganeshgirase@gmail.com>
""" Abstract base class for every type of shape """

import abc

class Shape(object):
  """
  Abstract class for shapes
  """
  __metaclass__  = abc.ABCMeta

  def __init__(self):
    """
    Initialization method for abstract class Shape
    """
    pass

  @abc.abstractmethod 
  def get_input_params(self):
    """
    Gets input parameters from user. 
    """
    pass
    
  @abc.abstractmethod 
  def validate_input_params(self, *args, **kwargs):
    """
    Validates input parameters from user.
    """
    pass

  @abc.abstractmethod 
  def execute(self):
    """
    Execute relative shape actions.
    """
    pass
