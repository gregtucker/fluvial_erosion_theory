# -*- coding: utf-8 -*-
"""
Analytical solution for alluvium thickness as a function of time in 
"SPACE" model.

Here $H$ is really $H' = H / H_*$
and $t$ is really $t' = t K_s q S / H_*$
and $d$ is $D / K_s q S$
and $beta = K_r / K_s$

Created on Sat Jun 18 20:43:52 2016

@author: gtucker
"""

import numpy as np
import matplotlib.pyplot as plt

# parameters
d = 1.0   # ratio of deposition rate to max entrainment rate
H0 = 0.0  # initial alluvium thickness (dimensionless)
tmax = 100.0  # maximum time (dimensionless)
dt = 0.1     # time step

# Array
t = np.arange(0.0, tmax, dt)

# Solution

if d == 1.0:
    H = np.log(t + np.exp(H0))
else:
    dm1 = d - 1.0
    H = np.log((1.0 / dm1) * (np.exp(dm1 * t) * (dm1 * np.exp(H0) + 1.0) - 1.0))

# Plot
plt.clf()
plt.plot(t, H)
plt.show()

