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


fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)
def animate(i):
    file_to_save = '/home/epc/empower-runtime/SavedHistUtility.mat'
    data_to_get = scipy.io.loadmat(file_to_save)
    su = data_to_get['M1']
    xar = np.array(range(0,1000))
    yar = su[0][:]
    ax1.clear()
    ax1.plot(xar,yar)
    plt.xlabel('History')
    plt.ylabel('Network Utility')
    plt.title('Utility = sum_rate(bit/s)*reward-n_RB*cost(power/re))')
ani = animation.FuncAnimation(fig, animate, interval=10000)
plt.show()



