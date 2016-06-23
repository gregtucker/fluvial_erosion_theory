# -*- coding: utf-8 -*-
"""
Created on Tue Jun 21 14:25:37 2016

@author: gtucker
"""

import numpy as np
import matplotlib.pyplot as plt
from sympy import erf

x = np.arange(-10.0, 10.1, 0.01)

def squash(x, x0=0.0, wid=1.0):
    """Calculate tanh squashing function."""
    return (np.tanh((x - x0) / wid) + 1.0) / 2.0

def myfn(x, x0):
    return x

x0 = 0.1
thx = squash(x, 0.0, wid=10.0)
fn1 = myfn(x, x0)
fn2 = squash(x)
fn3 = (x + (1.0 - fn2)) * fn2
fn4 = 1.0 - np.exp(-x/x0)
fn5 = x * (x - 1)


plt.figure(1)
plt.clf()
plt.plot(x, fn1)
plt.plot(x, fn2)
plt.plot(x, fn3)
plt.grid()
plt.show()

print np.min(fn3)
