from __future__ import division
import numpy as np 
def calculateReceivedPower(pSend, distance):
    R = distance
    lambda_val = 0.142758313333
    a = 4.0
    b = 0.0065
    c = 17.1
    d = 10.8
    s = 15.8

    ht = 40
    hr = 1.5
    f = 1.9
    gamma = a - b*ht + c/ht
    Xf = 6 * np.log10( f/2 )
    Xh = -d * np.log10( hr/2 )

    R0 = 100.0
    R0p = R0 * pow(10.0,-( (Xf+Xh) / (10*gamma) ))

    if(R>R0p):
        alpha = 20 * np.log10( (4*np.pi*R0p) / lambda_val )
        PL = alpha + 10*gamma*np.log10( R/R0 ) + Xf + Xh + s
    else:
        PL = 20 * np.log10( (4*np.pi*R) / lambda_val ) + s

    pRec = pSend - PL
    if(pRec > pSend):
        pRec = pSend
    return pRec