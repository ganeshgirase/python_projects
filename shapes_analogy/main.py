#! /usr/bin/python
#
#  This is entry program to play with different shapes
#  Author: Ganesh Girase <ganeshgirase@gmail.com>

import lib.shapes_factory
from lib.shapes_factory import ShapesFactory

def run():
  print "\t\t\tHello, welcome to shape analogy game!!\n"
  print "\t\t\tShapes available to evaluate: Triangle, Rectangle\n"
  # Get shape input from user
  shape_type = raw_input("\t\t\tEnter type of shape you want to evaluate: ")
 
  # Getobject of Shapes Factory class. 
  shape_factory = ShapesFactory()
  # This will return shape handler object for respective shape
  shape_handler = shape_factory.get_shape_handler(shape_type)
  shape_handler.execute() 

if __name__ == "__main__":
  # Entry point for main program
  run()




