#!/usr/bin/python3
"""Creating class square"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """ Square class that inherits
    from the rectangle"""

    def __init__(self, size, x=0, y=0, id=None):
        """Defining a function tha initialize
        the square class attributes"""

        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Defining a function that 
        returns the size of the square"""

        return self.width

    @size.setter
    def size(self, value):
        """Defining a function that
        sets the size of the square"""

        self.width = value
        self.height = value

    def __str__(self):
        """Definig a function that
        returns the string representation"""

        return "[Square] ({}) {}/{} - {}". \
            format(self.id, self.x, self.y, self.size)

    def update(self, *args, **kwargs):
        """Assigning attributes to arguments"""
        if len(args) != 0:
            try:
                self.id = args[0]
                self.size = args[1]
                self.x = args[2]
                self.y = args[3]
            except IndexError:
                pass

        elif len(kwargs) != 0:
            self.id = kwargs["id"] if "id" in kwargs else self.id
            self.size = kwargs["size"] if "size" in kwargs else self.size
            self.x = kwargs["x"] if "x" in kwargs else self.x
            self.y = kwargs["y"] if "y" in kwargs else self.y

    def to_dictionary(self):
        """Definig a function that 
        returns a dictionary representation of the square"""
        return {
                "id": self.id,
                "size": self.size,
                "x": self.x,
                "y": self.y
            }
