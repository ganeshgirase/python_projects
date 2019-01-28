#! /usr/bin/python
#
# Calendar for listing & hosting time slot for interview discussion
# between different parties. i.e, interviewer & interviewee
#
# Author: Ganesh Girase <ganeshgirase@gmail.com>
#
import flask
import json
import sys
#from lib.exceptions.api_error import RunTimeError
from flask import Flask, make_response, request

class InterviewCalendarApi(object):
  """
  Calendar for setting up interview time slot.  
  """
  # Class level declaration for app
  APP = Flask(__name__)
  JSON_TYPE = 'application/json'
  HEADERS = {'Content-Type': JSON_TYPE}
  DB_FILE = "../lib/db/TimeSlot.db"
  
  @staticmethod
  @APP.route("/set_available_timeslot", methods=['POST'])
  def set_available_time_slot():
    """
    Sets the personal available time slot in calendar
    """
    if request.content_type != 'application/json':
      error = json.dumps({'error': 'Invalid Content Type'})
      return make_response(error, 400, InterviewCalendarApi.HEADERS)

    data = request.json
    # For Temporary purpose, stored in flat file database
    with open(InterviewCalendarApi.DB_FILE, "a+") as fd:
      record = "%s|%s|%s|%s\n" %(data["Category"], data["Name"],
        data["Email"], ",".join(data["AvailablityDateTime"]))
      fd.write(record)
    msg = json.dumps({"Status": "Success"})
    return make_response(msg, 200, InterviewCalendarApi.HEADERS)

  @staticmethod
  @APP.route("/get_available_timeslot", methods=['GET'])
  def get_available_time_slot():
    """
    Gets the ideal time slot to arrange interview
    between different parties.
    """
    try:
      time_slot_set_list = list()
      # Read all time slot from database
      with open(InterviewCalendarApi.DB_FILE, "r") as fd:
        for line in fd:
          time_slot_list = list()
          (_,_,_, time_slots) = line.strip().split("|")
          for time_slot in time_slots.split(","):
            (from_time_slot, to_time_slot) = list(map(int, time_slot.split("-")))
            time_slot_list.extend(range(from_time_slot, (to_time_slot + 1)))
          # Get all available time slot for every user
          time_slot_set_list.append(set(time_slot_list))
 
      # Find common time slot between multiple parties
      available_slots = list(set.intersection(*time_slot_set_list))

      msg = json.dumps({"Status": "Success", "available_slots": available_slots})
      return make_response(msg, 200, InterviewCalendarApi.HEADERS)
    except:
      err_msg = sys.exc_info()
      error = json.dumps({'error': 'Unable to find time slot due to error: %s' %str(err_msg)})
      return make_response(error, 401, InterviewCalendarApi.HEADERS)

if __name__ == "__main__": 
  InterviewCalendarApi.APP.run(debug=True)
  
  
  
