
# Exercise #1

# Write a Python class named
# Rectangle constructed by a length and width and a method that will compute the area of a rectangle.
class Rectangle:
    """Rectangle class, includes length and width and a method that will compute the area of a rectangle"""

    def __init__(self, length, width):
        self.length = length
        self.width = width
        self.area = None

    def get_area(self):
        self.area = self.length * self.width
        return self.area


Test_Rectangle = Rectangle(11, 7)

print("Test Rectangle report" + " (" + Rectangle.__doc__ + "):")  # printing the headline with a docstring
print("Width:" + str(Test_Rectangle.width))
print("Length:" + str(Test_Rectangle.length))
print("Area:" + str(Test_Rectangle.get_area()))
