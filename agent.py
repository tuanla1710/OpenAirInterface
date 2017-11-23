#!/usr/bin/python
# -*- coding: utf-8 -*-

# The aim of this script is to collect some traces from oai stack and generate a sequence diagram image (png or jpeg).
#
# It is supposed that a protocol name (MSC_NEW_STR) starts with...its name (RRC, MAC, NAS, S1AP, etc) then is followed by an underscore and whatever (RRC_UE,  RRC_eNB)
#   Like this it is possible to distinguish between PDUS, SDUs or other messages only by reading source ans destination

# # TCP Client Code
import time
import pickle
from socket import *  # Imports socket module
import numpy as np

i = 0
cell = 2

while i == 0:
    s = socket(AF_INET, SOCK_STREAM)  # Creates a socket
    
    #s.allow_reuse_address = True
    s.bind(('0.0.0.0', 0))

    
    
#    with open('/home/ue2/empower-ue-agent/agent/ua_info.dat') as fn:
#        bs_id_check = fn.readlines()
	# print 'test'
    # print 'bs_id_check=', bs_id_check
    # print 'file opened'
#    if not bs_id_check:
#	bs_id = 4        
#    else:      
#	bs_id = bs_id_check[0][2]  # 1 is the index of the UE . f[1] return which base station is being connected
#        bs_id = int(bs_id)     
    # cell = 2
    if cell == 1:
        host = "192.168.100.101"  # Set the server address to variable host
        port = 4446  # Sets the variable port to 4446
    elif cell == 2:
        host = "192.168.100.102"  # Set the server address to variable host
        port = 4446  # Sets the variable port to 4446
    elif cell == 3:
        host = "192.168.100.103"  # Set the server address to variable host
        port = 4446  # Sets the variable port to 4446
    elif cell == 4:
        host = "192.168.100.103"  # Set the server address to variable host
        port = 4446  # Sets the variable port to 4446

    print 'connecting to eNB controller', cell
    s.connect((host, port))  # Connect to server addressim

    print('receiving data...')

    msg = s.recv(1024)  # Receives data up to 1024 bytes and stores in variables msg
    f = open('/home/ue2/empower-ue-agent/agent/ua_info.dat', 'wb')
    # print 'file opened', msg
    f.write(msg)
    f.close()

    # Write to the SDN.data
    control = 1
    cell = msg[1]
    cell = int(cell)
    if cell == 1:
    	cell_id = 8
        bs_id = 3618 
    if cell == 2:
    	cell_id = 10
	bs_id = 3619
    if cell == 3:
    	cell_id = 12
	bs_id = 3620
    with open('/home/ue2/openairinterface5g/cmake_targets/lte_build_oai/build/SDN.txt','wb') as out:
	line1 = control
	line2 = cell_id
        print ("--> Sending UA_info to user association module. \n")
	out.write('{}\n{}\n'.format(line1,line2))
	# print ("Mission is completed! Bye!")
    out.close()

    with open('/home/ue2/openairinterface5g/cmake_targets/lte_build_oai/build/SDN.dat','wb') as outdat:
	line1 = control
	line2 = cell_id
        # print ("I'm going to write these to the file. You have to execute my comments.")
	outdat.write('{}\n{}\n'.format(line1,line2))
	# print ("Mission is completed! Bye!")
    outdat.close()
	
    # print("--> Sending UE_info.txt information to the eNB \n")
    # cut the first line in the text 
 
    with open('/home/ue2/openairinterface5g/data.txt', 'r') as fin: # open file 
	data = fin.read().splitlines(True)  # get data 
    with open('/home/ue2/empower-ue-agent/agent/ue2_info.dat', 'w') as fout: # open file 
	    fout.writelines(data[1:])    # cut first line 
    
    filename = "/home/ue2/empower-ue-agent/agent/ue2_info.dat"     # read data from file 
    with open(filename) as fn1:  
        ue2_info_data = fn1.read() # get data 

    print(ue2_info_data)
    s.send(ue2_info_data)
    fn1.close()
    print '\nUE information from SDN controller to execute: \n'
    print 'Flag_from_SDN_controller = ',control, '\n'
    print 'UA_info to connect: BS_id = ',bs_id, 'Cell_id = ', cell_id
    time.sleep(60)        
    print 'Running...'

