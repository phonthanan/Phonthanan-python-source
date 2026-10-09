"""
Write a Python class Rectangle with:

Private attributes for length and width
Methods to calculate area (getArea()) and perimeter getPerimeter())
A method to check if it's a square (isSquare())

"""

class Rectangle:

    def __init__(self, lenght, width):
        self.__lenght = lenght
        self.__width = width

    def getArea(self):
        return f"Area of {self.__width} width and {self.__lenght} lenght = (self.__width * self.__lenght)"

    def getPerimeter(self):
        return f"Perimeter of {self.__width} width and {self.__lenght} lenght = (2 * self.__width * self.__lenght)"

    def isSqauare(self):
        return self.__width == self.__lenght

myRectangel = Rectangle(6, 12)
print(myRectangle.getArea())

myRectangle2 = Rectangle(8, 8)
print(myRectangle2.isSqauare())