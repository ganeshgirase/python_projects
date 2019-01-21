#! /usr/bin/python

import json
import unittest
from workflow.lib.log import INFO,WARN,DEBUG
from workflow.lib.util import TestUtil
from workflow.exceptions.test_error import RunTimeError

class APITest(unittest.TestCase):
  """
  Test class for organizing test cases of API testing.
  """
  def setUp(self):
    """
    Setup method for every test.
    Using configuration we can also make this method as 
    setup method for class level.
    Args:
      None
    Returns:
      None
    Raises:
      RunTimeError if any issue.
    """ 
    # This can be hide in class attribute.
    config_file = "workflows/config/config.json"
    INFO("Test Config file: %s" %(config_file))
    try:
      with open(config_file, "r") as f:
        config_data = json.load(f)
    except Exception as ex:
      raise RunTimeError("Unable to load configuration data: %s" %str(ex))
    self.test_args = config_data[self._testMethodName]

  def test_json_users(self):
    """
    Test to ensure http request for list of users
    is succesful.
    STEPS:
      1. Make http request.
      2. Check if url returns json data.
      3. Validate Http response json data.
      3. Verify if json data contains mandetory data. 
    """
    url = self.test_args["url"]
    resp = TestUtil.http_request(url)

    INFO("STEP: Make HTTP request for users")
    assert resp.status_code == 200, \
      "Unable to fetch data from url '%s'" %url

    users = json.loads(resp.text)
    INFO("Every user will be having sanity check with mandate data")
    for user in users: 
      for attrib in self.test_args["mandate_params"]:
        assert user.has_key(attrib), "User data is corrupted !! It does " \
          "not have all key %s" %attrib

  def test_json_albums(self):
    """
    Test to ensure http request for list of users
    is succesful.
    STEPS:
      1. Make http request.
      2. Check if url returns json data.
      3. Validate Http response json data.
      3. Verify if json data contains mandetory data. 
    """
    url = self.test_args["url"]
    resp = TestUtil.http_request(url)

    INFO("STEP: Make HTTP request for users")
    assert resp.status_code == 200, \
      "Unable to fetch data from url '%s'" %url

    users = json.loads(resp.text)
    INFO("Every user will be having sanity check with mandate data")
    for user in users: 
      for attrib in self.test_args["mandate_params"]:
        assert user.has_key(attrib), "User data is corrupted !! It does " \
          "not have all key %s" %attrib


  def tearDown(self):
    """
    In Teardown method, we will clear all stale objects 
    and destroyes all hanging objects as well as close the
    open connections.
    """
    pass

if __name__ == "__main__":
  unittest.main()

