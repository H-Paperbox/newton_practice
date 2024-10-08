import autograd.numpy as np
from autograd import hessian

def find_multi(x,f):
    min = 1e-4
    delta = 2
    while delta > min:
        first_derivative = np.gradient(x)
        hess = hessian(x)
        del_x = hess.T * first_derivative
        delta = sum( del_x**2 )
        x = x - del_x

    print("Hello!")
    return x