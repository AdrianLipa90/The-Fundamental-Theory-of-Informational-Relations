import numpy as np


def closure_operator(gamma):
    gamma = np.array(gamma)
    z = np.exp(1j * gamma)
    delta = np.sum(z)
    R = (np.abs(delta) ** 2) / (len(gamma) ** 2)
    C = 1 - R
    return delta, R, C
