#!/usr/bin/python3
"""
Definition for class rectangle.
"""


class Rectangle:
    """
     Defines the implementation of a rectangle
    """


    def __init__(self, width=0, height=0):
        self.height = height
        self.width = width

    @property
    def height(self):
        """
          getter function for private attribute height.
          Returns: height of the triangle.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
          setter function for private attribute height.
          Args:
              value(int) new height value
          Raises:
                TypeError: if value is not int. 
                ValueError: if value is not >= 0.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    @property
    def width(self)
    """
      getter function for private attribute width.
      Returns: width of the triangle.
    """
        return self.__width

    @width.setter
    def width(self, value):
        """
          setter function for private attribute width.
          Args:
              value(int) new width value
          Raises:
               TypeError: if value is not int
               ValueError: if value is < 0
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value



