"""
Library for PUFFR analysis functions
"""

import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize as opt

#define useful significant physical constants here
stefbolt = 5.67e-8 #Stefan-Boltzmann constant W/m^2 K^4
c = 3e8 #speed of light m/s
g = 9.80665 #standard gravity m/s^2
AmMass = 242 #AMU
kgPerAmu = 1.6e-27

#define ballpark engine parameters here for use as function defaults - can update as our estimates improve
emis=.8 #emissivity
A=.1 #engine surface area m^2
reactionRate = 5.8e17 #fissions / second
mass_flow= AmMass*kgPerAmu*reactionRate #self explanatory kg/s
c_p=0 #specific heat of fission fragments K/J*kg
T_products=2000 #temperature of fission fragments K
I=1000 #power density of core radiation W/M^2
v=.03 * 3e8 #velocity of fision fragments m/s
#reaction_rate = ? #fission rate fissions/s
fuel_frac = .5 #fraction of rocket's mass allocated for fuel
view_factor = .8
reaction_rate = 6e17 #fissions per second
energy_per_fission = 180 #MeV
surf_area = 10 #m^2

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
    
    return(T)
    
def temp_equilibrium2(F = view_factor, fission_rate=reaction_rate, energy_per_fission = energy_per_fission,
                      emis=emis, surf_area=surf_area):
    """
    Created on Thu Nov 15 19:26:25 2018
    
    @author: Joshua
    
    Second pass thermal calculations
    """
    
    # convert energy to joules
    energy_per_fission = energy_per_fission * 1.60218e-13 # Joules
    
    # Calculation
    T = (fission_rate*energy_per_fission*F/(stefbolt*emis*surf_area))**.25
    
    return T

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
    
    return thrust

def deltaV1(v=v, fuel_frac=fuel_frac):
    """
    Calculates the rocket's delta V
    
    Inputs:
    v: exhaust velocity m/s
    fuel_frac: fraction of the mass of the rocket allocated for fuel
    """
    
    return v*fuel_frac

def Isp1(v=v):
    """
    Calculates engine ISP
    
    Inputs:
    v: exhaust velocity m/s^2
    """
    return v/g