## First order derivative
def f1(x, f):
    return f(x + 1e-4) - f(x) / 1e-4


## Second order derivative
def f2(x, f):
    return f1(x + 1e-4, f) - f1(x, f) / 1e-4


## The newton's law of finding optimal x
def find(x, f):
    min = 1e-4
    x_pre = x - 2  ##
    while x - x_pre > min:
        x_pre = x
        x = x_pre - f1(x_pre, f) / f2(x_pre, f)
    return x


## Example
import numpy as np
print(find(2.5, np.cos))
