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
fuel_frac = .5 #fraction of rocket's mass allocated for fuel
view_factor = .8
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
    
def temp_equilibrium2(F=view_factor, fission_rate=reactionRate, energy_per_fission = energy_per_fission, emis=emis, surf_area=surf_area):
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
    
    return v*np.log(1/fuel_frac)

def Isp1(v=v):
    """
    Calculates engine ISP
    
    Inputs:
    v: exhaust velocity m/s^2
    """
    return v/g

def thermal_power(rate=reactionRate, en=energy_per_fission):
    """
    Calculates the total power of the engine due to fission
    
    Inputs:
    rate: fissions per second
    en: energy per fission in MeV
    """
    
    return rate*en*1.60218e-13
    
def radiatorEngine_mass(Tlimit, thrust, eff):
    """
    Given an upper limit on temperature and a desired thrust, calculates the mass of radiators required
    
    inputs:
    Tlimit: max allowable temperature in Kelvin
    thrust: desired thrust in Newtons (used to calculate fission rate, assuming 3% escape rate)
    eff: fission escape probability (in the range 0 to 1)
    
    outputs:
    mass: mass of carbon fiber radiator (see https://ntrs.nasa.gov/archive/nasa/casi.ntrs.nasa.gov/20140016906.pdf)
    """
    
    mAm = 4.035e-25 #mass of Americium in kg
    vEx = 9e6 #.03c exhaust velocity in m/s
    fissionE = 3.204e-11 #energy of fission - 200MeV in Joules
    
    #calculate fission rate from thrust = (fissions per second) * impulse per fission * escape rate
    fission_rate = thrust / (.5 * eff * mAm * vEx)
    
    #thermal power = fission rate * energy per fission * efficiency of conversion to heat
    thermP = fission_rate * fissionE * (1-eff)
    
    #calculate power emission due solely to engine
    hexFaces = 434 #number of exposed hexagons emitting heat
    vertFaces = 102 #number of vertical surfaces emitting heat
    rHex = .02 #inner radius of hexagon in meters
    sHex = np.sqrt(4/3) * rHex #side length of hexagon
    height = .7 #height of engine in m
    hexArea = 2 * np.sqrt(3) * rHex**2 #area of hexagon
    vertArea = sHex*height #surface area of vertical surfaces
    engSurfArea = hexArea * hexFaces + vertArea * vertFaces #total surface area of engine
    
    engEmis = .95 #assume high emissivity coating on engine
    engPowerEmission = engSurfArea * engEmis * stefbolt * Tlimit**4 #power emitted by engine without radiators
    
    #the power that must be radiated is the difference between the thermal power produced by the engine
    #and the thermal power its surfaces radiate
    #Power emitted by radiators = Power produced by engine - power radiated by engine
    radP = thermP - engPowerEmission
    
    #calculate radiator area from Stefan-Boltzmann
    emis = .8 #carbon fiber emissivity
    radArea = radP / (emis * stefbolt * Tlimit**4)
    radMass = 2*radArea #assume 2kg per square meter for carbon fiber radiator
    engineMass = 439
    totalMass = radMass + engineMass
    
    return totalMass