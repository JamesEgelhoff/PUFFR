"""
Library for PUFFR analysis files
"""

import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize as opt

#define useful significant physical constants here
stefbolt = 5.67e-8 #W/m^2 K^4
c = 3e8 #m/s

#define ballpark engine parameters here for use as function defaults
emis=.8
A=.1
mass_flow=.00000001
c_p=0
T_products=2000
I=1000
v=1e6

def temp_equilibrium1(emis=emis, A=A, mass_flow=mass_flow, c_p=c_p, T_products=T_products, I=I, v=v):
    
    """
    Finds the equilibrium temperature of the engine.
    
    Inputs (all optional):
    emis: emissivity of the engine
    A: engine surface area in m^2
    mass_flow: mass flow of fission products from core kg / s
    c_p: average specific heat of products K / J*kg
    T_products: temperature of products K
    I: power density of core radiation W / m^2
    v: velocity of fission fragments m / s
    """
    
    power_in = .5*((mass_flow * c_p * T_products / A) + I + (.5 * mass_flow * v**2 / A))
    
    T_4 = (power_in/emis/stefbolt)
    
    T = T_4**.25
    
    print('The equilibrium temperature is {0:.3f}'.format(T))

def thrust1(exhaust_mode, mass_flow=mass_flow, v=v):
    """
    Calculates engine thrust
    
    Inputs:
    exhaust_mode:
        if =reflect assume all ions are expelled directly from engine
        if =absorb assume half of all ions are expelled from engine
    mass_flow: mass flow rate of engine
    v: exhaust velocity
    """
    
    if exhaust_mode=='reflect':
        thrust = mass_flow*v
    if exhaust_mode=='absorb':
        thrust = .5*mass_flow*v
    else:
        print('exhaust_mode specification error')
    
    print('The thrust is {0:.3f} Newtons'.format(thrust))