from __future__ import division
import numpy as np 
def fun_ChooseProb(P,X):
    '''#===============================================================================
    # % -------------------------------------------------------------------------
    # % fun_Chooserob randomly chooses an action x (configuration or choice) 
    # % depending on its probability p(x).
    # %
    # % Inputs:   P       - probability vector [p(x)]
    # %           x       - action vector [x]
    # % Outputs:  F       - chosen action
    # %
    # % Thant Zin Oo
    # % February 18, 2017.
    # % ------------------------------------------------------------------------- 
    #==============================================================================='''    
    cdf  = np.cumsum(P) # find cdf by taking cumulative sum.
    temp = np.random.uniform(0, 1) < cdf # check condition that rand is less than cdf    
    index = np.where(temp==1) # find the index of first true condition
    # print len(index),index     
    #print 'np.shape(X)=',np.shape(X)
    if len(index)!=0: 
        temp1 = np.array(index)            
        i =  temp1[[0],[0]]                         
        F = X[i] # choose the action with index.        
    else:
        print ('nothing happen! Check fun_ChooseProb function')
    return F
