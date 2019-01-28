#! /usr/bin/python
#
# Test class for resting REST API
# Author: Ganesh Girase <ganesh.girase@gmail.com>

import unittest
import requests
import json

class APITest(unittest.TestCase):
  """ 
  Tests API GET, POST, DELETE functionality.
  """
  def _test_set_interviewer_availability(self):
    """
    Test if you can set the interviewer avaiability
    """
    headers = {'content-type' : 'application/json'}
    data1 = {
           "Name": "Json Holder", 
           "Email": "Json@foobar.com",
           "Category": "1",
           "AvailablityDateTime": ["2019012809-2019012814", "2019013109-2019013114"]
           }

    data2 = {
           "Name": "Kelly McBar",
           "Email": "kelly@foobar.com",
           "Category": "1",
           "AvailablityDateTime": ["2019013111-2019013115", "2019012814-2019012816"]
           }
    for data in (data1, data2):
      url = "http://127.0.0.1:5000/set_available_timeslot"
      resp = requests.post(url, data=json.dumps(data), headers=headers)
      assert resp.status_code == 200, "Setting time slot availability failed"


  def _test_set_interviewee_availability(self):
    """
    Test if you can set the interviewee avaiability
    """
    headers = {'content-type' : 'application/json'}
    data = {
           "Name": "Victor Joshua",
           "Email": "vic@gmail.com",
           "Category": "2",
           "AvailablityDateTime": ["2019012814-2019012815", "2019013113-2019013114", "2019012614-2019012615"]
           }

    url = "http://127.0.0.1:5000/set_available_timeslot"
    resp = requests.post(url, data=json.dumps(data), headers=headers)
    assert resp.status_code == 200, "Setting time slot availability failed"

  def test_get_available_slot_for_all(self):
    """
    Test if API is able to find correct time slot available 
    for both parties i.e, interview & interviewee
    """
    url = "http://127.0.0.1:5000/get_available_timeslot"
    resp = requests.get(url)
    data= json.loads(resp.text)
    a = [2019013113, 2019013114, 2019012814]
    assert resp.status_code == 200, "Unable to get available time slot !"
    assert len(set(a).difference(data['available_slots'])) == 0  \
       and len(set(data['available_slots']).difference(a)) == 0, \
      "Unable to get correct available time slot !" 

if __name__ == "__main__":
  unittest.main()
  
  


  
