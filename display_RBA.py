#!/usr/bin/python2.7
#
# Copyright (c) 2016 Roberto Riggio
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
from __future__ import division
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import time
import scipy.io
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.ticker as ticker
from matplotlib import colors as mcolors

def DisplaymRBA_RB_BS(mRBA_BS, nBS,nRB):
    #    plt.figure(2)
    fig, ax1 = plt.subplots()
    ax = plt.gca()
    ax.cla()
    for i in range(nRB):
        for j in range(nBS):
            if mRBA_BS[[j], [i]] == 1:
                plt.plot(j, i, 'rs', ms=10)
            else:
                plt.plot(j, i, 'gs', ms=10)
    plt.xlabel('RB index')
    plt.ylabel('BS index')
    plt.title('RB allocation to BSs')
    ax1.xaxis.set_ticks(np.arange(0, nBS, 1))
    ax1.xaxis.set_major_formatter(ticker.FormatStrFormatter('%1i'))
    ax1.yaxis.set_ticks(np.arange(0, nRB, 1))
    ax1.yaxis.set_major_formatter(ticker.FormatStrFormatter('%1i'))
    plt.grid(True)    
    return 1
file_to_save = '/home/epc/empower-runtime/SavedRBA.mat'
data_to_get = scipy.io.loadmat(file_to_save)
mRBA_BS = data_to_get['M1']
print (mRBA_BS)
DisplaymRBA_RB_BS(mRBA_BS,5,25)
plt.show()

