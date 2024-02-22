#!/usr/bin/python3
"""Python script with Rectangle class."""


class Rectangle:
    """A class representing a rectangle."""

    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """
        Initializes a Rectangle instance with specified width and height.

        Args:
            width (int): Width of the rectangle. Defaults to 0.
            height (int): Height of the rectangle. Defaults to 0.
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    def __str__(self):
        """Returns the string representation of the rectangle that
        print() and str() should print the rectangle with the character #
        """
        rectangle = ''
        i = j = 0
        for i in range(self.height):
            for j in range(self.width):
                rectangle += str(self.print_symbol)
            if i != self.height - 1 and j != 0:
                rectangle += '\n'
        return rectangle

    def __repr__(self):
        """Returns a string representation of the rectangle
        to be able to recreate a new instance by using eval()
        """
        return f"Rectangle({self.width}, {self.height})"

    def __del__(self):
        """prints a string when the instance is deleted"""
        print('Bye rectangle...')
        Rectangle.number_of_instances -= 1

    @property
    def width(self):
        """Getter method for the width attribute."""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter method for the width attribute."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Getter method for the height attribute."""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter method for the height attribute."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        Calculates the area of the rectangle.

        Returns:
            int: The area of the rectangle
        """
        return self.width * self.height

    def perimeter(self):
        """
        Calculates the perimeter of the rectangle.

        Returns:
            int: The perimeter of the rectangle.
        """
        if self.width == 0 or self.height == 0:
            return 0
        return 2 * (self.width + self.height)

    def bigger_or_equal(rect_1, rect_2):
        """
        Compares the areas of two rectangles and returns
        the larger or equal one.

        Args:
            rect_1 (Rectangle): An instance of Rectangle
            representing the first rectangle.
            rect_2 (Rectangle): An instance of Rectangle
            representing the second rectangle.

        Returns:
            Rectangle: The larger or equal rectangle between
            rect_1 and rect_2.

        Raises:
            TypeError: If either rect_1 or rect_2 is not
            an instance of Rectangle.
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError('rect_1 must be an instance of Rectangle')
        if not isinstance(rect_2, Rectangle):
            raise TypeError('rect_2 must be an instance of Rectangle')

        if max(rect_1.area(), rect_2.area()) == rect_1.area():
            return rect_1
        else:
            return rect_2
