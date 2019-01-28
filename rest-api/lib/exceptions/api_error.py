#! /usr/bin/python
#  Author: Ganesh Girase <ganeshgirase@gmail.com>
#         
"""This module defines REST API base exception."""

import sys

class ApiError(Exception):

  """Base class for all Expression Parser exceptions.
  """
  def __init__(self, message='', **kwargs):
    """Constructor for the base framework exception.

      Args:
        message(str): The exception message.
    """
    message = "\nError: %s !!\n" %(message)
    super(ApiError, self).__init__(message)

class InvalidInputError(ApiError):
  """
  If input isn't valid for any particular shape,
  this exception will be raised by shape program
  """
  pass

class RunTimeError(ApiError):
  """
  If any error occurs while running workflow,
  this exception will be raised.
  """
  pass

class UnsupportedOperations(ApiError):
  """
  If any operation isn't supported,
  this exception will be raised.
  """
  pass
