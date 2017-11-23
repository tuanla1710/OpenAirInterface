from __future__ import division
"""
This module contains objective classes
@author: Dr. LE ANH TUAN
"""
from empower.vbsp.project_modules import *
#===============================================================================
clear_all.clear_all()

class Controller_Name:     
    nBS = 0;  # Number of BSs
    nMBS = 0; # Number of MBSs     
    nPBS = 0; # Number of PBSs    
    nFBS = 0; # Number of GBSs    
    
    nRB = 0;  # Number of resource blocks    
    
    nUE = 0;  # Number of UEs    
        
    mUA = []; # User association matrix 
    mFUA = []; # User association matrix
    mRBA = [];# Resource blocks allocation matrix    

    rMBS = 0; # Radius of MBS 
    rPBS = 0; # Radius of PBS     
    rFBS = 0; # Radius of FBS 
    
    pBS  = [];# Transmit power of all BSs
    pMBS = 0; # Radius of MBS 
    pPBS = 0; # Radius of PBS     
    pFBS = 0; # Radius of FBS 
    
    cBS = []; # Coor of MBS
    cMBS =[];# Coor of MBS 
    cPBS =[];# Coor of PBS     
    cFBS =[];# Coor of FBS
    
    cUE = []; # Coor of FBS

    RefPL = [];# nBSx1
    
    BS_Dist = []; # nBS x nBS: distance among BSs
    
    FFT_size = 0; 
    
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

