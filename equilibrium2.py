# -*- coding: utf-8 -*-
import numpy as np

"""
Created on Thu Nov 15 19:26:25 2018

@author: Joshua
"""

# Second Pass Thermal Calculations

# Fuel Parameters
F = .8 # View Factor
fission_rate = 5e17 # Fissions/second
energy_per_fission = 200 # MeV
energy_per_fission = energy_per_fission * 1.60218e-13 # Joules

# Thermal Parameters
stefbolt = 5.67e-8  # W/m^2 K^4
emis = 0.8
surf_area = 10 # m^2

# Calculation

T = (fission_rate*energy_per_fission*F/(stefbolt*emis*surf_area))**.25

print(T)
