'''
Create a class named Rectangle that represents a rectangle using two corner points. The class should have the following functionalities:

Constructor (__init__ method):

Takes two tuples left_upper and right_lower as arguments, representing the coordinates of the upper-left and lower-right corners of the rectangle, respectively.
Initializes the following attributes:
left_upper: the given left_upper tuple.
right_lower: the given right_lower tuple.
width: calculated as the difference between the x-coordinates of right_lower and left_upper.
height: calculated as the difference between the y-coordinates of right_lower and left_upper.
Method area():

Returns the area of the rectangle, calculated as width * height.
Method perimeter():

Returns the perimeter of the rectangle, calculated as 2 * (width + height).
Method move(x_change, y_change):

Takes two integers, x_change and y_change, and shifts the rectangle by these amounts.
Updates the coordinates of left_upper and right_lower based on the changes.
'''

class Rectangle:
    def __init__(self,left_upper : tuple,right_lower: tuple):
        self.left_upper = left_upper
        self.right_lower = right_lower
        self.width = (right_lower[0] - left_upper[0])
        self.height = right_lower[1] - left_upper[1]
        
    def area(self):
        return self.width * self.height
    
    def perimeter(self):
        return 2*(self.height + self.width)
    
    def move(self,x_change:int, y_change:int):
        corner = self.left_upper
        self.left_upper = (corner[0] + x_change, corner[1] + y_change)
        corner = self.right_lower
        self.right_lower = (corner[0] + x_change,corner[1] + y_change)

rectangle = Rectangle((1, 1), (4, 3))
print(rectangle.left_upper)
print(rectangle.right_lower)
print(rectangle.width)
print(rectangle.height)
print(rectangle.perimeter())
print(rectangle.area())

rectangle.move(3, 3)
print(rectangle.left_upper)
print(rectangle.right_lower)

rectangle = Rectangle((1, 1), (4, 3))
print(rectangle)