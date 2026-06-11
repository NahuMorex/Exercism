import math

def square(number):
    if 64 < number or number < 1:
        raise ValueError("square must be between 1 and 64")
    return 2 ** (number -1)


def total():
    return 2 ** 64 + -1

