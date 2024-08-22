import numpy as np
# def f(x):
#     return np.cos(x)
def f1(x,f):
    return f(x+1e-4)-f(x)/1e-4
def f2(x,f):
    return f1(x+1e-4,f)-f1(x,f)/1e-4

min = 1e-4
def find(x, f):
    x_pre = x - 2 ##
    while (x-x_pre > min):
        x_pre = x
        x = x_pre - f1(x_pre,f)/f2(x_pre,f) 
    # print(x)
    return x