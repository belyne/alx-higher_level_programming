#!/usr/bin/python3
import sys
from decimal import Decimal
if __name__ == "__main__":
    arguments = sys.argv[1:]
    the_result = 0
    for arg in arguments:
        the_result += int(arg)
    print(the_result)
