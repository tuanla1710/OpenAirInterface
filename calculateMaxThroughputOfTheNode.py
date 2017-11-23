from __future__ import division
import numpy as np 
import math

def calculateMaxThroughputOfTheNode(sinr,d,r):
    r_i = 0.0
    M_i = 0.0
    #sinr = calculateSINR(bs_vector, obstacles)
    if sinr < -5.45:
        r_i = 78/1024
        M_i = 2
    elif -5.45 <= sinr < -3.63:
        r_i = 78/1024
        M_i = 4
    elif -3.63 <= sinr < -1.81:
        r_i = 120/1034
        M_i = 4
    elif -1.81 <= sinr < 0:
        r_i = 193/1024
        M_i = 4
    elif 0 <= sinr < 1.81:
        r_i = 308/1024
        M_i = 4
    elif 1.81 <= sinr < 3.63:
        r_i = 449/1024
        M_i = 4
    elif 3.63 <= sinr < 5.45:
        r_i = 602/1024
        M_i = 4
    elif 5.45 <= sinr < 7.27:
        r_i = 378/1024
        M_i = 16
    elif 7.27 <= sinr < 9.09:
        r_i = 490/1024
        M_i = 16
    elif 9.09 <= sinr < 10.90:
        r_i = 616/1024
        M_i = 16
    elif 10.90 <= sinr < 12.72:
        r_i = 466/1024
        M_i = 64
    elif 12.72 <= sinr < 14.54:
        r_i = 567/1024
        M_i = 64
    elif 14.54 <= sinr < 16.36:
        r_i = 666/1024
        M_i = 64
    elif 16.36 <= sinr < 18.18:
        r_i = 772/1024
        M_i = 64
    elif 18.18 <= sinr < 20:
        r_i = 873/1024
        M_i = 64
    elif 20 <= sinr:
        r_i = 948/1024
        M_i = 64

    
    if d <= r:
        capacityForUE_ms = r_i * np.log2(M_i) * 12 * 7 * ((200*(1/3))/1)
        capacityForUE_s = capacityForUE_ms * 1000
    else:
        capacityForUE_ms = r_i * np.log2(M_i) * 12 * 7 * ((200*(1/3))/1)
        capacityForUE_s = capacityForUE_ms * 1000

    return capacityForUE_s # bit/second