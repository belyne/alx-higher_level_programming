#!/usr/bin/python3
class Square:
    """
    This class represents a square.

    Attributes:
        __size (int): The size of the square.
        __position (tuple): The position of the square.

    Methods:
        __init__(self, size=0, position=(0, 0)): Initializes a new instance of the Square class.
        size(self): Getter method for retrieving the size attribute.
        size(self, value): Setter method for setting the size attribute.
        position(self): Getter method for retrieving the position attribute.
        position(self, value): Setter method for setting the position attribute.
        area(self): Calculates the area of the square.
        my_print(self): Prints the square using the '#' character.
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes a new instance of the Square class.

        Args:
            size (int): The size of the square (default is 0).
            position (tuple): The position of the square (default is (0, 0)).
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """
        Getter method for retrieving the size attribute.

        Returns:
            int: The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter method for setting the size attribute.

        Args:
            value (int): The size value to set.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        """
        Getter method for retrieving the position attribute.

        Returns:
            tuple: The position of the square.
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Setter method for setting the position attribute.

        Args:
            value (tuple): The position value to set.

        Raises:
            TypeError: If the value is not a tuple of two positive integers.
        """
        if not isinstance(value, tuple) or len(value) != 2 or not all(isinstance(num, int) for num in value) or any(num < 0 for num in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """
        Calculates the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2

    def my_print(self):
        """
        Prints the square using the '#' character.

        If the size is 0, an empty line is printed.
        The position is used to determine the starting position of the square.
        """
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__position[1]):
                print()
            for _ in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)
