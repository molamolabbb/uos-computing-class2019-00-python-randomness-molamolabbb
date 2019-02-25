#!/usr/bin/env python3

# python3 division in python2
from __future__ import division

# Python3 print in python2
from __future__ import print_function

print(1+2+3+4)

a = 5
print(f"Here is a {a+2}")  # Requires python 3.6+
print(f"Watch out for division {a/2} (float div in py3, int div in py2)"
      f" {a//2} (int div)")


def double(x):
    """Optional docstring that explains what the function does. This
    function multiplies its input by 2"""
    return x * 2


def apply_to_one(f):
    """Function in python are first-class.
    You can pass them to functions.
    """
    return f(1)


print(f"{apply_to_one(double)}")
print(f"An inline lambda function: {apply_to_one(lambda x: x + 2)}")

try:
    print(0 / 0)
except ZeroDivisionError:
    print("cannot divide by zero")

# Lists

# # List comprehension
aa = [1, 2, 3]
bb = [2*i for i in aa]

# Tuples

# Dictionaries, including defaultdict
from collections import defaultdict

# Sets

# Task: write a random() function, write some tests for it (?)

# Need: random integers, random floats, shuffle, gaussian sampling
