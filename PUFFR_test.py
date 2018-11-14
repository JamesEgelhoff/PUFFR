#analysis code

import numpy as np
import matplotlib.pyplot as plt
import PUFFR_tools as pfr

#put useful constants here
c=3e8 #speed of light m/s

#calculate things here

T = pfr.temp_equilibrium1(emis=.5)
print('The engine temperature is {0:.3f} Kelvin'.format(T))

thrust = pfr.thrust1('absorb')
print('Thrust is {0:.3e} Newtons'.format(thrust))

dV = pfr.deltaV1()
print('The delta V is {0:.3e} meters per second'.format(dV))

isp = pfr.Isp1()
print('The ISP is {0:.3e} seconds'.format(isp))

raw_input('Press enter to finish script')