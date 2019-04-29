#analysis code

import numpy as np
import matplotlib.pyplot as plt
import PUFFR_tools as pfr

#put useful constants here
c=3e8 #speed of light m/s

#calculate things here
iso600 = []
iso800 = []
iso1000 = []
iso1200 = []
iso1400 = []

thrust = np.geomspace(.01, 1, 1000)
eff=.01

for i in range(0, len(thrust)):
    iso600.append(pfr.radiatorEngine_mass(600+273, thrust[i], eff))
    iso800.append(pfr.radiatorEngine_mass(800+273, thrust[i], eff))
    iso1000.append(pfr.radiatorEngine_mass(1000+273, thrust[i], eff))
    iso1200.append(pfr.radiatorEngine_mass(1200+273, thrust[i], eff))
    iso1400.append(pfr.radiatorEngine_mass(1400+273, thrust[i], eff))

fig, ax = plt.subplots(1,1)
ax.plot(thrust, iso600, label="600 Celsius Isotherm")
ax.plot(thrust, iso800, label="800 Celsius Isotherm")
ax.plot(thrust, iso1000, label="1000 Celsius Isotherm")
ax.plot(thrust, iso1200, label="1200 Celsius Isotherm")
ax.plot(thrust, iso1400, label="1400 Celsius Isotherm")
ax.legend()
ax.set_xscale('log')
ax.set_yscale('log')
ax.set_xlabel('Thrust (Newtons)')
ax.set_ylabel('Mass of engine and radiator (kg)')
ax.set_title('Mass required to keep engine temperature below aerogel limit at 1% escape rate')
fig.show()