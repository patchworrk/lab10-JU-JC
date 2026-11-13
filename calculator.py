"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
# First example
import math

def add(a, b):
    return a + b
def subtract(a, b):
    return a - b
def multiply(a, b):
    return a * b
def divide(a, b):
    if a == 0:
        raise ZeroDivisionError
    return b/a
def logarithm(a, b):
    if a <= 0 or b <= 0:
        raise ZeroDivisionError
    return math.log(b, a)
def exponent(a, b):
    return a ** b
def hypotenuse(a, b):
    inside_sqrt = a**2 + b**2
    return sqrt(inside_sqrt)
def sqrt(a):
    return math.sqrt(a)