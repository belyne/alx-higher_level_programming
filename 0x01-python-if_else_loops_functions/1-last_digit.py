#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
Last_digit = abs(number) % 10
str = "Last digit of {} ".format(number)
str += "is {}".format(Last_digit)
if Last_digit > 5:
    print(f"{str} and is greater than 5")
elif Last_digit == 0:
    print(f"{str} and is 0")
else:
    print(f"{str} and is less than 6 and not 0")
