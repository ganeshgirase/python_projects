#! /usr/bin/python
"""
Log package for API testing project

Author: Ganesh Girase<ganesh.girase@gmail.com>
"""

import logging
import logging.config
import traceback

def ERROR(msg):
  """Logs an error message.

  Args:
    msg (str): The message to be logged.

  Returns:
    None
  """
  logging.api_logger.error(msg, extra=__extra())

def WARN(msg):
  """Logs a warning message.

  Args:
    msg (str): The message to be logged.

  Returns:
    None
  """
  logging.api_logger.warning(msg, extra=__extra())

def INFO(msg):
  """Logs an info message.

  Args:
    msg (str): The message to be logged.

  Returns:
    None
  """
  logging.api_logger.info(msg, extra=__extra())

def DEBUG(msg):
  """Logs a debug message.

  Args:
    msg (str): The message to be logged.


  Returns:
    None
  """
  logging.api_logger.debug(msg, extra=__extra())

# Private function
def __extra():
  """Function to pass the callers name and line number.
  Returns:
    A dictionary with 'stage', 'step' and 'file_line' details
  """
  frame = traceback.extract_stack()[-3]
  file_name = frame[0].split("/")[-1]
  file_line = frame[1]
  return {
    'stage': logging.stage,
    'step': logging.step,
    'file_line': "%s:%s" % (file_name, file_line)
  }

def __set_default_config(level=logging.INFO):
  """Sets the default logging config.
  Args:
    level(int): Log level, Default: logging.INFO
  """
  handler = logging.StreamHandler()
  formatter = logging.Formatter(
    '%(asctime)s %(levelname)-5s %(file_line)s %(message)s',
    '%Y-%m-%d %H:%M:%S')
  handler.setFormatter(formatter)
  logging.api_logger.addHandler(handler)
  logging.api_logger.setLevel(level)
  logging.api_logger.propagate = 0


def configure(log_dir=None, log_file='api_test.log', level=logging.INFO):
  """Initializes and configures the loggers.

  Args:
    log_dir (str): The log folder where the logs will be created
                  Default is under logs/
    log_file (str): The log file to send the logs to.
                    Defaults to 'api_test.log'.
    level (str): The log level.
                 Defaults to 'INFO'
  Returns:
    None
  """

  # Custom variables
  logging.marker = "-" * 60
  logging.step = 1
  logging.stage = ''
  FORMAT = '%(asctime)-15s %(user)-8s %(message)s'
  logging.basicConfig(format=FORMAT)

  # Create the loggers
  logging.api_logger = logging.getLogger('api_test')
  __set_default_config(level=level)

configure()
