import math
import random

def sum(x, y):
    return x + y

def subt(x, y):
    return x - y

def mult(x, y):
    return x * y

def div(x, y):
    return x / y

def exp(x, y):
    return x ** y

def module(x):
    return abs(x)

def rand(x, y):
    return random.randint(x, y)

def fac(x):
    if x == 0 or x == 1:
        return 1
    else:
        return fac(x - 1) * x

def arc(x):
    return math.acos(x)
