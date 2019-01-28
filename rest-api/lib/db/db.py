#! /usr/bin/python
"""
Class for database function handling. 
"""
from lib.exceptions import RunTimeError

class DB(object):
  """
  Database class for CRUD operations.
  """
  def save(self, record):
    """
    Save record to database.
    Args:
      record: Record saved to the database.
    Returns:
      ret(bool): True if success else Fail.
    Raises:
      RunTimeError if any error occurs .
    """
    pass

  def select(self, entity, attributes=None, filters=None):
    """
    Retrieves record from the database.
    Args:
      entity: Database record will be etracted from specific entity
      attributes: List of attributes for entity. Default to all.
      filters: Database records will be filtered on some criteria.
    Returns:
      data: List of database records.
    Raises:
      RunTimeError if any error occurs .
    """
    pass

    
    

