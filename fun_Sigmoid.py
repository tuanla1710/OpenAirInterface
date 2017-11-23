from __future__ import division
import numpy as np
import math
def fun_Sigmoid(beta, U_f): # U_f is only a value not a an array ??? 
    # U_f = np.random.random(5)
    #print(U_f )
    # U_f = np.sort(U_f)
    #print(U_f)
    # beta = 0.05
    
    U_f = np.array([U_f])
    #print ('U_f=', U_f)
    nChoice = len(U_f)
     
    tmp = np.dot(np.array([np.ones(nChoice)]),U_f)
    tmp = np.array(tmp)
    #print(tmp)
    theta = tmp - tmp.T
    #print(theta)
    p_f = np.array([np.zeros(nChoice)])
    #print(p_f)
    
    for k1 in range(nChoice):
        tmp2 = 0
        for k2 in range(nChoice):
            if (k1!= k2):
                tmp2 = tmp2 + math.exp(-beta*theta[k2][k1])
        p_f[0][k1] = 1/(1+tmp2)
    
    return p_f[0]
