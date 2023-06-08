#!/usr/bin/python3
from add_0 import add
if __name__ == "__main__":
    # Define the variables
    a = 1
    b = 2

    # Call the add function from add_0 module
    result = add(a, b)
    # Print the result
    print("{} + {} = {}".format(a, b, result))
