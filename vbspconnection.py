#!/usr/bin/env python3
#
# Copyright (c) 2016 Supreeth Herle
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied. See the License for the
# specific language governing permissions and limitations
# under the License.

"""VBSP Connection."""
#from numpy import int
#import numpy as np 
import time
import tornado.ioloop
import socket
import sys
from numpy import int
import numpy as np
# from scipy.spatial.distance import cdist
import random
from cvxpy import error
from empower.vbsp.project_modules import *
import sys
import struct
from protobuf_to_dict import protobuf_to_dict
from empower.vbsp import EMAGE_VERSION
from empower.vbsp import PRT_UE_JOIN
from empower.vbsp import PRT_UE_LEAVE
from empower.vbsp import PRT_VBSP_HELLO
from empower.vbsp import PRT_VBSP_BYE
from empower.vbsp import PRT_VBSP_REGISTER
from empower.vbsp import PRT_VBSP_TRIGGER_EVENT
from empower.vbsp import PRT_VBSP_AGENT_SCHEDULED_EVENT
from empower.vbsp import PRT_VBSP_SINGLE_EVENT
from empower.vbsp.messages import main_pb2
from empower.vbsp.messages import configs_pb2
from empower.core.utils import hex_to_ether
from empower.core.utils import ether_to_hex
from empower.core.ue import UE
import scipy.io
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.ticker as ticker
from matplotlib import colors as mcolors
#from empower.vbsp.embeded_code import scheduling_algoirthm




from empower.main import RUNTIME

import empower.logger
LOG = empower.logger.get_logger()


# update to history 

#su_t = np.zeros(1000, dtype=float)
#file_to_save = 'SavedHistUtility.mat'
#scipy.io.savemat(file_to_save, mdict={'M1': su_t}, oned_as='row')     




#def create_header(t_id, b_id, header, ue_list):
def create_header(t_id, b_id, header,mUA, mPA, GRB1, GRB2, GRB3, GRB4, GRB5, td1, td2, td3, td4, td5, td6,
                  td7, td8, td9, td10, td11, td12, td13, td14, td15, td16, td17, td18, td19, td20 ):
    if not header:
        LOG.error("header parameter is None")

    header.vers = EMAGE_VERSION
    # Set the transaction identifier (module id).
    header.t_id = t_id
    # Set the Base station identifier.
    header.b_id = b_id
    # Start the sequence number for messages from zero.
    header.seq = 0
    # added
    header.mUA = mUA
    header.mPA = mPA
    header.GRB1 = GRB1
    header.GRB2 = GRB2
    header.GRB3 = GRB3
    header.GRB4 = GRB4
    header.GRB5 = GRB5
    header.td1 = td1
    header.td2 = td2
    header.td3 = td3
    header.td4 = td4
    header.td5 = td5
    header.td6 = td6
    header.td7 = td7
    header.td8 = td8
    header.td9 = td9
    header.td10 = td10
    header.td11 = td11
    header.td12 = td12
    header.td13 = td13
    header.td14 = td14
    header.td15 = td15
    header.td16 = td16
    header.td17 = td17
    header.td18 = td18
    header.td19 = td19
    header.td20 = td20

    #header.power = power
def serialize_message(message):
    """Serialize message."""

    if not message:
        LOG.error("message parameter is None")
        return None

    return message.SerializeToString()


def deserialize_message(serialized_data):
    """De-Serialize message."""

    if not serialized_data:
        LOG.error("Received serialized data is None")
        return None

    msg = main_pb2.emage_msg()
    msg.ParseFromString(serialized_data)
    return msg


class Controller_Name:
    nBS = 0  # Number of BSs
    nMBS = 0  # Number of MBSs
    nPBS = 0  # Number of PBSs
    nFBS = 0  # Number of GBSs

    nRB = 0  # Number of resource blocks

    nUE = 0  # Number of UEs

    mUA = []  # User association matrix
    mFUA = []  # User association matrix
    mRBA = []  # Resource blocks allocation matrix

    rMBS = 0  # Radius of MBS
    rPBS = 0  # Radius of PBS
    rFBS = 0  # Radius of FBS

    pBS = []  # Transmit power of all BSs
    pMBS = 0  # Radius of MBS
    pPBS = 0  # Radius of PBS
    pFBS = 0  # Radius of FBS

    cBS = []  # Coor of MBS
    cMBS =[]  # Coor of MBS
    cPBS =[]  # Coor of PBS
    cFBS =[]  # Coor of FBS

    cUE = [] # Coor of FBS

    RefPL = [] # nBSx1

    BS_Dist = [] # nBS x nBS: distance among BSs

    FFT_size = 0

    def __init__(self, name): # project name
        self.name = name
    def info(self,Controller_Name):
        print('nBS= {0}, nUE= {1}, nRB:= {2}'.format(Controller_Name.nBS,
              Controller_Name.nRB,Controller_Name.nUE))
        return 0

class BS_Types(object):
    """__init__() functions as the class constructor"""
    def __init__(self, Type='None', TxPower_sCH=[], TxHeight=0,TxGain = 0,
                 CellRadius = 0, RefPL = 0, TotalPower = 0):
        self.Type = Type
        self.TxPower_sCH = TxPower_sCH;   # Per sub-channel Transmit Power [watt]
        self.TxHeight = TxHeight; # Transmit antenna height [metre]
        self.TxGain = TxGain; # Transmit antenna gain [dBi]
        self.CellRadius = CellRadius; # Cell radius of BS [metre]
        self.RefPL = RefPL; # Reference path loss [dBm]
        self.TotalPower = TotalPower;

class User_Equipment(object):
    """__init__() user equipment class"""
    def __init__(self, name='None', BS=None, P_Tx=None,RB = None, Rate = None,
                 Power = None,pExp = None,Explored = None, Utility = None):
        self.name = name
        self.BS = BS
        self.P_Tx = P_Tx
        self.RB = RB
        self.Rate = Rate
        self.Power = Power
        self.pExp = pExp
        self.Explored = Explored
        self.Utility = Utility

class Base_Station(object):
    """__init__() base station class"""
    def __init__(self, name='None', cell_radius = 0, user_association=0,
                 transmit_power=0,uplink_RB_allocation = [],
                 downlink_RB_allocation = [],cell_location = [],RefRP = 0,TxPower_RB=[]):
        self.name = name
        self.user_association = user_association
        self.transmit_power = transmit_power
        self.uplink_RB_allocation = uplink_RB_allocation
        self.downlink_RB_allocation = downlink_RB_allocation
        self.cell_location = cell_location
        self.cell_radius = cell_radius
        self.RefRP = RefRP
        self.TxPower_RB = TxPower_RB

def DisplaymUE1Utility(Utility):
    plt.figure(1)
    ax = plt.gca()
    ax.cla()
    # plt.axis([0,nUE,0,nRB])
    L = range(len(Utility))
    plt.plot(L, Utility)
    plt.xlabel('History')
    plt.ylabel('Utility')
    plt.title('UE utility')
    plt.show()
    return 0

def DisplaymRBA_RB_BS(mRBA_BS, nRB, nBS):
    plt.figure(2)
    fig, ax1 = plt.subplots()
    ax = plt.gca()
    ax.cla()
    for i in range(nBS):
        for j in range(nRB):
            if mRBA_BS[[j], [i]] == 1:
                plt.plot(j, i, 'rs', ms=10)
            else:
                plt.plot(j, i, 'gs', ms=10)
    plt.xlabel('RB index')
    plt.ylabel('BS index')
    plt.title('RB allocation to BSs')
    ax1.xaxis.set_ticks(np.arange(0, nRB, 1))
    ax1.xaxis.set_major_formatter(ticker.FormatStrFormatter('%1i'))
    ax1.yaxis.set_ticks(np.arange(0, nBS, 1))
    ax1.yaxis.set_major_formatter(ticker.FormatStrFormatter('%1i'))
    plt.grid(True)
    plt.axis([-0.5, nRB, -0.5, nBS])
    ax1.clear()
    plt.show()
    plt.close()

    return 1


# ===============================================================================
def scheduling_algoirthm(M1, M2, M3, M4, M5, M6, M7):
    MNO = Controller_Name('----Project Name: Markov approximation-based learning in 5G network---')
    ###### ----> INPUT PARAMETERs

    # Read data from messages sent from eNBs:
    #

    #print ('Updating network parameter from eNB and UE to SDN controller...')
    # Network size
    MNO.nBS = 3;  # Number of BSs
    MNO.nFBS = 3;  # Number of FBSs
    MNO.nUE = 5;  # Number of UEs
    MNO.nRB = 25;  # Number of RBs
    MNO.nTotCar = 300;  # Total number of subcarriers = 25 RB
    nHistory = 100
    #print ('Initializing Algorithm parameters')
    nIterations = 80
    beta_step = 8
    conv_stop = 50
    Algorithm = 3  # MCDA = 1; PLLA = 2; SOA = 3;
    if Algorithm == 1:  # MCDA
        pExp = 1
        pEstep = 0
        Str2 = 'OP_MA_' + str(MNO.nUE) + '.mat'
    if Algorithm == 2:  # PLLA
        pExp = 0.5
        pEstep = 0
        Str2 = 'OP_LL_' + str(MNO.nUE) + '.mat'
    if Algorithm == 3:  # SOA
        pExp = 1
        pEstep = 0.1
        Str2 = 'OP_SOA_' + str(MNO.nUE) + '.mat'
    # initialization matrix to update:
    #print ('Initializing output parameters to the MNO...')
    MNO.P_Tx_UExBS_RB = np.zeros(shape=(MNO.nUE, MNO.nBS), dtype=float)
    MNO.Rate_UExBS_RB = np.zeros(shape=(MNO.nUE, MNO.nBS), dtype=float)
    MNO.Intf_UExBS_RB = np.zeros(shape=(MNO.nUE, MNO.nBS), dtype=float)
    MNO.mnRBA = np.zeros(shape=(MNO.nUE, MNO.nBS), dtype=int)
    MNO.SINR_UE_BS_RB = np.zeros(shape=(MNO.nUE, MNO.nBS), dtype=float)
    MNO.mUA = np.zeros(shape=(MNO.nUE, MNO.nBS), dtype=int)  #
    MNO.mRBA = np.zeros(shape=(MNO.nRB, MNO.nBS), dtype=bool)  # resource allocation
    MNO.OP_Rate = np.zeros(shape=(MNO.nUE, MNO.nBS), dtype=float)
    MNO.OP_Cost = np.zeros(shape=(MNO.nUE, MNO.nBS), dtype=float)
    MNO.OP2_User = np.zeros(shape=(nIterations, MNO.nBS), dtype=int)
    MNO.OP2_User = np.zeros(shape=(nIterations, MNO.nBS), dtype=float)
    MNO.OP2_Cost = np.zeros(shape=(nIterations, MNO.nBS), dtype=float)
    MNO.BS_Cmap = np.zeros(shape=(MNO.nBS, MNO.nBS), dtype=float)
    MNO.BS_Rmap = np.zeros(shape=(MNO.nBS, MNO.nBS), dtype=float)
    P = np.zeros(shape=(MNO.nRB, MNO.nBS))  # Control variable for power
    U = np.zeros(shape=(MNO.nUE, MNO.nBS))  # Utility --> Revenue - Cost
    pExpVec = np.ones(MNO.nUE, dtype=float)
    # ===============================================================================
    # ===============================================================================
    #print ('Getting Device information from testbed system')
    BS_id_list = ["3618", "3619", "3620"]  # via BS id set at configuration file
    UE_id_list = ["UE-id-1", "UE-id-2", "UE-id-3", "UE-id-4", "UE-id-5"]  # via UE emei
    tx_gain_bs = M1  # [89.75,89.75,89.75] # via BS id set at configuration file
    rx_gain_ue = M2  # [21,21,21,21,21] # via UE emei
    #print ('Conflict and Resue Graphs for Base Stations ... ')  # where???
    MNO.BS_Cmap = M3  # np.array([[0, 0, 1],
    #                            [0, 0, 1],
    #                           [1, 1, 0]])
    MNO.BS_Rmap = M4  # np.array([[1, 0, 0],
    #                          [0, 1, 0],
    #                         [0, 0,  1]])
    MNO.P_Rx = M5  # np.array([[-69.12372078, -74.1376763,  -71.82325875],
    #                      [-53.83030764, -70.29361338, -74.97618152],
    #                     [-59.74909419, -67.796359,   -75.62515563],
    #                    [-66.54979872, -74.95372667, -69.25830752],
    #                   [-61.29133112, -73.60238591, -70.5957919 ]])
    # ===============================================================================
    # print 'Getting SINR level'
    # MNO.P_Rx = 10**(0.1*MNO.P_Rx)
    # #print 'MNO.P_Rx', MNO.P_Rx
    # for k1 in range(MNO.nUE):
    #     for k2 in range(MNO.nBS):
    #         MNO.Intf_UExBS_RB[[k1],[k2]] = np.dot(MNO.P_Rx[[k1],:], MNO.BS_Rmap[:,[k2]]) # Wats
    #         MNO.SINR_UE_BS_RB[[k1],[k2]] = MNO.P_Rx[[k1],[k2]] / (MNO.Intf_UExBS_RB[[k1],[k2]]  + MNO.N0) # Wats
    #
    # SINR_dB = 10*np.log10(MNO.SINR_UE_BS_RB)
    # --> MNO.Intf_UExBS_RB = M6  # np.array([[  6.57164546e-08,   6.57164546e-08,   1.60925213e-07],
    #                               [  3.17966852e-08,   3.17966852e-08,   4.23316627e-06],
    #                              [  2.73832150e-08,  2.73832150e-08,   1.22557256e-06],
    #                             [  1.18623094e-07,   1.18623094e-07,   2.53281241e-07],
    #                            [  8.71807921e-08,   8.71807921e-08,   7.86419045e-07]])
    SINR_dB = M7  # np.array([[  2.69953797, -2.31441755,  -3.88949969],
    #                [ 21.14587388,   4.68256814, -21.24283479],
    #               [ 15.87606144,   7.82879663, -16.50854592],
    #              [  2.7085088,   -5.69541915,  -3.29433778],
    #             [  9.30446078,  -3.00659401,  -9.55233212]])
    MNO.pFBS = 30  # Power of FBSs
    Noise = calculateNoise.calculateNoise(5)  # [dBm] Thermal noise floor with BW = 5MHz.
    MNO.N0 = 10 ** ((Noise - 30) / 10)  # [W]
    # ===============================================================================
    MNO.UE_DL_Demand = np.array([1650000, 1350000, 1200000, 1500000, 1350000])
    MNO.UE_DL_Demand = MNO.UE_DL_Demand*2.5
    # ===============================================================================
    # =========Initialization classes
    #print ('Initializing BSs and UEs')
    # base station
    base_station = []
    i = 0
    for i in range(MNO.nBS):
        base_station.append(Base_Station('FBS-id:= fbs-' + str(i), MNO.rFBS, [], MNO.pFBS, [], [], [], 0, MNO.pFBS))
        # user
    UE = []
    for i in range(MNO.nUE):
        UE.append(User_Equipment('UE-id:= ue-' + str(i), [], [], [], [], [], [], [], []))
    # ===============================================================================
    #print ('updating base station id .\n')
    for i in range(MNO.nBS):
        base_station[i].name = BS_id_list[i]

    #print ('updating UE id .\n')
    for i in range(MNO.nUE):
        UE[i].name = UE_id_list[i]

    # === --> Compute RBs for each virutal UE given the UE demand
    MNO.mFUA = (SINR_dB >= -12)  # 9 dBm is interference threshold
    for k1 in range(MNO.nUE):
        for k2 in range(MNO.nBS):
            if MNO.mFUA[[k1], [k2]] == 1:
                # Calculate Achievable rate per unit RB
                MNO.Rate_UExBS_RB[[k1], [k2]] = calculateMaxThroughputOfTheNode.calculateMaxThroughputOfTheNode(
                    SINR_dB[[k1], [k2]], 100, 50)
                # Calculate # of RB to meet UE demand
                number = np.ceil(MNO.UE_DL_Demand[k1] / MNO.Rate_UExBS_RB[[k1], [k2]])  # we will execute this one
                MNO.mnRBA[[k1], [k2]] = int(number)

    for k1 in range(MNO.nUE):
        UE[k1].BS = np.zeros(nHistory, dtype=int)
        UE[k1].P_Tx = np.zeros(nHistory, dtype=float)
        UE[k1].RB = np.zeros(shape=(MNO.nRB, nHistory), dtype=bool)
        UE[k1].Rate = np.zeros(nHistory, dtype=float)
        UE[k1].Power = np.zeros(nHistory, dtype=float)
        UE[k1].Utility = np.zeros(nHistory, dtype=float)
        UE[k1].beta = 0
        UE[k1].Explored = 0
    ##### --> UA allocation between virutal BSs and virtual UEs
    for k1 in range(MNO.nUE):
        SINR_max = np.amax(
            SINR_dB[[k1], :])  # Maximum SINR UE association --> will create an array[ [0,0,0], [1, 3, 5]] for ex.
        BS_ind1 = np.where(SINR_dB[[k1], :] == SINR_max)  # Maximum SINR UE association
        BS_ind = BS_ind1[1][0]
        MNO.mUA[[k1], [BS_ind]] = 1  # cell association
        ##### ---> RBs allocation to virtual UEs
        BS_Conflict = MNO.BS_Cmap[[BS_ind], :]  # Conflict BS of BS_ind
        # print (BS_Conflict[0])
        BS_Conflict_id = []
        BS_Conflict_id = []
        for k2 in range(MNO.nBS):
            if BS_Conflict[0][k2] == 1:
                if not BS_Conflict_id:
                    BS_Conflict_id = np.array([k2])
                else:
                    BS_Conflict_id = np.concatenate((BS_Conflict_id, [k2]), axis=1)

        # # update spectrum sensing results:
        # data_to_get_3618 = scipy.io.loadmat('SavedDataSS_3618.mat')
        # MSS_3618 = data_to_get_3618['SS_3618']
        # data_to_get_3619 = scipy.io.loadmat('SavedDataSS_3619.mat')
        # MSS_3619 = data_to_get_3619['SS_3619']
        # data_to_get_3620 = scipy.io.loadmat('SavedDataSS_3620.mat')
        # MSS_3620 = data_to_get_3620['SS_3620']
        # # update to MNO.mRBA
        # for rb_index in range(25):
        #     if MSS_3618[rb_index] == 1:
        #         MNO.mRBA[[rb_index][0]] = 1
        #     if MSS_3618[rb_index] == 1:
        #         MNO.mRBA[[rb_index][1]] = 1
        #     if MSS_3618[rb_index] == 1:
        #         MNO.mRBA[[rb_index][2]] = 1
        # # End of updating

        tmp1 = np.sum(MNO.mRBA[:, BS_Conflict_id], axis=1)  # check again when you have a results. axist = 0 or 1
        tmp11 = np.where(tmp1 == 0)  # find the number of available RBs
        tmp11 = tmp11[0]  # get the first array in finding results
        if len(tmp11) >= MNO.mnRBA[[k1], [BS_ind]]:
            temp111 = MNO.mnRBA[[k1], [BS_ind]]
            temp111 = temp111[0]  # because   MNO.mRBA[[k1],[BS_ind]] is an array
            temp111 = temp111.astype(int)
            tmp2 = tmp11[0:temp111]  # allocate availes RBs to the UE k1
        else:
            print ('Error: the system is not enought RBs to allocate for this UE!')
            sys.exit(1)

        MNO.mRBA[tmp2, [BS_ind]] = 1  # Fill up the used RBs.
        #### ---> UPdate to virtual UE at the controller
        UE[k1].BS[-1] = BS_ind  # update cell at UE side
        UE[k1].P_Tx[-1] = MNO.P_Tx_UExBS_RB[[k1], [BS_ind]]  # update transmit power downlink
        UE[k1].RB[np.transpose(tmp2), [-1]] = MNO.mRBA[np.transpose(tmp2), [BS_ind]]  # update RBs to UE
        UE[k1].Rate[-1] = MNO.mnRBA[[k1], [BS_ind]] * MNO.Rate_UExBS_RB[[k1], [BS_ind]]  #
        UE[k1].Power[-1] = MNO.mnRBA[[k1], [BS_ind]] * MNO.P_Tx_UExBS_RB[[k1], [BS_ind]]  # Total power
        UE[k1].Utility[-1] = UE[k1].Rate[-1] - UE[k1].Power[-1] * 0.1  # cost = 0.1
        MNO.mUA[[k1], [BS_ind]] = 1  #
    # ---> Learning ================================================
    #print('\n Starting log linear learning algorithm...\n')
    for t in range(nIterations):
        #print ('Epoch number:', t, '\n')
        #print ('Updating paramerters to learn...')
        # ===========================================================================
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
        # ===========================================================================
        UE_list = np.random.permutation(MNO.nUE)
        UE_list = np.array(UE_list)  # randomly choose UE index to process

        #print ('Learning user association... \n')
        for k1 in range(MNO.nUE):
            k2 = UE_list[k1]  # UE to process
            F_v = np.where(MNO.mFUA[[k2], :] == 1)  # which BSs can be connected ?
            f_t = UE[k2].BS  # list of BSs was connected
            u_t = UE[k2].Utility  # list of Utility was connected
            iExp = UE[k2].Explored  # exploration probability
            pExp = pExpVec[k2]  # exploration probability
            beta = UE[k2].beta  #
            F_v = F_v[1].astype(int)
            f_t, u_t, iExp = fun_SelfOrganize.fun_SelfOrganize(F_v, f_t, u_t, iExp, pExp,
                                                               beta)  # each UE
            if len(F_v) == 1:
                pExp = 0
            UE[k2].BS = f_t
            UE[k2].Explored = iExp
            pExpVec[k2] = pExp
        
        # print ('UE[k2].BS',UE[k2].BS)

        #print ('Learning resource allocation...')

        MNO.mUA[:] = 0
        MNO.mRBA[:] = 0  # why we need delete all database at the controller? we have to reallocte all
        # Updating SINR, CQI, ...

        for k1 in range(MNO.nUE):
            k2 = UE_list[k1]  # UE index to process
            BS_ind = UE[k2].BS[[-1]]  #
            BS_ind = BS_ind[0]  # BS_ind = 4
            MNO.mUA[[k2], UE[k2].BS[-1]] = 1  # Associating BS
            BS_Conflict = MNO.BS_Cmap[[BS_ind], :]  # Conflict BS of BS_ind

            # print BS_Conflict[0]
            BS_Conflict_id = []
            BS_Conflict_id = []
            for k3 in range(MNO.nBS):
                if BS_Conflict[0][k3] == 1:
                    if not BS_Conflict_id:
                        BS_Conflict_id = np.array([k3])
                    else:
                        BS_Conflict_id = np.concatenate((BS_Conflict_id, [k3]), axis=1)

            tmp1 = np.sum(MNO.mRBA[:, BS_Conflict_id], axis=1)  # check again when you have a results. axist = 0 or 1
            tmp11 = np.where(tmp1 == 0)  # find the number of available RBs
            tmp11 = tmp11[0]  # get the first array in finding results
            if len(tmp11) >= MNO.mnRBA[[k1], [BS_ind]]:
                temp111 = MNO.mnRBA[[k1], [BS_ind]]
                temp111 = temp111[0]  # because   MNO.mRBA[[k1],[BS_ind]] is an array
                temp111 = temp111.astype(int)
                tmp2 = tmp11[0:temp111]  # allocate availes RBs to the UE k1
            else:
                print ('Error: the system is not enought RBs to allocate for this UE!')
                sys.exit(1)

            MNO.mRBA[tmp2, [BS_ind]] = 1  # Fill up the used RBs.

            #print ('Updating data to Virtual UEs ...')

            UE[k2].BS[-1] = BS_ind  # update cell at UE side
            UE[k2].P_Tx[-1] = MNO.P_Tx_UExBS_RB[[k2], [BS_ind]]  # update transmit power downlink
            UE[k2].RB[np.transpose(tmp2), [-1]] = MNO.mRBA[np.transpose(tmp2), [BS_ind]]  # updating RBs to UE
            UE[k2].Rate[-1] = MNO.mnRBA[[k2], [BS_ind]] * MNO.Rate_UExBS_RB[[k2], [BS_ind]]  #
            UE[k2].Power[-1] = MNO.mnRBA[[k2], [BS_ind]] * MNO.P_Tx_UExBS_RB[[k2], [BS_ind]]  # Total power
            UE[k2].Utility[-1] = UE[k2].Rate[-1] - UE[k2].Power[-1] * 100  # cost = 0.1
            MNO.mUA[[k2], [BS_ind]] = 1  #

            #print ('Updating parameter in the learning algorithm ...')
            if np.isnan(UE[k2].Rate[-1]):
                break
            if UE[k2].Utility[-1] >= UE[k2].Utility[-2]:
                UE[k2].beta = UE[k2].beta + beta_step
                pExpVec[k2] = np.max([0, pExpVec[k2] - pEstep])

            tmp1 = UE[k2].BS[-1]
            MNO.mUA[k2] = tmp1
            MNO.OP_Rate[[k2], [tmp1]] = UE[k2].Rate[-1]
            MNO.OP_Cost[[k2], [tmp1]] = UE[k2].Power[-1]


        #print MNO.mUE
         
        


        #print ('Exporting output results ')
        MNO.OP2_User[[t], :] = np.transpose(np.sum(MNO.mUA))
        MNO.OP2_User[[t], :] = np.transpose(np.sum(MNO.OP_Rate * MNO.mUA))
        MNO.OP2_Cost[[t], :] = np.transpose(np.sum(MNO.OP_Cost * MNO.mUA))
        # ===========================================================================
        # Total_pExplore = 0
        # for k1 in range(MNO.nUE):
        #     Total_pExplore = Total_pExplore + pExpVec[k1]
        # if Total_pExplore == 0:
        #     break
        # ===========================================================================

    # print ('Output: sending our proposals to eNBs and UEs!')

    # print ('Waiting estimation total utility!')

    # print ('Mission completed! Goodluck!')

    # ===============================================================================
    # print ('Display information ...')
    #    DisplayNetwork.DisplaymRBA_RB_BS(MNO.mRBA, MNO.nRB, MNO.nBS)
    #    DisplayNetwork.DisplaymUE1Utility(UE[1].Utility)
    # print ('UE[1].Utility=', UE[1].Utility)
    #MNO.mUA [[0 0 0]
    #[0 0 0]
    #[1 1 1]
    #[0 0 0]
    #[0 0 0]]
    
    print ('UE[k2].RB', UE[k2].RB)

    ua = "23232"
    x = list(ua)
    for i in range(5):       
        bs_i = MNO.mUA[i][1]
        if bs_i == 0:
            s = '1'     
        elif bs_i ==1:
            s = '2'
        elif bs_i ==2:
            s = '3'         
        x[i] = s 
        
    ua = "".join(x)	
    print ('MNO.mUA', ua)
    #print ('ua',ua)
    ua_int = int(ua)
   
    # need to write a function represent resource block allocation 
    # we have UA and resource block for each UE connect to each BS. 
    # 1. Form matrix nUE x nRB to allocate. 
    print ('MNO.mnRBA', MNO.mnRBA)
    #mRBA = np.zeros(shape=(5,25),int)
    #index = 0
    #for n in range(5):
    #    nRB_UE = MNO.mnRBA[[n][MNO.mUA[n][1]]]
    #    print ('nRB_UE',nRB_UE)
#	# mRBA[[n],(index:(index+nRB_UE))] == 1
 #       index = index + nRB_UE   	
    #print ('mRBA',mRBA)

    
    LA_UA = np.array([ua_int])
    # LA_UA = np.array([22232])
    print ('LA_UA',LA_UA)

    #
    # Updating MNO.mnRBA
    smUA = str(ua_int)
    lsmUA = list(smUA)
    print ('lsmUA',lsmUA)

    mRBA = np.zeros(shape=(5, 25), dtype=int)
    index = 0
    for n in range(5):
        # print ('lsmUA',lsmUA)
        s = lsmUA[n]
        ss = int(s)
        print ('n',n, 'ss', ss)
        nRBiUE = MNO.mnRBA[n][ss - 1]
        print ('nRB_UE', nRBiUE)
        mRBA[n, index:(index+nRBiUE)] = 1
        index = index + nRBiUE
    print ('mRBA', mRBA)

    # for i1 in range(5):
    # 	for i2 in range(25):
    # 		print mRBA[i1, i2]
    #
    LA_DRBA_1 = ['1', '0', '0', '0', '0', '0']
    LA_DRBA_2 = ['2', '0', '0', '0', '0', '0']
    LA_DRBA_3 = ['3', '0', '0', '0', '0', '0']
    LA_DRBA_4 = ['4', '0', '0', '0', '0', '0']
    LA_DRBA_5 = ['5', '0', '0', '0', '0', '0']

    index = 0
    for g in range(5):
        index = 5 * g
        mrb = mRBA[:, index:5+5*g]
    # print mrb
        for ue in range(5):
            s = ue + 1
            ss = str(s)
            for grb in range(5):
                if mrb[ue, grb] == 1:
                    if g == 0:
                        LA_DRBA_1[grb+1] = ss
                    elif g == 1:
                        LA_DRBA_2[grb+1] = ss
                    elif g == 2:
                        LA_DRBA_3[grb+1] = ss
                    elif g == 3:
                        LA_DRBA_4[grb+1] = ss
                    elif g == 4:
                        LA_DRBA_5[grb+1] = ss

    LA_DRBA_1_ = "".join(LA_DRBA_1)
    LA_DRBA_2_ = "".join(LA_DRBA_2)
    LA_DRBA_3_ = "".join(LA_DRBA_3)
    LA_DRBA_4_ = "".join(LA_DRBA_4)
    LA_DRBA_5_ = "".join(LA_DRBA_5)

    LA_DRBA_1int = int(LA_DRBA_1_)
    LA_DRBA_2int = int(LA_DRBA_2_)
    LA_DRBA_3int = int(LA_DRBA_3_)
    LA_DRBA_4int = int(LA_DRBA_4_)
    LA_DRBA_5int = int(LA_DRBA_5_)

    print (LA_DRBA_1int, LA_DRBA_2int, LA_DRBA_3int, LA_DRBA_4int, LA_DRBA_5int)

    LA_DRBA = np.array([120101, 202020, 355005, 401030, 510403]) # 1060070080090100,1110120130140150,1160170180190200,1210220230240250])
    #
    LA_DRBA[0] = LA_DRBA_1int
    LA_DRBA[1] = LA_DRBA_2int
    LA_DRBA[2] = LA_DRBA_3int
    LA_DRBA[3] = LA_DRBA_4int
    LA_DRBA[4] = LA_DRBA_5int

    LA_DPA = np.array([302040])

    x = len(UE[1].Utility)
    mu = np.zeros(shape=(5,x))
    for ue in range(5):
        mu[[ue][:]] = UE[ue].Utility
    su = mu.sum(axis=0, dtype='float')
    #time.sleep(1)
    #print ('su =', su)
    #print ('x=', mu)
    #print ('UE[ue].Utility=',UE[ue].Utility)
    #DisplaymUE1Utility(su)
    #DisplaymRBA_RB_BS(MNO.mRBA, 25, 3)
    #time.sleep(1)
    file_to_save = 'SavedDatautility.mat'
    scipy.io.savemat(file_to_save, mdict={'M1': su}, oned_as='row')

    file_to_save = 'SavedRBA.mat'
    scipy.io.savemat(file_to_save, mdict={'M1': mRBA}, oned_as='row')

    file_to_save = 'SavedmUA.mat'
    scipy.io.savemat(file_to_save, mdict={'M1': MNO.mUA}, oned_as='row')

    # get newest utility to update    

    file_to_save = 'SavedHistUtility.mat'
    data_to_get = scipy.io.loadmat(file_to_save) 
    su_tt = data_to_get['M1']
    su_t = su_tt[0]
    
    # print ('su_t=', su_t)
    Utility = su[90]
    old_u_t = su_t[1:(len(su_t)-1)]
    su_t[0:(len(su_t)-2)] = old_u_t # update configuratin history; len(f_t) = 1:end-1 in matlab 
    su_t[len(su_t)-2]  = Utility


    # update to history 
    file_to_save = 'SavedHistUtility.mat'
    scipy.io.savemat(file_to_save, mdict={'M1': su_t}, oned_as='row')         


    return UE[1].Utility, LA_UA, LA_DPA, LA_DRBA



class VBSPConnection(object):
    """VBSP Connection.
    Represents a connection to a ENB (EUTRAN Base Station) using
    the VBSP Protocol. One VBSPConnection object is created for every
    ENB in the network. The object implements the logic for handling
    incoming messages. The currently supported messages are:

    Attributes:
        stream: The stream object used to talk with the ENB.
        address: The connection source address, i.e. the ENB IP address.
        server: Pointer to the server object.
        vbs: Pointer to a VBS object.
    """
    def __init__(self, stream, addr, server):
        self.stream = stream
        self.stream.set_nodelay(True)
        self.addr = addr
        self.server = server
        self.vbs = None
        self.seq = 0
        self.stream.set_close_callback(self._on_disconnect)
        self.__buffer = b''
        self._hb_interval_ms = 500
        self._hb_worker = tornado.ioloop.PeriodicCallback(self._heartbeat_cb,
                                                          self._hb_interval_ms)
        self.endian = sys.byteorder
        self._hb_worker.start()
        self._wait()

    def to_dict(self):
        """Return dict representation of object."""

        return self.addr

    def _heartbeat_cb(self):
        """Check if connection is still active."""

        if self.vbs and not self.stream.closed():
            timeout = (self.vbs.period / 1000) * 3
            if (self.vbs.last_seen_ts + timeout) < time.time():
                LOG.info('Client inactive %s at %r', self.vbs.addr, self.addr)

    def stream_send(self, message):
        """Send message."""
        mUA = 1.0
        mPA = 1.0
        GRB1= 1.0
        GRB2 = 1.0
        GRB3 = 1.0

        # Update the sequence number of the messages
        message.head.seq = self.seq + 1
        # added for testing
        message.head.mUA= mUA
        message.head.mPA = mPA
        message.head.GRB1= GRB1
        message.head.GRB2 =  GRB2
        message.head.GRB2 = GRB3

        # LOG.info("Testing: version %s Data1 %s, Data2 %s , Data3 %s Head %s  Seq number %u", message.head.mUA ,
        # message.head.mPA, message.head.GRB1, message.head.GRB2, message, message.head.seq)
        MNO = Controller_Name('----Project Name: Markov approximation-based learning in 5G network---')

        print ("Getting data from the packet \n") # This section is taken from

        nBS = 3;  # Number of BSs
        nFBS = 3;  # Number of FBSs
        nUE = 5;  # Number of UEs
        nRB = 25;  # Number of RBs
        nTotCar = 300;  # Total number of subcarriers = 25 RB

        M1 = [89.75, 89.75, 89.75]  # via BS id set at configuration file
        M2 = [89.75, 89.75, 89.75]  # via BS id set at configuration file

        M3 = np.array([[0, 0, 0],
                       [0, 0, 0],
                       [0, 0, 0]])
        # M3 = np.array([[0, 0, 1], # old data
        #                [0, 0, 1],
        #                [1, 1, 0]])

        M4 = np.array([[1, 1, 1],
                       [1, 1, 1],
                       [1, 1, 1]])

        # M4 = np.array([[1, 0, 0], # old data
        #                [0, 1, 0],
        #                [0, 0, 1]])

        M5 = np.array([[-84.12372078, -73.1376763, -71.82325875],
                        [-86.83030764, -90.29361338, -74.97618152],
                        [-91.74909419, -77.796359, -80.62515563],
                        [-70.54979872, -84.95372667, -79.25830752],
                        [-85.29133112, -76.60238591, -80.5957919]])
        # getting data_to_save = M5
        file_to_save = 'SavedDataM5Index.mat'
        # scipy.io.savemat(file_to_save, mdict={'M5': M5, 'index': condition}, oned_as='row')
        data_to_get = scipy.io.loadmat(file_to_save)
        M5 = data_to_get['M5']
        index1 = data_to_get['index1']
        index2 = data_to_get['index2']
        index3 = data_to_get['index3']

        # M5 = M5-30;

        # M6 = np.array([[6.57164546e-08, 6.57164546e-08, 1.60925213e-07],
        #                                    [3.17966852e-08, 3.17966852e-08, 4.23316627e-06],
        #                                    [2.73832150e-08, 2.73832150e-08, 1.22557256e-06],
        #                                    [1.18623094e-07, 1.18623094e-07, 2.53281241e-07],
        #                                    [8.71807921e-08, 8.71807921e-08, 7.86419045e-07]]) #MNO.Intf_UExBS_RB =

        # M7 = np.array([[2.69953797, -2.31441755, -3.88949969],
        #             [21.14587388, 4.68256814, -21.24283479],
        #             [15.87606144, 7.82879663, -16.50854592],
        #             [2.7085088, -5.69541915, -3.29433778],
        #             [9.30446078, -3.00659401, -9.55233212]]) # SINR_dB

        # tx_gain_bs = M1
        # rx_gain_ue = M2
        #
        # MNO.BS_Cmap = M3
        # MNO.BS_Rmap = M4
        # MNO.P_Rx = M5
        # MNO.Intf_UExBS_RB = M6
        # SINR_dB = M7
        updating_finish = 0
        in1 = 0
        in2 = 0
        in3 = 0
        while (updating_finish == 0):
            # Read data from packet
            BS_ID = self.b_id
            T_ID1 = self.td1 # spectrum_sensing_grb1;
            T_ID2 = self.td2 # spectrum_sensing_grb2;
            T_ID3 = self.td3 # spectrum_sensing_grb3;
            T_ID4 = self.td4 # spectrum_sensing_grb4;
            T_ID5 = self.td5 # spectrum_sensing_grb5;
            T_ID6 = self.td6
            T_ID7 = self.td7 # p_ue_rx1. For example: 2350 -->-23.5dBm, 9930 --> -99.3 dBm. 1752 --> -175.2 dBm, . If value = -4.6 or 4.5 dBm. Need another coding style.
            T_ID8 = self.td8 # p_ue_rx2
            T_ID9 = self.td9 # p_ue_rx3
            T_ID10 = self.td10  # p_ue_rx4
            T_ID11 = self.td11 # p_ue_rx5
            T_ID12 = self.td12 # rsrp1
            T_ID13 = self.td13 # rsrp2
            T_ID14 = self.td14 # rsrp3
            T_ID15 = self.td15 # rsrp4
            T_ID16 = self.td16 # rsrp5
            T_ID17 = self.td17
            T_ID18 = self.td18
            T_ID19 = self.td19
            T_ID20 = self.td20
            print ('Getting data from BS_ID = ',BS_ID)
            BS_ID = float(BS_ID)
            print ('Getting data from BS_ID = %f ', BS_ID)
            if (BS_ID == 3618):
                in1 = 1
                print ('Getting data from fisrt BS')
                # updating M5
                # Update to UE 0 in M5
                tem_M5 = T_ID7
                # string to double : float(x)
                # double to string: str(5) --> '5'
                s_tem_M5 = str(tem_M5)
                for i1 in range(3):
                    print ('s_tem_M5',s_tem_M5)
                    tem_s_tem_M5 = s_tem_M5[(1+i1*4):(5+i1*4)]
                    f_tem_s_tem_M5 = float(tem_s_tem_M5)
                    c_f_tem_s_tem_M5 = (-1 / 100) * f_tem_s_tem_M5
                    if c_f_tem_s_tem_M5 >-90: # this is condition threshold to update data at the interference matrix.
                        # for example: if new update is greater than this value, which mean it will update is greater than noise interfance
                        # if new update is less than this value. we set that is a default value to more easier treating in our algorithm.
                        # Moreover, this one is to avoide updating from the same UE in other BS while it is not connecting to this BS.
                        # In this case, that BS is still send a default value to the controller. It is defined as an interference.This is because this BS
                        # did not update from UEs not connecting to this BS.
                        M5[0][i1] = c_f_tem_s_tem_M5

                # Update to UE 1 in M5
                tem_M5 = T_ID8
                # string to double : float(x)
                # double to string: str(5) --> '5'
                s_tem_M5 = str(tem_M5)
                for i1 in range(3):
                    tem_s_tem_M5 = s_tem_M5[(1+i1*4):(5+i1*4)]
                    f_tem_s_tem_M5 = float(tem_s_tem_M5)
                    c_f_tem_s_tem_M5 = (-1 / 100) * f_tem_s_tem_M5
                    if c_f_tem_s_tem_M5 >-90: # this is condition threshold to update data at the interference matrix.
                        # for example: if new update is greater than this value, which mean it will update is greater than noise interfance
                        # if new update is less than this value. we set that is a default value to more easier treating in our algorithm.
                        # Moreover, this one is to avoide updating from the same UE in other BS while it is not connecting to this BS.
                        # In this case, that BS is still send a default value to the controller. It is defined as an interference.This is because this BS
                        # did not update from UEs not connecting to this BS.
                        M5[1][i1] = c_f_tem_s_tem_M5
                # Update to UE 2 in M5
                tem_M5 = T_ID9
                # string to double : float(x)
                # double to string: str(5) --> '5'
                s_tem_M5 = str(tem_M5)
                for i1 in range(3):
                    tem_s_tem_M5 = s_tem_M5[(1+i1*4):(5+i1*4)]
                    f_tem_s_tem_M5 = float(tem_s_tem_M5)
                    c_f_tem_s_tem_M5 = (-1 / 100) * f_tem_s_tem_M5
                    if c_f_tem_s_tem_M5 >-90: # this is condition threshold to update data at the interference matrix.
                        # for example: if new update is greater than this value, which mean it will update is greater than noise interfance
                        # if new update is less than this value. we set that is a default value to more easier treating in our algorithm.
                        # Moreover, this one is to avoide updating from the same UE in other BS while it is not connecting to this BS.
                        # In this case, that BS is still send a default value to the controller. It is defined as an interference.This is because this BS
                        # did not update from UEs not connecting to this BS.
                        M5[2][i1] = c_f_tem_s_tem_M5
                # Update to UE 0 in M5
                tem_M5 = T_ID10
                # string to double : float(x)
                # double to string: str(5) --> '5'
                s_tem_M5 = str(tem_M5)
                for i1 in range(3):
                    tem_s_tem_M5 = s_tem_M5[(1+i1*4):(5+i1*4)]
                    f_tem_s_tem_M5 = float(tem_s_tem_M5)
                    c_f_tem_s_tem_M5 = (-1 / 100) * f_tem_s_tem_M5
                    if c_f_tem_s_tem_M5 >-90: # this is condition threshold to update data at the interference matrix.
                        # for example: if new update is greater than this value, which mean it will update is greater than noise interfance
                        # if new update is less than this value. we set that is a default value to more easier treating in our algorithm.
                        # Moreover, this one is to avoide updating from the same UE in other BS while it is not connecting to this BS.
                        # In this case, that BS is still send a default value to the controller. It is defined as an interference.This is because this BS
                        # did not update from UEs not connecting to this BS.
                        M5[3][i1] = c_f_tem_s_tem_M5
                # Update to UE 0 in M5
                tem_M5 = T_ID11
                # string to double : float(x)
                # double to string: str(5) --> '5'
                s_tem_M5 = str(tem_M5)
                for i1 in range(3):
                    tem_s_tem_M5 = s_tem_M5[(1+i1*4):(5+i1*4)]
                    f_tem_s_tem_M5 = float(tem_s_tem_M5)
                    c_f_tem_s_tem_M5 = (-1 / 100) * f_tem_s_tem_M5
                    if c_f_tem_s_tem_M5 >-90: # this is condition threshold to update data at the interference matrix.
                        # for example: if new update is greater than this value, which mean it will update is greater than noise interfance
                        # if new update is less than this value. we set that is a default value to more easier treating in our algorithm.
                        # Moreover, this one is to avoide updating from the same UE in other BS while it is not connecting to this BS.
                        # In this case, that BS is still send a default value to the controller. It is defined as an interference.This is because this BS
                        # did not update from UEs not connecting to this BS.
                        M5[[4], [i1]] = c_f_tem_s_tem_M5
                index1 = 1
                # index2 = 0
                # index3 = 0
                file_to_save = 'SavedDataM5Index.mat'
                scipy.io.savemat(file_to_save, mdict={'M5': M5, 'index1': index1, 'index2': index2, 'index3': index3}, oned_as = 'row')
    
	        

                # index = data_to_get['index']
                # print ('M5 =', M5)
                # print ('condition =', index[0][0])
                # end of updating M5

                # update spectrum sensing results:
                SS_3618 = np.zeros(shape=(nRB))
                ssr1 = str(T_ID1) # self.td1  # spectrum_sensing_grb1;
                for ss1 in range(1, 6):
                    if ssr1[ss1] == '1':
                        SS_3618[ss1] = 1
                ssr2 = str(T_ID2)  # spectrum_sensing_grb2;
                for ss2 in range(1, 6):
                    if ssr2[ss2] == '1':
                        SS_3618[ss2+5] = 1  # becaues each grb2 will sense 5 RBs
                ssr3 = str(T_ID3) # spectrum_sensing_grb3;
                for ss3 in range(1, 6):
                    if ssr3[ss3] == '1':
                        SS_3618[ss3+10] = 1  # becaues each grb2 will sense 5 RBs
                ssr4 = str(T_ID4)  # spectrum_sensing_grb3;
                for ss4 in range(1, 6):
                    if ssr4[ss4] == '1':
                        SS_3618[ss4 + 15] = 1  # becaues each grb2 will sense 5 RBs
                ssr5 = str(T_ID5)  # spectrum_sensing_grb3;
                for ss5 in range(1, 6):
                    if ssr5[ss5] == '1':
                        SS_3618[ss5 + 20] = 1  # becaues each grb2 will sense 5 RBs
                file_to_save = 'SavedDataSS_3618.mat'
                scipy.io.savemat(file_to_save, mdict={'SS_3618': SS_3618}, oned_as='row')




            elif (BS_ID == 3619):
                in2 = 1
                tem_M5 = T_ID7
                # string to double : float(x)
                # double to string: str(5) --> '5'
                s_tem_M5 = str(tem_M5)
                for i1 in range(3):
                    tem_s_tem_M5 = s_tem_M5[(1+i1*4):(5+i1*4)]
                    f_tem_s_tem_M5 = float(tem_s_tem_M5)
                    
                    c_f_tem_s_tem_M5 = (-1 / 100) * f_tem_s_tem_M5
                    print ('c_tem_s_tem_M5',c_f_tem_s_tem_M5)
                    if c_f_tem_s_tem_M5 >-90: # this is condition threshold to update data at the interference matrix.
                        # for example: if new update is greater than this value, which mean it will update is greater than noise interfance
                        # if new update is less than this value. we set that is a default value to more easier treating in our algorithm.
                        # Moreover, this one is to avoide updating from the same UE in other BS while it is not connecting to this BS.
                        # In this case, that BS is still send a default value to the controller. It is defined as an interference.This is because this BS
                        # did not update from UEs not connecting to this BS.
                        M5[0][i1] = c_f_tem_s_tem_M5
                print ('M5',M5)
                # Update to UE 1 in M5
                tem_M5 = T_ID8
                # string to double : float(x)
                # double to string: str(5) --> '5'
                s_tem_M5 = str(tem_M5)
                for i1 in range(3):
                    tem_s_tem_M5 = s_tem_M5[(1+i1*4):(5+i1*4)]
                    f_tem_s_tem_M5 = float(tem_s_tem_M5)
                    c_f_tem_s_tem_M5 = (-1 / 100) * f_tem_s_tem_M5
                    if c_f_tem_s_tem_M5 >-90: # this is condition threshold to update data at the interference matrix.
                        # for example: if new update is greater than this value, which mean it will update is greater than noise interfance
                        # if new update is less than this value. we set that is a default value to more easier treating in our algorithm.
                        # Moreover, this one is to avoide updating from the same UE in other BS while it is not connecting to this BS.
                        # In this case, that BS is still send a default value to the controller. It is defined as an interference.This is because this BS
                        # did not update from UEs not connecting to this BS.
                        M5[1][i1] = c_f_tem_s_tem_M5
                # Update to UE 2 in M5
                tem_M5 = T_ID9
                # string to double : float(x)
                # double to string: str(5) --> '5'
                s_tem_M5 = str(tem_M5)
                for i1 in range(3):
                    tem_s_tem_M5 = s_tem_M5[(1+i1*4):(5+i1*4)]
                    f_tem_s_tem_M5 = float(tem_s_tem_M5)
                    c_f_tem_s_tem_M5 = (-1 / 100) * f_tem_s_tem_M5
                    if c_f_tem_s_tem_M5 >-90: # this is condition threshold to update data at the interference matrix.
                        # for example: if new update is greater than this value, which mean it will update is greater than noise interfance
                        # if new update is less than this value. we set that is a default value to more easier treating in our algorithm.
                        # Moreover, this one is to avoide updating from the same UE in other BS while it is not connecting to this BS.
                        # In this case, that BS is still send a default value to the controller. It is defined as an interference.This is because this BS
                        # did not update from UEs not connecting to this BS.
                        M5[2][i1] = c_f_tem_s_tem_M5
                # Update to UE 0 in M5
                tem_M5 = T_ID10
                # string to double : float(x)
                # double to string: str(5) --> '5'
                s_tem_M5 = str(tem_M5)
                for i1 in range(3):
                    tem_s_tem_M5 = s_tem_M5[(1+i1*4):(5+i1*4)]
                    f_tem_s_tem_M5 = float(tem_s_tem_M5)
                    c_f_tem_s_tem_M5 = (-1 / 100) * f_tem_s_tem_M5
                    if c_f_tem_s_tem_M5 >-120: # this is condition threshold to update data at the interference matrix.
                        # for example: if new update is greater than this value, which mean it will update is greater than noise interfance
                        # if new update is less than this value. we set that is a default value to more easier treating in our algorithm.
                        # Moreover, this one is to avoide updating from the same UE in other BS while it is not connecting to this BS.
                        # In this case, that BS is still send a default value to the controller. It is defined as an interference.This is because this BS
                        # did not update from UEs not connecting to this BS.
                        M5[3][i1] = c_f_tem_s_tem_M5
                # Update to UE 0 in M5
                tem_M5 = T_ID11
                # string to double : float(x)
                # double to string: str(5) --> '5'
                s_tem_M5 = str(tem_M5)
                for i1 in range(3):
                    tem_s_tem_M5 = s_tem_M5[(1+i1*4):(5+i1*4)]
                    f_tem_s_tem_M5 = float(tem_s_tem_M5)
                    c_f_tem_s_tem_M5 = (-1 / 100) * f_tem_s_tem_M5
                    if c_f_tem_s_tem_M5 >-120: # this is condition threshold to update data at the interference matrix.
                        # for example: if new update is greater than this value, which mean it will update is greater than noise interfance
                        # if new update is less than this value. we set that is a default value to more easier treating in our algorithm.
                        # Moreover, this one is to avoide updating from the same UE in other BS while it is not connecting to this BS.
                        # In this case, that BS is still send a default value to the controller. It is defined as an interference.This is because this BS
                        # did not update from UEs not connecting to this BS.
                        M5[[4], [i1]] = c_f_tem_s_tem_M5
                # save data
                # index1 = 1
                index2 = 1
                # index3 = 0
                file_to_save = 'SavedDataM5Index.mat'
                scipy.io.savemat(file_to_save, mdict={'M5': M5, 'index1': index1, 'index2': index2, 'index3': index3}, oned_as='row')

                # update spectrum sensing results:
                SS_3619 = np.zeros(shape=(nRB))
                ssr1 = str(T_ID1) # self.td1  # spectrum_sensing_grb1;
                for ss1 in range(1, 6):
                    if ssr1[ss1] == '1':
                        SS_3619[ss1] = 1
                ssr2 = str(T_ID2)  # spectrum_sensing_grb2;
                for ss2 in range(1, 6):
                    if ssr2[ss2] == '1':
                        SS_3619[ss2+5] = 1  # becaues each grb2 will sense 5 RBs
                ssr3 = str(T_ID3) # spectrum_sensing_grb3;
                for ss3 in range(1, 6):
                    if ssr3[ss3] == '1':
                        SS_3619[ss3+10] = 1  # becaues each grb2 will sense 5 RBs
                ssr4 = str(T_ID4)  # spectrum_sensing_grb3;
                for ss4 in range(1, 6):
                    if ssr4[ss4] == '1':
                        SS_3619[ss4 + 15] = 1  # becaues each grb2 will sense 5 RBs
                ssr5 = str(T_ID5)  # spectrum_sensing_grb3;
                for ss5 in range(1, 6):
                    if ssr5[ss5] == '1':
                        SS_3619[ss5 + 20] = 1  # becaues each grb2 will sense 5 RBs
                file_to_save = 'SavedDataSS_3619.mat'
                scipy.io.savemat(file_to_save, mdict={'SS_3619': SS_3619}, oned_as='row')

            elif (BS_ID == 3620):
                in3 = 1
                # Update to UE 0 in M5
                tem_M5 = T_ID7
                # string to double : float(x)
                # double to string: str(5) --> '5'
                s_tem_M5 = str(tem_M5)
                for i1 in range(3):
                    tem_s_tem_M5 = s_tem_M5[(1+i1*4):(5+i1*4)]
                    f_tem_s_tem_M5 = float(tem_s_tem_M5)
                    c_f_tem_s_tem_M5 = (-1 / 100) * f_tem_s_tem_M5
                    if c_f_tem_s_tem_M5 >-90: # this is condition threshold to update data at the interference matrix.
                        # for example: if new update is greater than this value, which mean it will update is greater than noise interfance
                        # if new update is less than this value. we set that is a default value to more easier treating in our algorithm.
                        # Moreover, this one is to avoide updating from the same UE in other BS while it is not connecting to this BS.
                        # In this case, that BS is still send a default value to the controller. It is defined as an interference.This is because this BS
                        # did not update from UEs not connecting to this BS.
                        M5[0][i1] = c_f_tem_s_tem_M5
                # Update to UE 1 in M5
                tem_M5 = T_ID8
                # string to double : float(x)
                # double to string: str(5) --> '5'
                s_tem_M5 = str(tem_M5)
                for i1 in range(3):
                    tem_s_tem_M5 = s_tem_M5[(1+i1*4):(5+i1*4)]
                    f_tem_s_tem_M5 = float(tem_s_tem_M5)
                    c_f_tem_s_tem_M5 = (-1 / 100) * f_tem_s_tem_M5
                    if c_f_tem_s_tem_M5 >-90: # this is condition threshold to update data at the interference matrix.
                        # for example: if new update is greater than this value, which mean it will update is greater than noise interfance
                        # if new update is less than this value. we set that is a default value to more easier treating in our algorithm.
                        # Moreover, this one is to avoide updating from the same UE in other BS while it is not connecting to this BS.
                        # In this case, that BS is still send a default value to the controller. It is defined as an interference.This is because this BS
                        # did not update from UEs not connecting to this BS.
                        M5[1][i1] = c_f_tem_s_tem_M5
                # Update to UE 2 in M5
                tem_M5 = T_ID9
                # string to double : float(x)
                # double to string: str(5) --> '5'
                s_tem_M5 = str(tem_M5)
                for i1 in range(3):
                    tem_s_tem_M5 = s_tem_M5[(1+i1*4):(5+i1*4)]
                    f_tem_s_tem_M5 = float(tem_s_tem_M5)
                    c_f_tem_s_tem_M5 = (-1 / 100) * f_tem_s_tem_M5
                    if c_f_tem_s_tem_M5 >-90: # this is condition threshold to update data at the interference matrix.
                        # for example: if new update is greater than this value, which mean it will update is greater than noise interfance
                        # if new update is less than this value. we set that is a default value to more easier treating in our algorithm.
                        # Moreover, this one is to avoide updating from the same UE in other BS while it is not connecting to this BS.
                        # In this case, that BS is still send a default value to the controller. It is defined as an interference.This is because this BS
                        # did not update from UEs not connecting to this BS.
                        M5[2][i1] = c_f_tem_s_tem_M5
                # Update to UE 0 in M5
                tem_M5 = T_ID10
                # string to double : float(x)
                # double to string: str(5) --> '5'
                s_tem_M5 = str(tem_M5)
                for i1 in range(3):
                    tem_s_tem_M5 = s_tem_M5[(1+i1*4):(5+i1*4)]
                    f_tem_s_tem_M5 = float(tem_s_tem_M5)
                    c_f_tem_s_tem_M5 = (-1 / 100) * f_tem_s_tem_M5
                    if c_f_tem_s_tem_M5 >-90: # this is condition threshold to update data at the interference matrix.
                        # for example: if new update is greater than this value, which mean it will update is greater than noise interfance
                        # if new update is less than this value. we set that is a default value to more easier treating in our algorithm.
                        # Moreover, this one is to avoide updating from the same UE in other BS while it is not connecting to this BS.
                        # In this case, that BS is still send a default value to the controller. It is defined as an interference.This is because this BS
                        # did not update from UEs not connecting to this BS.
                        M5[3][i1] = c_f_tem_s_tem_M5
            # Update to UE 0 in M5
                tem_M5 = T_ID11
                # string to double : float(x)
                # double to string: str(5) --> '5'
                s_tem_M5 = str(tem_M5)
                for i1 in range(3):
                    tem_s_tem_M5 = s_tem_M5[(1+i1*4):(5+i1*4)]
                    f_tem_s_tem_M5 = float(tem_s_tem_M5)
                    c_f_tem_s_tem_M5 = (-1 / 100) * f_tem_s_tem_M5
                    if c_f_tem_s_tem_M5 >-90: # this is condition threshold to update data at the interference matrix.
                        # for example: if new update is greater than this value, which mean it will update is greater than noise interfance
                        # if new update is less than this value. we set that is a default value to more easier treating in our algorithm.
                        # Moreover, this one is to avoide updating from the same UE in other BS while it is not connecting to this BS.
                        # In this case, that BS is still send a default value to the controller. It is defined as an interference.This is because this BS
                        # did not update from UEs not connecting to this BS.
                        M5[4][i1] = c_f_tem_s_tem_M5
                # end of updating M5
                # save data
                # index1 = 1
                # index2 = 1
                index3 = 1
                file_to_save = 'SavedDataM5Index.mat'
                scipy.io.savemat(file_to_save, mdict={'M5': M5, 'index1': index1, 'index2': index2, 'index3': index3}, oned_as='row')

                # update spectrum sensing results:
                SS_3620 = np.zeros(shape=(nRB))
                ssr1 = str(T_ID1) # self.td1  # spectrum_sensing_grb1;
                for ss1 in range(1, 6):
                    if ssr1[ss1] == '1':
                        SS_3620[ss1] = 1
                ssr2 = str(T_ID2)  # spectrum_sensing_grb2;
                for ss2 in range(1, 6):
                    if ssr2[ss2] == '1':
                        SS_3620[ss2+5] = 1  # becaues each grb2 will sense 5 RBs
                ssr3 = str(T_ID3) # spectrum_sensing_grb3;
                for ss3 in range(1, 6):
                    if ssr3[ss3] == '1':
                        SS_3620[ss3+10] = 1  # becaues each grb2 will sense 5 RBs
                ssr4 = str(T_ID4)  # spectrum_sensing_grb3;
                for ss4 in range(1, 6):
                    if ssr4[ss4] == '1':
                        SS_3620[ss4 + 15] = 1  # becaues each grb2 will sense 5 RBs
                ssr5 = str(T_ID5)  # spectrum_sensing_grb3;
                for ss5 in range(1, 6):
                    if ssr5[ss5] == '1':
                        SS_3620[ss5 + 20] = 1  # becaues each grb2 will sense 5 RBs
                file_to_save = 'SavedDataSS_3620.mat'
                scipy.io.savemat(file_to_save, mdict={'SS_3620': SS_3620}, oned_as='row')

            updating_finish = 1
            # Save M5 to file
            LOG.info("Updating the BS %f.0 is completed. Moving to consideration before starting Learning Algorithm!", BS_ID)

        # if (in1 + in2 + in3 >= 1):
        #     updating_finish = 1
        #     LOG.info("Mission is completed. Moving to Learning Algorithm")
        # else:
        #     LOG.info("Mission is not completed. Go to first step")

        # updating M7: SINR or RSVP or RSRQ or CQI table

        # M7 = np.array([[2.69953797, -2.31441755, -3.88949969],
        #             [21.14587388, 4.68256814, -21.24283479],
        #             [15.87606144, 7.82879663, -16.50854592],
        #             [2.7085088, -5.69541915, -3.29433778],
        #             [9.30446078, -3.00659401, -9.55233212]]) #SINR_dB

        # print (self.td1)
        # LOG.info("Testing: version %s Data1 %s, Data2 %s , Data3 %s Head %s  Seq number %s", self.td1, self.td2,
        #         self.td3, self.td4, self.td5, self.td6)
        # ==============================================================================
        # RSRP         measurements         are         used in handover, cell         selection and cell         re - selections
        # ===============================================================================
        print ('Getting SINR level')

        P_Rx = M5
        #LOG.info("Testing: P_Rx %s", P_Rx)
        #LOG.info("Testing: MNO.P_Rx %s", MNO.P_Rx) --> OK
        BS_Cmap = M3
        BS_Rmap = M4
        #LOG.info("Testing: BS_Rmap %s", BS_Rmap)
        # for nue in range(5):
        #     for nbs in range(3):
        #         #print ('nue, nbs, = ',nue, nbs)
        #         P_Rx[nue][nbs] = 10**(0.1*P_Rx[nue][nbs]) # converting to W
        P_Rx = 10 ** (0.1 * (P_Rx-30))  # converting to W
        print ('P_Rx=', P_Rx)
        SINR_UE_BS_RB = np.zeros(shape=(nUE, nBS)) # updating SINR
        Intf_UExBS_RB = np.zeros(shape=(nUE, nBS)) # updating SINR
        for k1 in range(nUE):
            for k2 in range(nBS):
                #print ('BS_Rmap[:,[k2]]=', BS_Rmap[:,[k2]], P_Rx[[k1],:])
                Intf_UExBS_RB[[k1],[k2]] = 0#np.dot(P_Rx[[k1],:], BS_Rmap[:,[k2]]) # Wats
                #LOG.info("Testing:Intf_UExBS_RB[[k1],[k2]] %s", Intf_UExBS_RB[[k1],[k2]] )

                SINR_UE_BS_RB[[k1], [k2]] = P_Rx[[k1], [k2]] / (Intf_UExBS_RB[[k1],[k2]]  + 10**(-11)) # Wats

        # LOG.info("Testing: MNO.SINR_UE_BS_RB %s", SINR_UE_BS_RB)
        #print ('SINR_UE_BS_RB_W=', SINR_UE_BS_RB)
        SINR_dB = 10*np.log10(SINR_UE_BS_RB)

        LOG.info("Testing: SINR_dB = %s", SINR_dB)
        M6 = Intf_UExBS_RB
        M7 = SINR_dB
        #print (M7)
        # LA_UA = np.array([112232])

        R_U, LA_UA, LA_DPA, LA_DRBA = scheduling_algoirthm(M1, M2, M3, M4, M5, M6, M7)
        print ('Waiting to learn in next period!')
        time.sleep(20)
        #print ('result', R_U)

        nBS =3
        for bs_id in range(nBS):
            # Send to eNB-1
            message.head.mUA=LA_UA[0]
            message.head.mPA=LA_DPA[0]
            message.head.GRB1 = LA_DRBA[0]
            message.head.GRB2 = LA_DRBA[1]
            message.head.GRB3 = LA_DRBA[2]
            message.head.GRB4 = LA_DRBA[3]
            message.head.GRB5 = LA_DRBA[4]
            size = message.ByteSize()
            #print(message.__str__())
            size_bytes = (socket.htonl(size)).to_bytes(4, byteorder=self.endian)
            send_buff = serialize_message(message)
            buff = size_bytes + send_buff

            if buff is None:
                LOG.error("errno %u occured")
            self.stream.write(buff)
            if bs_id ==0:
                # #added by anselme
                address = ('192.168.100.101', 2210)
                sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                sock.connect(address)
                sock.sendall(buff)
                #self.stream.write(buff)
                print ('message.head.mPA=',message.head.mPA)
                print ('sending to bs ', bs_id)
            if bs_id ==1:
                # #added by anselme
                address = ('192.168.100.102', 2210)
                sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                sock.connect(address)
                sock.sendall(buff)
                #self.stream.write(buff)
                print ('message.head.mPA=', message.head.mPA)
                print ('sending to bs ', bs_id)

            if bs_id ==2:
                # #added by anselme
                address = ('192.168.100.103', 2210)
                sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                sock.connect(address)
                sock.sendall(buff)
                #self.stream.write(buff)
                print ('message.head.mPA=', message.head.mPA)
                print ('sending to bs ', bs_id)


    def _on_read(self, line):
        """ Appends bytes read from socket to a buffer. Once the full packet
        has been read the parser is invoked and the buffers is cleared. The
        parsed packet is then passed to the suitable method or dropped if the
        packet type in unknown. """

        self.__buffer = b''
        if line is not None:
            self.__buffer = self.__buffer + line
            if len(line) == 4:
                temp_size = int.from_bytes(line, byteorder=self.endian)
                size = socket.ntohl(int(temp_size))
                self.stream.read_bytes(size, self._on_read)
                return
            # print ('len(line) = ', len(line)) = 280
            deserialized_msg = deserialize_message(line)
            # Update the sequency number from received message
            self.seq = deserialized_msg.head.seq
            self.t_id=deserialized_msg.head.t_id
            self.b_id = deserialized_msg.head.b_id
            # self.mUA = deserialized_msg.head.mUA
            # self.mPA = deserialized_msg.head.mPA
            # self.GRB1 = deserialized_msg.head.GRB1
            # self.GRB2= deserialized_msg.head.GRB2
            # self.GRB3 = deserialized_msg.head.GRB3
            # self.GRB4 = deserialized_msg.head.GRB4
            # self.GRB5= deserialized_msg.head.GRB5
            self.b_id = deserialized_msg.head.b_id
            self.td1 = deserialized_msg.head.td1
            self.td2 = deserialized_msg.head.td2
            self.td3 = deserialized_msg.head.td3
            self.td4 = deserialized_msg.head.td4
            self.td5 = deserialized_msg.head.td5
            self.td6 = deserialized_msg.head.td6
            self.td7 = deserialized_msg.head.td7
            self.td8 = deserialized_msg.head.td8
            self.td9 = deserialized_msg.head.td9
            self.td10 = deserialized_msg.head.td10
            self.td11 = deserialized_msg.head.td11
            self.td12 = deserialized_msg.head.td12
            self.td13 = deserialized_msg.head.td13
            self.td14 = deserialized_msg.head.td14
            self.td15 = deserialized_msg.head.td15
            self.td16 = deserialized_msg.head.td16
            self.td17 = deserialized_msg.head.td17
            self.td18 = deserialized_msg.head.td18
            self.td19 = deserialized_msg.head.td19
            self.td20 = deserialized_msg.head.td20
            # LOG.info("Testing: version %s Data1 %s, Data2 %s , Data3 %s Head %s  Seq number %s", self.td1,self.td2, self.td3, self.td4, self.td5, self.td6)

            # print(deserialized_msg.__str__()) # display message
            self._trigger_message(deserialized_msg)
            self._wait()
            #return (self.td1, self.td2, self.td3, self.td4, self.td5, self.td6, self.td7, self.td8, self.td9, self.td10, self.td11,
            #self.td12, self.td13, self.td14, self.td15, self.td16, self.td17, self.td18, self.td19, self.td20)

   # deserialized_msg = deserialize_message(line)

   # td1, td2, td3, td4, td5, td6, td7, td8, td9, td10, td11, td12, td13, td14, td15, td16, td17, td18, td19, td20 = _on_read(line);
    #print('td1 = %s', td1)

    #LOG.info("Testing: Data1 %s", td1);

    def _trigger_message(self, deserialized_msg):

        event_type = deserialized_msg.WhichOneof("event_types")

        if event_type == PRT_VBSP_SINGLE_EVENT:
            msg_type = deserialized_msg.se.WhichOneof("events")
        elif event_type == PRT_VBSP_AGENT_SCHEDULED_EVENT:
            msg_type = deserialized_msg.sche.WhichOneof("events")
        elif event_type == PRT_VBSP_TRIGGER_EVENT:
            msg_type = deserialized_msg.te.WhichOneof("events")
        else:
            LOG.error("Unknown message event type %s", event_type)

        if not msg_type or msg_type not in self.server.pt_types:
            LOG.error("Unknown message type %s", msg_type)
            return

        if msg_type != PRT_VBSP_HELLO and not self.vbs:
            return

        handler_name = "_handle_%s" % self.server.pt_types[msg_type]

        if hasattr(self, handler_name):
            handler = getattr(self, handler_name)
            handler(deserialized_msg)

        if msg_type in self.server.pt_types_handlers:
            for handler in self.server.pt_types_handlers[msg_type]:
                handler(deserialized_msg)

    def _handle_hello(self, main_msg):
        """Handle an incoming HELLO message.

        Args:
            main_msg, a emage_msg containing HELLO message
        Returns:
            None
        """
        enb_id = main_msg.head.b_id
        vbs_id = hex_to_ether(enb_id)
        try:
            vbs = RUNTIME.vbses[vbs_id]
        except KeyError:
            LOG.error("Hello from unknown VBS (%s)", (vbs_id))
            return

#        LOG.info("Connection from s% VBS %s OAI %s data %s data1 %s, data2 %s , data3 %s seq number %u", self.addr[0], vbs.addr,  enb_id,  mUA,  mPA, GRB1, GRB2, GRB3,
#                 main_msg.head.seq)
        #LOG.info("Deserialized message from buffer GRB5 s%", GRB5)
        #LOG.info("Deserialized message from buffer td20 s% ", td20)
        # New connection
        if not vbs.connection:

            # set pointer to pnfdev object
            self.vbs = vbs

            # set connection
            vbs.connection = self

            # request registered UEs
            self.send_UEs_id_req()

            # generate register message
            self.send_register_message_to_self()

        # Update VBSP params
        vbs.period = main_msg.se.mHello.repl.period
        vbs.last_seen = main_msg.head.seq
        vbs.last_seen_ts = time.time()
        self.stream_send(main_msg)

    def _handle_UEs_id_repl(self, main_msg):
        """Handle an incoming UEs ID reply.

        Args:
            message, a emage_msg containing UE IDs (RNTIs)
        Returns:
            None
        """

        active_ues = {}
        inactive_ues = {}

        event_type = main_msg.WhichOneof("event_types")
        msg = protobuf_to_dict(main_msg)
        ues_id_msg_repl = msg[event_type]["mUEs_id"]["repl"]

        if ues_id_msg_repl["status"] != configs_pb2.CREQS_SUCCESS:
            return

        # List of active UEs
        if "active_ue_id" in ues_id_msg_repl:
            for ue in ues_id_msg_repl["active_ue_id"]:
                active_ues[(self.vbs.addr, ue["rnti"])] = {}
                if "imsi" in ue:
                    active_ues[(self.vbs.addr, ue["rnti"])]["imsi"] = \
                                                                int(ue["imsi"])
                else:
                    active_ues[(self.vbs.addr, ue["rnti"])]["imsi"] = None
                if "plmn_id" in ue:
                    active_ues[(self.vbs.addr, ue["rnti"])]["plmn_id"] = \
                                                            int(ue["plmn_id"])
                else:
                    active_ues[(self.vbs.addr, ue["rnti"])]["plmn_id"] = None

        # List of inactive UEs
        if "inactive_ue_id" in ues_id_msg_repl:
            for ue in ues_id_msg_repl["inactive_ue_id"]:
                inactive_ues[(self.vbs.addr, ue["rnti"])] = {}
                if "imsi" in ue:
                    inactive_ues[(self.vbs.addr, ue["rnti"])]["imsi"] = \
                                                                int(ue["imsi"])
                else:
                    inactive_ues[(self.vbs.addr, ue["rnti"])]["imsi"] = None
                if "plmn_id" in ue:
                    inactive_ues[(self.vbs.addr, ue["rnti"])]["plmn_id"] = \
                                                            int(ue["plmn_id"])
                else:
                    inactive_ues[(self.vbs.addr, ue["rnti"])]["plmn_id"] = None

        for vbs_id, rnti in active_ues.keys():

            ue_id = (self.vbs.addr, rnti)

            if ue_id not in RUNTIME.ues:
                new_ue = UE(ue_id, ue_id[1], self.vbs)
                RUNTIME.ues[ue_id] = new_ue

            ue = RUNTIME.ues[ue_id]

            imsi = active_ues[ue_id]["imsi"]
            plmn_id = active_ues[ue_id]["plmn_id"]

            # Setting IMSI of UE
            ue.imsi = imsi

            if not ue.plmn_id and plmn_id:

                # Setting tenant
                ue.tenant = RUNTIME.load_tenant_by_plmn_id(plmn_id)

                if ue.tenant:

                    # Adding UE to tenant
                    LOG.info("Adding %s to tenant %s", ue.addr,
                             ue.tenant.plmn_id)
                    ue.tenant.ues[ue.addr] = ue

                    # Raise UE join
                    self.server.send_ue_join_message_to_self(ue)

                    # Create a trigger for reporting RRC measurements config.
                    from empower.ue_confs.ue_rrc_meas_confs import ue_rrc_meas_confs

                    conf_req = {
                        "event_type": "trigger"
                    }

                    ue_rrc_meas_confs(tenant_id=ue.tenant.tenant_id,
                                      vbs=ue.vbs.addr,
                                      ue=ue.rnti,
                                      conf_req=conf_req)

            if ue.plmn_id and not plmn_id:

                # Raise UE leave
                self.server.send_ue_leave_message_to_self(ue)

                # Removing UE from tenant
                LOG.info("Removing %s from tenant %s", ue.addr,
                         ue.tenant.plmn_id)
                del ue.tenant.ues[ue.addr]

                # Resetting tenant
                ue.tenant = None

        existing_ues = []
        existing_ues.extend(RUNTIME.ues.keys())

        for ue_addr in existing_ues:
            if ue_addr not in active_ues:
                RUNTIME.remove_ue(ue_addr)
                self.stream_send(main_msg)

    def _handle_rrc_meas_conf_repl(self, main_msg):
        """Handle an incoming UE's RRC Measurements configuration reply.

        Args:
            message, a message containing RRC Measurements configuration in UE
        Returns:
            None
        """

        event_type = main_msg.WhichOneof("event_types")
        msg = protobuf_to_dict(main_msg)
        rrc_m_conf_repl = msg[event_type]["mUE_rrc_meas_conf"]["repl"]

        rnti = rrc_m_conf_repl["rnti"]

        ue_id = (self.vbs.addr, rnti)

        if ue_id not in RUNTIME.ues:
            return

        ue = RUNTIME.ues[ue_id]

        if rrc_m_conf_repl["status"] != configs_pb2.CREQS_SUCCESS:
            return

        del rrc_m_conf_repl["rnti"]
        del rrc_m_conf_repl["status"]

        if "ue_rrc_state" in rrc_m_conf_repl:
            ue.rrc_state = rrc_m_conf_repl["ue_rrc_state"]
            del rrc_m_conf_repl["ue_rrc_state"]

        if "capabilities" in rrc_m_conf_repl:
            ue.capabilities = rrc_m_conf_repl["capabilities"]
            del rrc_m_conf_repl["capabilities"]

        ue.rrc_meas_config = rrc_m_conf_repl
        self.stream_send(ue.rrc_meas_config )

    def send_UEs_id_req(self):
        """ Send request for UEs ID registered in VBS """

        ues_id_req = main_pb2.emage_msg()
        enb_id = ether_to_hex(self.vbs.addr)
        # Transaction identifier is one by default.
        #create_header(1, enb_id, ues_id_req.head)

        # added by anselme

        td1=1.0
        td2=1.0
        td3=1.0
        td4=1.0
        td5=1.0
        td6=1.0
        td7=1.0
        td8=1.0
        td9=1.0
        td10=1.0
        td11=1.0
        td12=1.0
        td13=1.0
        td14=1.0
        td15=1.0
        td16=1.0
        td17=1.0
        td18=1.0
        td19=1.0
        td20=1.0
        mUA=1.0
        mPA=2.0
        GRB1=0.2
        GRB2=0.2
        GRB3=0.5
        GRB4=52.52
        GRB5=5.1



        create_header(1, enb_id, ues_id_req.head,mUA, mPA, GRB1, GRB2, GRB3, GRB4, GRB5,td1, td2, td3, td4, td5, td6,
                      td7, td8, td9, td10, td11, td12, td13, td14, td15, td16, td17, td18, td19, td20) #modified by Anselme

        # Creating a trigger message to fetch UE RNTIs
        trigger_msg = ues_id_req.te
        trigger_msg.action = main_pb2.EA_ADD

        UEs_id_msg = trigger_msg.mUEs_id
        UEs_id_req_msg = UEs_id_msg.req

        UEs_id_req_msg.dummy = 1

        LOG.info("Sending UEs request to VBS %s (%u)",
                 self.vbs.addr, enb_id)

        self.stream_send(ues_id_req)

    def send_rrc_meas_conf_req(self, ue):
        """ Sends a request for RRC measurements configuration of UE """

        rrc_m_conf_req = main_pb2.emage_msg()
        enb_id = ether_to_hex(self.vbs.addr)

        # added by anselme

        td1=1.0
        td2=1.0
        td3=1.0
        td4=1.0
        td5=1.0
        td6=1.0
        td7=1.0
        td8=1.0
        td9=1.0
        td10=1.0
        td11=1.0
        td12=1.0
        td13=1.0
        td14=1.0
        td15=1.0
        td16=1.0
        td17=1.0
        td18=1.0
        td19=1.0
        td20=1.0
        mUA = 1.0
        mPA = 2.0
        GRB1 = 0.2
        GRB2 = 0.2
        GRB3 = 0.5
        GRB4 = 52.52
        GRB5 = 5.1

        # Transaction identifier is one by default.
        #create_header(1, enb_id, rrc_m_conf_req.head)
        #  create_header(1, enb_id, rrc_m_conf_req.head, 1, power)
        create_header(1, enb_id, rrc_m_conf_req.head, mUA, mPA, GRB1, GRB2, GRB3, GRB4, GRB5,td1, td2, td3, td4, td5,
                      td6, td7, td8, td9, td10, td11, td12, td13, td14, td15, td16, td17, td18, td19, td20)
        # modified by Anselme

        # Creating a trigger message to fetch UE RNTIs
        trigger_msg = rrc_m_conf_req.te
        trigger_msg.action = main_pb2.EA_ADD

        rrc_m_conf_msg = trigger_msg.mUE_rrc_meas_conf
        rrc_m_conf_req_msg = rrc_m_conf_msg.req

        rrc_m_conf_req_msg.rnti = ue.rnti

        LOG.info("Sending UEs RRC measurement config request to VBS %s (%u)",
                 self.vbs.addr, enb_id)

        self.stream_send(rrc_m_conf_req)

    def _wait(self):
        """ Wait for incoming packets on signalling channel """
        self.stream.read_bytes(4, self._on_read)
    #Aadded by anselme

    def _on_disconnect(self):
        """Handle VBSP disconnection."""

        if not self.vbs:
            return

        LOG.info("VBS disconnected: %s", self.vbs.addr)

        # remove hosted ues
        for addr in list(RUNTIME.ues.keys()):
            ue = RUNTIME.ues[addr]
            if ue.vbs == self.vbs:
                RUNTIME.remove_ue(ue.addr)

        # reset state
        self.vbs.last_seen = 0
        self.vbs.connection = None
        self.vbs.ues = {}
        self.vbs.period = 0
        self.vbs = None

    def send_bye_message_to_self(self):
       """Send a unsollicited BYE message to self."""

       for handler in self.server.pt_types_handlers[PRT_VBSP_BYE]:
            handler(self.vbs)
    def send_register_message_to_self(self):
       """Send a REGISTER message to self."""
       for handler in self.server.pt_types_handlers[PRT_VBSP_REGISTER]:
            handler(self.vbs)
