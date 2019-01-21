#! /usr/bin/python
#  Author: Ganesh Girase <ganeshgirase@gmail.com>
#         
"""This module defines Shape base exception."""

import sys

class TestError(Exception):

  """Base class for all exceptions can be raised in Test 
     Framework
  """
  def __init__(self, message='', **kwargs):
    """Constructor for the base framework exception.

      Args:
        message(str): The exception message.
    """
    message = "\nError: %s !!\n" %(message)
    super(TestError, self).__init__(message)

class InvalidInputError(TestError):
  """
  If input isn't valid for any particular shape,
  this exception will be raised by shape program
  """
  pass

class RunTimeError(TestError):
  """
  If any error occurs while running workflow,
  this exception will be raised.
  """
  pass
