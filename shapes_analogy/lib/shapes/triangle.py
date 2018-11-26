#
# Triangle shape related operations will be performed.
#
# Author: Ganesh Girase <ganeshgirase@gmail.com>

import lib.exceptions.shapes_error
import lib.shapes.shape

from lib.shapes.shape import Shape
from lib.exceptions.shapes_error import InvalidInputError

class TriangleOperations:
  """
  Handles triangle related operations.
  """ 
  @staticmethod
  def get_triangle_type(length_a, length_b, length_c):
    """
    Determine type of triangle.
    Args:
      length_a(int): Length of triangle side
      length_b(int): Length of triangle side
      length_c(int): Length of triangle side
    Returns:
      type_of_triangle: Type of triangle.
    """
    type_of_triangle = None
    if not all((length_a, length_b, length_c)):
      return None

    if length_a == length_b == length_c:
      type_of_triangle = "equilateral"
    elif (length_a == length_b) or \
         (length_b == length_c) or \
         (length_a == length_c):
      type_of_triangle = "isosceles"
    else:
      type_of_triangle = "scalene"
    return type_of_triangle
   
  @staticmethod
  def get_area(cls, length_a, length_b, length_c):
    #TODO: Calculate area of circle
    pass
  

class Triangle(Shape):
  """
  Triangle shape handling
  """
  def __init__(self):
    """
    Initialization method for Triangle class
    """
    pass

  def get_input_params(self):
    """
    Get input parameters from user. 
    Args: 
      None
    Returns:
      input_params(string): Triangle lenght string separated
                            by space.
    """
    input_params =  \
      raw_input("\t\t\tPlease enter triangle lenghts separated by space: ")
    return input_params.split(" ")
    
  def validate_input_params(self, triangle_lengths):
    """
    Validate triangle lengths passed by user.
    Args:
      triangle_lengths(list): List of triangle lengths.
    Returns:
      bool: True if input is valid
    Raises:
      InvalidInputError: Raises error if input isn't as per standard
    """ 
    # Raise error if length of triangle is less than 3
    if len(triangle_lengths) != 3:
      err_msg = "Invalid number of lengths. Please pass 3 lengths."
      raise InvalidInputError(err_msg)

    # Raise error if any of triangle length is not digit
    for triange_length in triangle_lengths:
      try:
        int(triange_length)
      except ValueError as e:
        err_msg = "Triangle lengths should always be in integer !"
        raise InvalidInputError(err_msg)
        break
    return True

  def execute(self):
    """
    Executes action for triangle shape as per input from client.
    Args:
      None   
    Returns:
      True if execution is successful else False
    """
    input_params = []
    print "\n\n\t\t\tHey Hi, Let's play with triangle !!"
    while True:
      input_params = self.get_input_params()
      try: 
        # Validate input params
        self.validate_input_params(input_params)
        (len_a, len_b, len_c) = input_params
        # Get Triangle type
        triangle_type = TriangleOperations.get_triangle_type(len_a,len_b,len_c)
        output = "\t\t\tOn the basis of lengths you passed, type of triangle is"
        print "%s: %s" %(output, triangle_type)
        break
      except InvalidInputError as e:
        print e
        ans = raw_input("\nDo you wish to try again?[y/yes]: ")
        if ans.upper() in ("Y", "YES"):
          continue
        else:
          break
    return True
