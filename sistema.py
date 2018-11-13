from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
from scipy import integrate

def solve_sistema(K=1.0):
    """Plot a solution to the Lorenz differential equations."""

    num = [2*K]
    den = [1 , 2 , 2]

    sys = TransferFunction(num, den)

    yout , T = step(sys, T=linspace(0,10,100))

    plot(T, yout, '-')
    

    return T, yout