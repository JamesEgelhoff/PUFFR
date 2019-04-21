#analysis code

import numpy as np
import matplotlib.pyplot as plt
import PUFFR_tools as pfr

#put useful constants here
c=3e8 #speed of light m/s

#calculate things here

<<<<<<< Updated upstream
<<<<<<< Updated upstream
T = pfr.temp_equilibrium2(fission_rate=3e18)
=======
T = pfr.temp_equilibrium2()
>>>>>>> Stashed changes
=======
T = pfr.temp_equilibrium2()
>>>>>>> Stashed changes
print('The engine temperature is {0:.3f} Kelvin'.format(T))

thrust = pfr.thrust1('absorb')
print('Thrust is {0:.3e} Newtons'.format(thrust))

dV = pfr.deltaV1()
print('The delta V is {0:.3e} meters per second'.format(dV))

isp = pfr.Isp1()
print('The ISP is {0:.3e} seconds'.format(isp))

power = pfr.thermal_power()
print("Power is {} kilowatts".format(power*1e-3))

input('Press enter to finish script')