#!/usr/bin/env python
from __future__ import division
import matplotlib.pyplot as plt
import numpy as np 
import matplotlib.ticker as ticker
from matplotlib import colors as mcolors
#===============================================================================
# colors = dict(mcolors.BASE_COLORS, **mcolors.CSS4_COLORS)

# from blaze.expr.expressions import shape
# #===============================================================================
# def DisplayNetwork(Cor_BS , Cor_UE, OP_Asso, OP2_Rate, OP2_User):
#     '''
#     % DisplayNetwork plot the Network.
#     %
#     % Inputs:   Cor_UE  = X and Y coordinates of UE
#     %           Cor_BS  = X and Y coordinates of BS
#     %
#     % Author: LE ANH TUAN
#     % 2014, March, 26.
#     % =========================================================================
#
#     % load Cor_MBS; load Cor_PBS; load Cor_FBS;
#     % Cor_UE = 200*rand(200,2);
#     % [ Buildings, Streets ] = CreateSubRegion( );
#     % nBuilding = length(Buildings);
#     % for i = 1:nBuilding
#     %     rectangle('Position',Buildings(i,:),...
#     %         'LineWidth',2,'LineStyle','-',...
#     %         'EdgeColor','r','FaceColor','c')
#     % end
#     '''
# #===============================================================================
# #     plt.axis([0,50,60,80])
# #     for i in np.arange(1,5):
# #         z = 68 + 4 * np.random.randn(50)
# #         zm = np.cumsum(z) / range(1,len(z)+1)
# #         plt.plot(zm)
# #
# #         n = np.arange(1,51)
# #         su = 68 + 4 / np.sqrt(n)
# #         sl = 68 - 4 / np.sqrt(n)
# #
# #         plt.plot(n,su,n,sl)
# #
# #     plt.show()
# #===============================================================================
#     ax = plt.gca()
#     ax.cla()
#     for bs in range(4):
#         if bs ==0:
#             x = Cor_BS[[bs],[0]]
#             x = x[0]
#             y = Cor_BS[[bs],[1]]
#             y = y[0]
#             circle = plt.Circle((x, y), 1500, color='r',fill=False)
#         #=======================================================================
#         # elif bs ==1:
#         #     x = Cor_BS[[bs],[0]]
#         #     x = x[0]
#         #     y = Cor_BS[[bs],[1]]
#         #     y = y[0]
#         #     circle1 = plt.Circle((x, y), 150, color='b',fill=False)
#         # elif bs ==2:
#         #     x = Cor_BS[[bs],[0]]
#         #     x = x[0]
#         #     y = Cor_BS[[bs],[1]]
#         #     y = y[0]
#         #     circle2 = plt.Circle((x, y), 150, color='g',fill=False)
#         # elif bs ==3:
#         #     x = Cor_BS[[bs],[0]]
#         #     x = x[0]
#         #     y = Cor_BS[[bs],[1]]
#         #     y = y[0]
#         #     circle3 = plt.Circle((x, y), 150, color='g',fill=False)
#         #=======================================================================
#
#     ax.add_artist(circle)
#     #===========================================================================
#     # ax.add_artist(circle1)
#     # ax.add_artist(circle2)
#     # ax.add_artist(circle3)
#     #===========================================================================
#
#     #fig.savefig('plotcircles2.png')
#
#
#     nUE = 5
#
#
#     z = np.array([100,100,100])
#     plt.figure(1)
#     plt.axis([600,900,600,900])
#     for i in range(len(z)):
#         x = Cor_BS[[i],[0]]
#         x = x[0]
#         y = Cor_BS[[i],[1]]
#         y = y[0]
#         plt.plot(x, y, 'r^')
#         s = 'BS-'+str(i)
#         plt.text(x-10, y-20, s )
#
#     for i in range(nUE):
#         x = Cor_UE[[i],[0]]
#         x = x[0]
#         y = Cor_UE[[i],[1]]
#         y = y[0]
#         plt.plot(x, y, 'bs')
#         s = 'UE-'+str(i)
#         plt.text(x-10, y-20, s )
#
#
#
#
#     plt.xlabel('X (m)')
#     plt.ylabel('Y (m)')
#     plt.title('Test-bed model')
#     plt.grid()
#     plt.show()
#     return 0
#     #===============================================================================
#     # Cor_BS = np.array([[0.,0.],[750.,750.],[ 900.,  750.],[ 850.,  850.]])
#     # #Cor_BS = np.array([[0.,0.],[400.,600.],[ 900.,  750.],[ 850.,  850.]])
#     #
#     # Cor_UE= np.array([[ 800, 650],[ 930 , 860], [ 810.41151527,  823.56156804], [ 758.54915236 , 864.55550331], [ 839.13526345  , 755.4124108 ]])
#     #
#     # OP_Asso = np.array([[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1],[[0,0,0,1]]]) # nUExnBS)
#     #
#     # DisplayNetwork(Cor_BS , Cor_UE, OP_Asso)
#     #===============================================================================
# #===============================================================================
# # def DisplaymRBA_RB_BS(mRBA_BS,nRB,nBS):
# #     plt.figure(2)
# #     ax = plt.gca()
# #     ax.cla()
# #     plt.axis([-1,nBS,-1,nRB])
# #     for i in range(nRB):
# #         for j in range(nBS):
# #             if mRBA_BS[[i],[j]] ==1:
# #                 plt.plot(j, i, 'bs')
# #             else:
# #                 plt.plot(j, i, 'ys')
# #     plt.ylabel('RBs index')
# #     plt.xlabel('BSs index')
# #     plt.title('RBs allocation to BSs')
# #     plt.grid()
# #     plt.show()
# #     return 0
# #===============================================================================
        
def DisplaymRBA_RB_BS(mRBA_BS,nRB,nBS):  
    
    plt.figure(2)
    fig, ax1 = plt.subplots()
    ax = plt.gca()
    ax.cla()    
    for i in range(nBS):
        for j in range(nRB):
            if mRBA_BS[[j],[i]] ==1:
                plt.plot(j, i, 'rs',ms=10)
            else: 
                plt.plot(j, i, 'gs',ms=10)             
    plt.xlabel('RB index')
    plt.ylabel('BS index')
    plt.title('RB allocation to BSs')        
    ax1.xaxis.set_ticks(np.arange(0, nRB, 1))
    ax1.xaxis.set_major_formatter(ticker.FormatStrFormatter('%1i'))
    ax1.yaxis.set_ticks(np.arange(0, nBS, 1))
    ax1.yaxis.set_major_formatter(ticker.FormatStrFormatter('%1i'))
    plt.grid(True)   
    plt.axis([-0.5,nRB,-0.5,nBS])
    plt.show()  
    return 0

    
def DisplaymUE1Utility(Utility):  
    plt.figure(3)
    ax = plt.gca()
    ax.cla()
    #plt.axis([0,nUE,0,nRB])
    L = range(len(Utility))    
    plt.plot(L,Utility)             
    plt.xlabel('History')
    plt.ylabel('Utility')
    plt.title('UE utility')    
    plt.show()
    return 0
    

#===============================================================================
# def DisplaymRBA_BS_UE(mRBA_BS_UE,nRB,nBS,nUE):        
#    
#     df_cm = pd.DataFrame(mRBA_BS_UE, range(nRB),range(nBS))
#     plt.figure(figsize = (10,7))
#     sn.set(font_scale=1.4)#for label size
#     sn.heatmap(df_cm, annot=True,annot_kws={"size": 16})# font size    
#     plt.show()
#===============================================================================
