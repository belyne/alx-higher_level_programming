#!/usr/bin/python3
def magic_string():
    if not hasattr(magic_string, 'iteration'):
        magic_string.iteration = 0
    else:
        magic_string.iteration += 1
    return "BestSchool, " * magic_string.iteration + "BestSchool"
