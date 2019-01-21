#! /usr/bin/python
"""
All common utility functions needed by Test Framework.
Author: Ganesh Girase <ganeshgirase@gmail.com>
"""

import requests
from workflow.exceptions.test_error import *
from workflow.lib.log import INFO,ERROR

class TestUtil(object):
  """
  Utility functions commone from framework.
  """
  @staticmethod
  def http_request(url, method="GET"):
    """
    Handle HTTP web requests
    Args:
      url(string): Http web url.
      method: HTTP Request method type
    Returns:
      HTTP Response
    Raises:
      RunTimeError if any issues occurs.
    """
    response = requests.get(url) 
    return response
