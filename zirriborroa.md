!pip install slycot

!pip install control



import control

from control.matlab import *

from matplotlib.pyplot import * # Grab MATLAB plotting functions



num = [2]

den = [1 , 2 , 2]

sys = TransferFunction(num, den)



(Ty, Yy) = step(sys, T=linspace(0,10,100))

plot(Ty, Yy[0,:].T, '-')
