from __future__ import division
import numpy as np 
import empower.vbsp.project_modules.fun_ChooseProb
import empower.vbsp.project_modules.fun_Sigmoid
def fun_SelfOrganize(F_v, f_t, u_t, iExp, pExp, beta):
    '''
    % fun_SelfOrganize performs the self organization via learning and
    % consolidation.
    % First, learning stage randomly chooses a possible configuration.
    % Second, consolidation stage compares the new result with old results
    % and choose the higher payoff configuration with higher probability.
    %
    % Inputs:   F_v     - Vector of all feasible configurations
    %           U_v     - Utility corresonding to all feasible configurations
    %           f_t     - Historical vector of chosen configurations
    %           u_t     - Historical utilities of chosen configurations
    %           iExp    - Indicator showing Explored (1) / Unexplored (0)
    %                     status at previous timeslot
    %           pExp    - Exploration probability (learning rate)
    %           beta    - Annealing factor
    %
    % Outputs:  Same as Inputs
    '''    
    old_f_t = f_t[1:(len(f_t))]
    f_t[0:(len(f_t)-1)] = old_f_t # update configuratin history; len(f_t) = 1:end-1 in matlab
    old_u_t = u_t[1:(len(u_t))]
    u_t[0:(len(u_t)-1)] = old_u_t # update configuratin history; len(f_t) = 1:end-1 in matlab 
    
    if iExp == 0: # Learning        
        Exp = empower.vbsp.project_modules.fun_ChooseProb.fun_ChooseProb(np.array([pExp, 1-pExp]), np.array([1, 2])) # ?????
        F_v = list(F_v)                   
        temp = list([f_t[-2]])
        #print 'temp', temp
        #print 'F_v', F_v             
        if Exp == 1: # Exploration --> Choose a new configuration randomly                    
            Utility_0 = list(set(F_v)-set(temp))# setdiff(F_v,f_t(end-1)) # ???                       
            if not Utility_0:                
                f_t[-1] = f_t[-2]                
            else:
                #print 'ok2' 
                nChoice = len(Utility_0)
                Prob0 = 1/nChoice * np.ones(shape=(nChoice,1)) # calculate uniform probability                
                choice = empower.vbsp.project_modules.fun_ChooseProb.fun_ChooseProb(Prob0, np.arange(nChoice)) # ??? testing ????
                # print ('choice', choice)
                choice = choice[0]   
                f_t[-1] = Utility_0[choice] 
                #print 'Utility_0=',Utility_0,'choice=',choice  
                #print 'f_t[-1]=', f_t              
                #print f_t[10000]           
            iExp = 1                   
        else: # Exploitation --> Stay with the previous configuration
            f_t[-1]= f_t[-2]
            #print 'ok3' 
    else: # Consolidation        
        Utility_1 = u_t[-3] - u_t[-2]
        nu = empower.vbsp.project_modules.fun_Sigmoid.fun_Sigmoid(beta, Utility_1) # fun_Sigmoid
        #print ('nu=', nu)
        Act = empower.vbsp.project_modules.fun_ChooseProb.fun_ChooseProb([1-nu, nu],np.array([11, 12]))
        if Act == 11: # % Choose configuration @ (t-2)
            f_t[-1] = f_t[-3]          
        else: #Choose configuration @ (t-1)
            f_t[-1] = f_t[-2]        
        iExp = 0
        #print ('ok4')
    return f_t, u_t, iExp          
