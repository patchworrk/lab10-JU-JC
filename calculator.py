# https://github.com/patchworrk/lab10-JU-JC
# Partner 1: Joshua Ulery
# Partner 2: Javier Castro
import math

def add(a, b):
    return a + b
def subtract(a, b):
    return a - b
def multiply(a, b):
    return a * b

def mul(a, b):
    return a * b

def divide(a, b):
    if a == 0:
        raise ZeroDivisionError
    return b/a

def div(a, b):
    if a == 0:
        raise ZeroDivisionError
    return b/a

def logarithm(a, b):
    if b <= 0:
        raise ValueError
    if a <= 0:
        raise ZeroDivisionError
    return math.log(b, a)

def exponent(a, b):
    return a ** b

def exp(a, b):
    return a ** b

def hypotenuse(a, b):
    inside_sqrt = a**2 + b**2
    return sqrt(inside_sqrt)

def sqrt(a):
    return math.sqrt(a)

def square_root(a):
    return math.sqrt(a)

