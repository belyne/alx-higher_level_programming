#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
a = 10
b = 5
addition = add(10, 5)
print("{} + {} = {}".format(a, b, addition))
difference = sub(10, 5)
print("{} - {} = {}".format(a, b, difference))
product = mul(10, 5)
print("{} * {} = {}".format(a, b, product))
division = div(10, 5)
print("{} / {} ={}".format(a, b, division))
