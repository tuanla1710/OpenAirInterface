from __future__ import division
import numpy as np
import math 
def calculateNoise(self, bandwidth=5):
    k = 1.3806488 * math.pow(10, -23)
    T = 293.0
    BW = bandwidth * 1000 * 1000
    N = 10*math.log10(k*T) + 10*np.log10(BW) # dBm
    return N