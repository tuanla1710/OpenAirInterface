from __future__ import division
"""
Created on Wed May 11 13:10:20 2017
Translated from matlab files Dr. ThanzinOo
@author: LE ANH TUAN
"""
#===============================================================================
from numpy import int
import numpy as np
from scipy.spatial.distance import cdist
import random
from empower.vbsp.project_modules import *
from cvxpy import error
import sys
#===============================================================================
#clear_all.clear_all()
#===============================================================================
# class Controller_Name:
#     nBS = 0;  # Number of BSs
#     nMBS = 0; # Number of MBSs
#     nPBS = 0; # Number of PBSs
#     nFBS = 0; # Number of GBSs
#
#     nRB = 0;  # Number of resource blocks
#
#     nUE = 0;  # Number of UEs
#
#     mUA = []; # User association matrix
#     mFUA = []; # User association matrix
#     mRBA = [];# Resource blocks allocation matrix
#
#     rMBS = 0; # Radius of MBS
#     rPBS = 0; # Radius of PBS
#     rFBS = 0; # Radius of FBS
#
#     pBS  = [];# Transmit power of all BSs
#     pMBS = 0; # Radius of MBS
#     pPBS = 0; # Radius of PBS
#     pFBS = 0; # Radius of FBS
#
#     cBS = []; # Coor of MBS
#     cMBS =[];# Coor of MBS
#     cPBS =[];# Coor of PBS
#     cFBS =[];# Coor of FBS
#
#     cUE = []; # Coor of FBS
#
#     RefPL = [];# nBSx1
#
#     BS_Dist = []; # nBS x nBS: distance among BSs
#
#     FFT_size = 0;
#
#     def __init__(self, name): # project name
#         self.name = name
#     def info(self,Controller_Name):
#         print('nBS= {0}, nUE= {1}, nRB:= {2}'.format(Controller_Name.nBS,
#               Controller_Name.nRB,Controller_Name.nUE))
#         return 0
#
# class BS_Types(object):
#     """__init__() functions as the class constructor"""
#     def __init__(self, Type='None', TxPower_sCH=[], TxHeight=0,TxGain = 0,
#                  CellRadius = 0, RefPL = 0, TotalPower = 0):
#         self.Type = Type
#         self.TxPower_sCH = TxPower_sCH;   # Per sub-channel Transmit Power [watt]
#         self.TxHeight = TxHeight; # Transmit antenna height [metre]
#         self.TxGain = TxGain; # Transmit antenna gain [dBi]
#         self.CellRadius = CellRadius; # Cell radius of BS [metre]
#         self.RefPL = RefPL; # Reference path loss [dBm]
#         self.TotalPower = TotalPower;
#
# class User_Equipment(object):
#     """__init__() user equipment class"""
#     def __init__(self, name='None', BS=None, P_Tx=None,RB = None, Rate = None,
#                  Power = None,pExp = None,Explored = None, Utility = None):
#         self.name = name
#         self.BS = BS
#         self.P_Tx = P_Tx
#         self.RB = RB
#         self.Rate = Rate
#         self.Power = Power
#         self.pExp = pExp
#         self.Explored = Explored
#         self.Utility = Utility
#
# class Base_Station(object):
#     """__init__() base station class"""
#     def __init__(self, name='None', cell_radius = 0, user_association=0,
#                  transmit_power=0,uplink_RB_allocation = [],
#                  downlink_RB_allocation = [],cell_location = [],RefRP = 0,TxPower_RB=[]):
#         self.name = name
#         self.user_association = user_association
#         self.transmit_power = transmit_power
#         self.uplink_RB_allocation = uplink_RB_allocation
#         self.downlink_RB_allocation = downlink_RB_allocation
#         self.cell_location = cell_location
#         self.cell_radius = cell_radius
#         self.RefRP = RefRP
#         self.TxPower_RB = TxPower_RB

#===============================================================================
def scheduling_algoirthm(M1,M2,M3,M4,M5,M6,M7):
    MNO = Controller_Name('----Project Name: Markov approximation-based learning in 5G network---')
    ###### ----> INPUT PARAMETERs
    print ('Updating network parameter from eNB and UE to SDN controller...')
    # Network size
    MNO.nBS = 3;            # Number of BSs
    MNO.nFBS = 3;           # Number of FBSs
    MNO.nUE = 5;            # Number of UEs
    MNO.nRB = 25;           # Number of RBs
    MNO.nTotCar = 300;       # Total number of subcarriers = 25 RB
    nHistory = 100
    print ('Initializing Algorithm parameters')
    nIterations = 80
    beta_step = 8
    conv_stop = 50
    Algorithm = 3 # MCDA = 1; PLLA = 2; SOA = 3;
    if Algorithm ==1: # MCDA
        pExp = 1
        pEstep = 0
        Str2 =  'OP_MA_' + str(MNO.nUE) + '.mat'
    if Algorithm == 2: # PLLA
            pExp = 0.5
            pEstep = 0
            Str2 =  'OP_LL_' + str(MNO.nUE) + '.mat'
    if Algorithm == 3: # SOA
            pExp = 1
            pEstep = 0.1
            Str2 =  'OP_SOA_' + str(MNO.nUE) + '.mat'
    # initialization matrix to update: 
    print ('Initializing output parameters to the MNO...')
    MNO.P_Tx_UExBS_RB = np.zeros(shape=(MNO.nUE,MNO.nBS),dtype = float)
    MNO.Rate_UExBS_RB = np.zeros(shape=(MNO.nUE,MNO.nBS),dtype = float)  
    MNO.Intf_UExBS_RB= np.zeros(shape=(MNO.nUE,MNO.nBS),dtype = float)  
    MNO.mnRBA = np.zeros(shape=(MNO.nUE,MNO.nBS))  
    MNO.SINR_UE_BS_RB = np.zeros(shape=(MNO.nUE,MNO.nBS),dtype = float)  
    MNO.mUA = np.zeros(shape=(MNO.nUE,MNO.nBS), dtype = int) #
    MNO.mRBA = np.zeros(shape=(MNO.nRB,MNO.nBS),dtype=bool) # resource allocation 
    MNO.OP_Rate = np.zeros(shape=(MNO.nUE,MNO.nBS),dtype = float)
    MNO.OP_Cost = np.zeros(shape=(MNO.nUE,MNO.nBS),dtype = float)
    MNO.OP2_User = np.zeros(shape=(nIterations,MNO.nBS),dtype = int)
    MNO.OP2_User = np.zeros(shape=(nIterations,MNO.nBS),dtype = float)
    MNO.OP2_Cost = np.zeros(shape=(nIterations,MNO.nBS),dtype = float)
    MNO.BS_Cmap = np.zeros(shape=(MNO.nBS,MNO.nBS),dtype = float)
    MNO.BS_Rmap = np.zeros(shape=(MNO.nBS,MNO.nBS),dtype = float)
    P = np.zeros(shape=(MNO.nRB,MNO.nBS)) # Control variable for power
    U = np.zeros(shape=(MNO.nUE,MNO.nBS)) # Utility --> Revenue - Cost
    pExpVec = np.ones(MNO.nUE,dtype = float)
    #===============================================================================
    #===============================================================================
    print ('Getting Device information from testbed system')
    
    BS_list = ["3618","3619","3620"] # via BS id set at configuration file
    UE_list = ["UE-id-1","UE-id-2","UE-id-3","UE-id-4","UE-id-5"] # via UE emei
    tx_gain_bs = M1#[89.75,89.75,89.75] # via BS id set at configuration file 
    rx_gain_ue = M2 #[21,21,21,21,21] # via UE emei
    
    print ('Conflict and Resue Graphs for Base Stations ... ') # where??? 
    
    MNO.BS_Cmap = M3#np.array([[0, 0, 1], 
#                            [0, 0, 1],
 #                           [1, 1, 0]])
    
    MNO.BS_Rmap = M4 #np.array([[1, 0, 0],
  #                          [0, 1, 0],
   #                         [0, 0,  1]])
    
    MNO.P_Rx =  M5 #np.array([[-69.12372078, -74.1376763,  -71.82325875],
    #                      [-53.83030764, -70.29361338, -74.97618152],
     #                     [-59.74909419, -67.796359,   -75.62515563],
      #                    [-66.54979872, -74.95372667, -69.25830752],
       #                   [-61.29133112, -73.60238591, -70.5957919 ]])
    #===============================================================================
    # print 'Getting SINR level'
    # MNO.P_Rx = 10**(0.1*MNO.P_Rx)
    # #print 'MNO.P_Rx', MNO.P_Rx
    # for k1 in range(MNO.nUE):
    #     for k2 in range(MNO.nBS):
    #         MNO.Intf_UExBS_RB[[k1],[k2]] = np.dot(MNO.P_Rx[[k1],:], MNO.BS_Rmap[:,[k2]]) # Wats            
    #         MNO.SINR_UE_BS_RB[[k1],[k2]] = MNO.P_Rx[[k1],[k2]] / (MNO.Intf_UExBS_RB[[k1],[k2]]  + MNO.N0) # Wats
    #         
    # SINR_dB = 10*np.log10(MNO.SINR_UE_BS_RB)
    MNO.Intf_UExBS_RB = M6 # np.array([[  6.57164546e-08,   6.57164546e-08,   1.60925213e-07],
    #                               [  3.17966852e-08,   3.17966852e-08,   4.23316627e-06],
     #                              [  2.73832150e-08,  2.73832150e-08,   1.22557256e-06],
      #                             [  1.18623094e-07,   1.18623094e-07,   2.53281241e-07],
       #                            [  8.71807921e-08,   8.71807921e-08,   7.86419045e-07]])
    SINR_dB = M7 # np.array([[  2.69953797, -2.31441755,  -3.88949969],
        #                [ 21.14587388,   4.68256814, -21.24283479],
         #               [ 15.87606144,   7.82879663, -16.50854592],
          #              [  2.7085088,   -5.69541915,  -3.29433778],
           #             [  9.30446078,  -3.00659401,  -9.55233212]])
    MNO.pFBS = 30;             # Power of FBSs
    Noise = calculateNoise.calculateNoise(5)  # [dBm] Thermal noise floor with BW = 5MHz.
    MNO.N0 = 10**((Noise-30)/10) # [W]
    #===============================================================================
    MNO.UE_DL_Demand = np.array([ 1650000,  1350000,  1200000,  1500000,  1350000])      
    #===============================================================================
    #=========Initialization classes
    print ('Initializing BSs and UEs')
    # base station
    base_station = []
    i = 0  
    for i in range(MNO.nBS):              
        base_station.append(Base_Station('FBS-id:= fbs-'+str(i),MNO.rFBS,[],MNO.pFBS,[], [], [],0,MNO.pFBS))            
    # user  
    UE = [] 
    for i in range(MNO.nUE):       
        UE.append(User_Equipment('UE-id:= ue-'+str(i),[],[],[],[],[],[],[],[]))
    #===============================================================================
    # === --> Compute RBs for each virutal UE given the UE demand
    MNO.mFUA = (SINR_dB >= -12) # 9 dBm is interference threshold
    for k1 in range(MNO.nUE):
        for k2 in range(MNO.nBS):
            if MNO.mFUA[[k1],[k2]] == 1:
                # Calculate Achievable rate per unit RB
                MNO.Rate_UExBS_RB[[k1],[k2]] = calculateMaxThroughputOfTheNode.calculateMaxThroughputOfTheNode(SINR_dB[[k1],[k2]],100,50)
                # Calculate # of RB to meet UE demand
                MNO.mnRBA[[k1],[k2]] = np.ceil(MNO.UE_DL_Demand[k1]/MNO.Rate_UExBS_RB[[k1],[k2]])  # we will execute this one  
    for k1 in range(MNO.nUE):    
        UE[k1].BS = np.zeros(nHistory, dtype = int)
        UE[k1].P_Tx = np.zeros(nHistory, dtype = float)        
        UE[k1].RB = np.zeros(shape=(MNO.nRB,nHistory),dtype = bool)
        UE[k1].Rate = np.zeros(nHistory, dtype = float)
        UE[k1].Power = np.zeros(nHistory, dtype = float)  
        UE[k1].Utility = np.zeros(nHistory, dtype = float)
        UE[k1].beta = 0
        UE[k1].Explored = 0
    ##### --> UA allocation between virutal BSs and virtual UEs
    for k1 in range(MNO.nUE):     
        SINR_max = np.amax(SINR_dB[[k1],:]) # Maximum SINR UE association --> will create an array[ [0,0,0], [1, 3, 5]] for ex.
        BS_ind1 = np.where(SINR_dB[[k1],:]==SINR_max) # Maximum SINR UE association        
        BS_ind = BS_ind1[1][0]       
        MNO.mUA[[k1],[BS_ind]] = 1    # cell association   
    ##### ---> RBs allocation to virtual UEs        
        BS_Conflict = MNO.BS_Cmap[[BS_ind],:] # Conflict BS of BS_ind    
        print (BS_Conflict[0])
        BS_Conflict_id = []
        BS_Conflict_id = []
        for k2 in range(MNO.nBS):
            if BS_Conflict[0][k2] == 1:
                if not BS_Conflict_id: 
                    BS_Conflict_id = np.array([k2])
                else:
                    BS_Conflict_id = np.concatenate((BS_Conflict_id,[k2]),axis=1)            
        tmp1 = np.sum(MNO.mRBA[:,BS_Conflict_id],axis=1) # check again when you have a results. axist = 0 or 1
        tmp11 = np.where(tmp1==0) # find the number of available RBs
        tmp11 = tmp11[0] # get the first array in finding results
        if len(tmp11)>=MNO.mnRBA[[k1],[BS_ind]]:                
            temp111 = MNO.mnRBA[[k1],[BS_ind]]
            temp111 = temp111[0] # because   MNO.mRBA[[k1],[BS_ind]] is an array    
            temp111 = temp111.astype(int) 
            tmp2 = tmp11[0:temp111] # allocate availes RBs to the UE k1
        else: 
            print ('Error: the system is not enought RBs to allocate for this UE!'        )
            sys.exit(1)        
                
        MNO.mRBA[tmp2, [BS_ind]] = 1 # Fill up the used RBs.           
    #### ---> UPdate to virtual UE at the controller    
        UE[k1].BS[-1] = BS_ind  # update cell at UE side        
        UE[k1].P_Tx[-1] = MNO.P_Tx_UExBS_RB[[k1],[BS_ind]] # update transmit power downlink
        UE[k1].RB[np.transpose(tmp2),[-1]] = MNO.mRBA[np.transpose(tmp2), [BS_ind]] # update RBs to UE    
        UE[k1].Rate[-1] = MNO.mnRBA[[k1],[BS_ind]] * MNO.Rate_UExBS_RB[[k1],[BS_ind]] #    
        UE[k1].Power[-1] = MNO.mnRBA[[k1],[BS_ind]] * MNO.P_Tx_UExBS_RB[[k1],[BS_ind]] # Total power     
        UE[k1].Utility[-1] = UE[k1].Rate[-1] - UE[k1].Power[-1]*10000 # cost = 0.1     
        MNO.mUA[[k1],[BS_ind]] = 1 #    
    # ---> Learning ================================================
    print('\n Starting log linear learning algorithm...\n')
    for t in range(nIterations):
        print ('Epoch number:', t , '\n'     )
        print ('Updating paramerters to learn...'      )
        #===========================================================================
        # Do we need update these value when we run the algorithm
        # # Calculate SINR --> this one is recomputed from above
        # MNO.SINR_UE_BS_RB[:] = 0 # reset
        # for k1 in range(MNO.nUE):
        #     for k2 in range(MNO.nBS):
        #         MNO.Intf_UExBS_RB[[k1],[k2]] = np.dot(MNO.P_Rx[[k1],:], MNO.BS_Rmap[:,[k2]]) # Wats            
        #         MNO.SINR_UE_BS_RB[[k1],[k2]] = MNO.P_Rx[[k1],[k2]] / (MNO.Intf_UExBS_RB[[k1],[k2]]  + MNO.N0) # Wats    
        # SINR_dB = 10 * np.log10(MNO.SINR_UE_BS_RB)     
        # MNO.mFUA = (SINR_dB >= -12) # X is variable for association --> true or false valuas    
        # MNO.mnRBA = np.zeros(shape=(MNO.nUE,MNO.nBS))     
        # for k1 in range(MNO.nUE):
        #     for k2 in range(MNO.nBS):
        #         if MNO.mFUA[[k1],[k2]] == 1:
        #             # Calculate Achievable rate per unit RB
        #             MNO.Rate_UExBS_RB[[k1],[k2]] = calculateMaxThroughputOfTheNode.calculateMaxThroughputOfTheNode(SINR_dB[[k1],[k2]],Dist[[k1],[k2]],MNO.rFBS)   # we will execute this one 
        #             # Calculate # of RB to meet UE demand
        #             MNO.mnRBA[[k1],[k2]] = np.ceil(MNO.UE_DL_Demand[k1]/MNO.Rate_UExBS_RB[[k1],[k2]])  # we will execute this one  
        #             
        #===========================================================================
        UE_list = np.random.permutation(MNO.nUE) 
        UE_list = np.array(UE_list) # randomly choose UE index to process
        
        print ('Learning user association... \n')
        for k1 in range(MNO.nUE): 
            k2 = UE_list[k1]   # UE to process
            F_v = np.where(MNO.mFUA[[k2],:]==1) # which BSs are can be connected ?                      
            f_t = UE[k2].BS # list of BSs was connected 
            u_t = UE[k2].Utility # list of Utility was connected 
            iExp = UE[k2].Explored # exploration probability 
            pExp = pExpVec[k2]     # exploration probability 
            beta = UE[k2].beta     #                        
            F_v = F_v[1].astype(int)        
            f_t, u_t, iExp = fun_SelfOrganize.fun_SelfOrganize(F_v,f_t,u_t, iExp,pExp,beta) # each UE                         
            if len(F_v) == 1: 
                pExp = 0                        
            UE[k2].BS = f_t 
            UE[k2].Explored = iExp
            pExpVec[k2] = pExp
            
        print ('Learning resource allocation...')
     
        MNO.mUA[:] = 0
        MNO.mRBA[:] = 0 # why we need delete all database at the controller? we have to reallocte all 
        for k1 in range(MNO.nUE):        
            k2 = UE_list[k1]  # UE index to process       
            BS_ind = UE[k2].BS[[-1]] #         
            BS_ind = BS_ind[0] #BS_ind = 4                
            MNO.mUA[[k2],UE[k2].BS[-1]] = 1 # Associating BS        
            BS_Conflict = MNO.BS_Cmap[[BS_ind],:] # Conflict BS of BS_ind        
            
            #print BS_Conflict[0]
            BS_Conflict_id = []
            BS_Conflict_id = []
            for k3 in range(MNO.nBS):
                if BS_Conflict[0][k3] == 1:
                    if not BS_Conflict_id: 
                        BS_Conflict_id = np.array([k3])
                    else:
                        BS_Conflict_id = np.concatenate((BS_Conflict_id,[k3]),axis=1)        
                        
            tmp1 = np.sum(MNO.mRBA[:,BS_Conflict_id],axis=1) # check again when you have a results. axist = 0 or 1
            tmp11 = np.where(tmp1==0) # find the number of available RBs
            tmp11 = tmp11[0] # get the first array in finding results
            if len(tmp11)>=MNO.mnRBA[[k1],[BS_ind]]:                
                temp111 = MNO.mnRBA[[k1],[BS_ind]]
                temp111 = temp111[0] # because   MNO.mRBA[[k1],[BS_ind]] is an array
                temp111 = temp111.astype(int)     
                tmp2 = tmp11[0:temp111] # allocate availes RBs to the UE k1
            else: 
                print ('Error: the system is not enought RBs to allocate for this UE!'            )
                sys.exit(1)        
    
            MNO.mRBA[tmp2, [BS_ind]] = 1 # Fill up the used RBs.        
    
            print ('Updating data to Virtual UEs ...')
                    
            UE[k2].BS[-1] = BS_ind  # update cell at UE side        
            UE[k2].P_Tx[-1] = MNO.P_Tx_UExBS_RB[[k2],[BS_ind]] # update transmit power downlink
            UE[k2].RB[np.transpose(tmp2),[-1]] = MNO.mRBA[np.transpose(tmp2), [BS_ind]] # updating RBs to UE         
            UE[k2].Rate[-1] = MNO.mnRBA[[k2],[BS_ind]] * MNO.Rate_UExBS_RB[[k2],[BS_ind]] #        
            UE[k2].Power[-1] = MNO.mnRBA[[k2],[BS_ind]] * MNO.P_Tx_UExBS_RB[[k2],[BS_ind]] # Total power         
            UE[k2].Utility[-1] = UE[k2].Rate[-1] - UE[k2].Power[-1]*100 # cost = 0.1         
            MNO.mUA[[k2],[BS_ind]] = 1 #           
                   
            print ('Updating parameter in the learning algorithm ...')
            if np.isnan(UE[k2].Rate[-1]):
                break
            if UE[k2].Utility[-1] >= UE[k2].Utility[-2]:
                UE[k2].beta = UE[k2].beta + beta_step
                pExpVec[k2] = np.max([0, pExpVec[k2]-pEstep])
                                
            tmp1 = UE[k2].BS[-1]        
            MNO.mUA[k2] = tmp1
            MNO.OP_Rate[[k2],[tmp1]] = UE[k2].Rate[-1]
            MNO.OP_Cost[[k2],[tmp1]] = UE[k2].Power[-1]
                
        print ('Exporting output results ')
        MNO.OP2_User[[t],:] = np.transpose(np.sum(MNO.mUA))
        MNO.OP2_User[[t],:] = np.transpose(np.sum(MNO.OP_Rate * MNO.mUA))    
        MNO.OP2_Cost[[t],:] = np.transpose(np.sum(MNO.OP_Cost * MNO.mUA))        
        #===========================================================================
        # Total_pExplore = 0    
        # for k1 in range(MNO.nUE):
        #     Total_pExplore = Total_pExplore + pExpVec[k1]
        # if Total_pExplore == 0:
        #     break
        #===========================================================================
    
    print ('Output: sending our proposals to eNBs and UEs!')
    
    print ('Waiting estimation total utility!')
    
    print ('Mission completed! Goodluck!')
    
    #===============================================================================
    print ('Display information ...')
#    DisplayNetwork.DisplaymRBA_RB_BS(MNO.mRBA, MNO.nRB, MNO.nBS)
#    DisplayNetwork.DisplaymUE1Utility(UE[1].Utility)
    print ('UE[1].Utility=',UE[1].Utility)
    
    return UE[1].Utility
#==============================================================================
# End of algorithm     
#==============================================================================

#==============================================================================
# # testing 
MNO = Controller_Name('----Project Name: Markov approximation-based learning in 5G network---')
#==============================================================================
M1 = [89.75,89.75,89.75] # via BS id set at configuration file
M2 = [21,21,21,21,21] # via UE emei

M3 = np.array([[0, 0, 1],
               [0, 0, 1],
                [1, 1, 0]])

M4 = np.array([[1, 0, 0],
               [0, 1, 0],
                [0, 0,  1]])

M5 =  np.array([[-69.12372078, -74.1376763,  -71.82325875],
                          [-53.83030764, -70.29361338, -74.97618152],
                          [-59.74909419, -67.796359,   -75.62515563],
                          [-66.54979872, -74.95372667, -69.25830752],
                          [-61.29133112, -73.60238591, -70.5957919 ]])
    #===============================================================================
    # print 'Getting SINR level'
    # MNO.P_Rx = 10**(0.1*MNO.P_Rx)
    # #print 'MNO.P_Rx', MNO.P_Rx
    # for k1 in range(MNO.nUE):
    #     for k2 in range(MNO.nBS):
    #         MNO.Intf_UExBS_RB[[k1],[k2]] = np.dot(MNO.P_Rx[[k1],:], MNO.BS_Rmap[:,[k2]]) # Wats
    #         MNO.SINR_UE_BS_RB[[k1],[k2]] = MNO.P_Rx[[k1],[k2]] / (MNO.Intf_UExBS_RB[[k1],[k2]]  + MNO.N0) # Wats
    #
    # SINR_dB = 10*np.log10(MNO.SINR_UE_BS_RB)
M6 =MNO.Intf_UExBS_RB =  np.array([[  6.57164546e-08,   6.57164546e-08,   1.60925213e-07],
                                   [  3.17966852e-08,   3.17966852e-08,   4.23316627e-06],
                                   [  2.73832150e-08,  2.73832150e-08,   1.22557256e-06],
                                   [  1.18623094e-07,   1.18623094e-07,   2.53281241e-07],
                                   [  8.71807921e-08,   8.71807921e-08,   7.86419045e-07]])
M7 = SINR_dB = np.array([[  2.69953797, -2.31441755,  -3.88949969],
                        [ 21.14587388,   4.68256814, -21.24283479],
                        [ 15.87606144,   7.82879663, -16.50854592],
                        [  2.7085088,   -5.69541915,  -3.29433778],
                        [  9.30446078,  -3.00659401,  -9.55233212]])



result = scheduling_algoirthm(M1,M2,M3,M4,M5,M6,M7)