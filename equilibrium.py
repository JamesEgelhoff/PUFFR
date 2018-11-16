import numpy as np

# -*- coding: utf-8 -*-
"""
Created on Wed Oct 10 19:42:33 2018

@author: Joshua
"""

# Material: Steel

emis = 0.8
stefbolt = 5.67e-8  # W/m^2 K^4
A = .1              # m^2

# Engine Properties

mass_flow = .00000001       # kg/s
c_p = 0             # K/Jkg
T_products = 2000   # K
I = 1000            # W/m^2
v = 1e6             # m/s

power_in = .5*((mass_flow * c_p * T_products / A) + I + (.5 * mass_flow * v**2 / A))

T_4 = (power_in/emis/stefbolt)

T = T_4**.25

print(T)


