#!/usr/bin/python3
def fizzbuzz():
    for nu_mber in range(1, 101):
        if nu_mber % 3 == 0 and nu_mber % 5 == 0:
            print("FizzBuzz ", end="")
        elif nu_mber % 3 == 0:
            print("Fizz ", end="")
        elif nu_mber % 5 == 0:
            print("Buzz ", end="")
        else:
            print("{0} ".format(nu_mber), end="")
    print("$")
