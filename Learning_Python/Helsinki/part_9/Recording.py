'''
Task:

Create a class named Recording that models a single recording. The class should have one private attribute:

__length: an integer representing the length of the recording in minutes.
Requirements:

The class should implement the following:

Constructor:

Takes length as an argument and initializes the private attribute.
If the length is below zero, raise a ValueError with an appropriate message.
Getter Method:

A method named length that returns the length of the recording.
Setter Method:

A method to set a new length for the recording.
If the provided length is below zero, raise a ValueError.

'''

class Recording:
    def __init__(self, length : int) -> None:
        if length < 0:
            raise ValueError("Length cannot be negative")
        self.__length = length
 
    @property
    def length(self):
        return self.__length
    
    @length.setter
    def length(self, length):
        if length < 0:
            raise ValueError("Length cannot be negative.")
        self.__length = length

if __name__ == "__main__":
    
    the_wall = Recording(43)
    print(the_wall.length)
    the_wall.length = 44
    print(the_wall.length)

