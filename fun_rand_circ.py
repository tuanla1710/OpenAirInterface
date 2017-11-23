from __future__ import division
import numpy as np 
import math
def fun_rand_circ(N,x,y,r,s):
    '''
    # RAND_CIRC(N) generates N random points in the unit circle at (0,0).
    # RAND_CIRC(N,x,y,r) generates N random points in a circle with radius r
    # and center at (x,y).
    '''
    Ns = 10*round(4/math.pi*N + 2.5*math.sqrt(N) + 100) # 4/pi = 1.2732)
    Ns = int(Ns)
    #print(Ns)     
    X1 = np.random.uniform(0, 1, size=Ns)
    X = X1*(2*r) - r
    Y = np.random.uniform(0, 1, size=Ns)*(2*r) - r
    T =  np.sqrt(X**2 + Y**2); 
    I = np.where(T <=r)       
    if s>3: 
        I5 = I;
    else: 
        for i in range(3): 
            if i==0:                
                A = np.sqrt(3)*X - Y 
                B = np.sqrt(3)*X + Y 
                I2 = np.where(A >=0)[0] 
                I3 = np.where(B >=0)[0] 
            elif i==1:                                
                I2 = np.where(Y <=0)[0]  
                A = np.sqrt(3)*X + Y
                I3 = np.where(A<=0)[0]                                                      
            elif i==2:   
                I2 = np.where(Y >=0);
                A = (np.sqrt(3)*X - Y <=0)
                I3 = np.where(A <=0)[0]             
        I4 = np.intersect1d(I2,I3)
        I5 = np.intersect1d(I,I4)
    #print 'x = ', x, 'X = ', X, 'I5 =', I5, 'y  =', y, 'Y = ', Y    
    N = int(N)
    X5 = X[I5[range(N)]] + x; 
    Y5 = Y[I5[range(N)]] + y;   
    return X5,Y5             