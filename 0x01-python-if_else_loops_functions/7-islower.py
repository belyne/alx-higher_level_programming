#!/usr/bin/python3
def islower(c):
    ascii_val = ord(c)
    if 97 <= ascii_val <= 122:
        return True
    else:
        return False

