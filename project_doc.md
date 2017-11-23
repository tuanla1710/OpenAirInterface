# demo-open-mobile-network-platform-project

SDN-based Control and Management Architecture for Heterogeneous Cognitive Networks
(Testbed)
	SDN controller architecture and system model
Performance evaluation
Test-bed evaluation (version 3.1-20170417)
This section provides experimentation plan details of our proposals to the SDN-based Control and Management Architecture for Heterogeneous Cognitive Networks. In following of the testbed purpose and approach in Sections 3.1 and 3.2, the background is presented in Section 3.3. Next, tested setup, system model and configuration are outlined in Section 3.4, measures of performance and effectiveness are also listed in Section 3.5, demonstration and test experiments are detailed in Section 3.6. 
Purpose 
The goal is to evaluate the proposed algorithm using the open platform for the problem of “joint user association and resource allocation to maximize total utility function in term of throughput and energy consumption in the cognitive radio network” as mentioned in Section 2.  Specifically, the objective of the test-bed effort is to deploy and test a mobile communication network that employ the cognitive radio technology combined with the SDN-based management. 
Approach
Our testbed is associated with a LTE network model based on the OpenAirInterface Software Alliance (OSA) [1] that provides truly open-source solutions for prototyping 5th Generation Mobile Networks and devices. Particularly, the testbed effort is to deploy and test with a COST-based communication model. In this model, the USRP-B210-based OAI eNB (and OAI EPC) is connected with commercial off-the-shelf (COTS) UE such as smartphones and LTE dongles.  
Experiments are to be performed to measure and report on the performance and effectiveness of the test-bed communications capabilities. The test-bed project is being executed in phases. The objectives and dates associated with each phase are outlined in Figure 3.1.
 
Figure 3.1:  Project Phases
Background 
In this section, we first present an introduction to USRP-B210. Then, we present an overview about the OpenAirInterface Software Alliance (OSA) [1]. Finally, we present the background functions of the main LTE packet core elements-MME, SGW, PGS, as follows:  
USRP B210
 
                                                             Figure  3.2  USRP B210
The USRP B210 provides a fully integrated, single-board, Universal Software Radio Peripheral (USRP) plateform with continuous frequency conversate from 70 MHz – 6 GHz.
Features :  
	First fully integrated, two-channel USRP device with continuous RF converage from 70 MHz –  6GHz
	Full duplex, MIMO (2 Tx & 2Rx) operation with up to 56MHz of real-time bandwidth (61.44MS/s squdrature)
	Fast and convenient superspeed USB 3.0 connectivity
	 GNURadio and OpenBTS support through the open-source USRP Hardware Driver(UHD)
	Open and reconfigurable spartan 6 XC6SLX150 FPGA ( for advanced users)
Early access   prototyping plateform for the Analog Devices AD9361 RFIC, a fully integrated direct conversion with mixed signal baseband.
OSA introduction: 
The OpenAirInterface (OAI) Software Alliance (OSA) is a separate legal entity from EURECOM, which aims to provide an open-source ecosystem for the core (EPC) and access-network (EUTRAN) protocols of 3GPP cellular systems with the possibility of interoperating with closed-source equipment in either portion of the network. More importantly it will ensure a much-needed communication mechanism between the two in order to bring academia closer to complex real-world systems which are controlled by major industrial players in the wireless industry. 
The OSA's EPC software is known and openairCN while the access-network software goes under the name of openair5G. openair5G is freely distributed by the OSA under the terms stipulated by a new open-source license catering to the intellectual property agreements used in 3GPP which allows contributions from 3GPP members holding patents on key procedures used in the standard. openairCN is distributed under an Apache V2.0 license, in order to ease with integration within an OpenStack environment. The software can be used in conjunction with standard RF laboratory equipment available in many labs (i.e. National Instruments/Ettus USRP and PXIe platforms), in addition to custom RF hardware provided by EURECOM, to implement these functions to a sufficient degree to allow for real-time interoperation with commercial devices.  The OSA can offer: 
	Providing a standard-compliant implementation of a subset of Release 10 LTE for UE, eNB, MME, HSS, SGw and PGw on standard Linux-based computing equipment (Intel x86 PC/ARM architectures).   
	Supporting modules for the development of Software Defined Networking (SDN) concepts to open the proprietary interfaces to control the RAN hardware/software. 
	The software is freely distributed by the Alliance under the terms stipulated by the OSA license model. It can be used in conjunction with standard RF laboratory equipment available in addition to custom RF hardware provided by EURECOM to implement these functions to a sufficient degree to allow for real-time interoperation with commercial devices. 

Functions of the main LTE packet core elements-MME, SGW, PGS

 MME functions include: 
	NAS signaling;
	NAS signaling security;
	Inter CN node signaling for mobility between 3GPP access networks (terminating S3);
	UE Reach ability in ECM-IDLE state (including control and execution of paging retransmission);
	Tracking Area list management;
	Mapping from UE location (e.g. TAI) to time zone, and signaling a UE time zone change associated with mobility;
	PDN GW and Serving GW selection;
	MME selection for handovers with MME change;
	SGSN selection for handovers to 2G or 3G 3GPP access networks;
	Roaming (S6a towards home HSS);
	Authentication;
	Authorization;
	Bearer management functions including dedicated bearer establishment;
	Lawful Interception of signaling traffic;
	Warning message transfer function (including selection of appropriate Cognitive BS or eNodeB);
	UE Reach ability procedures.
SGW functions: 
	The local Mobility Anchor point for inter-eNodeB handover;
	Sending of one or more "end marker" to the source eNodeB, source SGSN or source RNC immediately after switching the path during inter-eNodeB and inter-RAT handover, especially to assist the reordering function in eNodeB.
	Mobility anchoring for inter-3GPP mobility (terminating S4 and relaying the traffic between 2G/3G system and PDN GW);
	ECM-IDLE mode downlink packet buffering and initiation of network triggered service request procedure;
	Lawful Interception;
	Packet routing and forwarding;
	Transport level packet marking in the uplink and the downlink, e.g. setting the DiffServ Code Point, based on the QCI of the associated EPS bearer;
	Accounting for inter-operator charging. For GTP-based S5/S8, the Serving GW generates accounting data per UE and bearer;
	Interfacing OFCS according to charging principles and through reference points specified in TS 32.240

 PDN gateway function (PGW): 
	Per-user based packet filtering (by e.g. deep packet inspection);
	Lawful Interception;
	UE IP address allocation;
	Transport level packet marking in the uplink and downlink, e.g. setting the DiffServ Code Point, based on the QCI of the associated EPS bearer;
	Accounting for inter-operator charging;
	UL a
	nd DL service level charging as defined in TS 23.203 (e.g. based on SDFs defined by the PCRF, or based on deep packet inspection defined by local policy);
	Interfacing OFCS through according to charging principles and through reference points specified in TS 32.240.
	UL and DL service level gating control as defined in TS 23.203;
	UL and DL service level rate enforcement as defined in TS 23.203 [2] (e.g. by rate policing/shaping per SDF);
	UL and DL rate enforcement based on APN-AMBR (e.g. by rate policing/shaping per aggregate of traffic of all SDFs of the same APN that are associated with Non-GBR QCIs);
	DL rate enforcement based on the accumulated MBRs of the aggregate of SDFs with the same GBR QCI (e.g. by rate policing/shaping);
	DHCPv4 (server and client) and DHCPv6 (client and server) functions;
	The network does not support PPP bearer type in this version of the specification. Pre-Release 8 PPP functionality of a GGSN may be implemented in the PDN GW;
	Packet screening.

UE Identifiers in LTE
    IMSI - International Mobile Subscriber Identity:
	The IMSI is a permanent identity assigned by the Service Provider
	It is valid as long as the Service is Active with the Service Provider
	It is stored on the USIM card and on the HSS (Home Subscriber Server)
	It globally and uniquely identifies a user on any 3GPP PLMN (Public Land Mobile Network)
    IMEI - International Mobile Equipment Identity:
	The IMEI is a permanent identity assigned by the Device Manufacturer
	Valid as long as the Device is in Use
	Stored on the Device hardware and on the HSS (Home Subscriber Server)
    C-RNTI - Cell Radio Network Temporary Identity:
	Dynamic Identity assigned by the eNodeB
	Valid as long as the UE is Connected to the eNodeB that assigned the C-RNTI
	Stored in the UE and the eNodeB
    GUTI - Globally Unique Temporary Identity:
	Dynamic Identity assigned by the MME (Mobility Management Entity)
	Valid as long as the UE is Registered with the EPC (Evolved Packet Core) and Attached to the MME that assigned the GUTI
	Stored on the UE and the MME
    IP Address:
	Dynamic Identity assigned by the PGW
	Valid as long as the UE is Registered with the EPC (Evolved Packet Core)
	Stored in the UE and the PGW and any other node "north" of the PGW
C-RNTI (Cell RNTI):
	C-RNTI is a unique identification used for identifying RRC Connection and scheduling which is dedicated to a particular UE.
	The eNB assigns different C-RNTI values to different UEs. When Carrier Aggregation is configured, same C-RNTI applies to all serving cells.
	The eNB uses C-RNTI to allocate a UE with uplink grants, downlink assignments, PDCCH orders etc.
	The eNB also uses C-RNTI to differentiate uplink transmissions (e.g. PUSCH, PUCCH) of a UE from others.
	C-RNTI is of 16-bit in length and its value can range from 1 to 65523 (0x0001 to 0xFFF3).
	After connection establishment or re-establishment the Temporary C-RNTI (as explained above) is promoted to C-RNTI.
	 During Handovers within E-UTRA or from other RAT to E-UTRA, C-RNTI is explicitly provided by the eNB in MobilityControlInfo container with IE newUE-Identity
Non Access Stratum (NAS) protocols [3]

The Non-Access Stratum (NAS) protocols form the highest stratum of the control plane between the user equipment (UE) and MME.  NAS protocols support the mobility of the UE and the session management procedures to establish and maintain IP connectivity between the UE and a PDN GW. They define the rules for a mapping between parameters during inter-system mobility with 3G networks or non-3GPP access networks. They also provide the NAS security by integrity protection and ciphering of NAS signaling messages. EPS provides the subscriber with a "ready-to-use" IP connectivity and an "always-on" experience by linking between mobility management and session management procedures during the UE attach procedure.
Complete NAS transactions consist of specific sequences of elementary procedures with EPS Mobility Management (EMM) and EPS Session Management (ESM) protocols.
The Non-Access Stratum is a set of protocols in the Evolved Packet System. The NAS is used to convey non-radio signalling between the User Equipment (UE) and the Mobility Management Entity (MME) for an LTE/E-UTRAN access.
The NAS procedures are grouped in two categories:
	The EPS Mobility Management (EMM), and
	The EPS Session Management (ESM).
Radio Resource Control
	The Radio Resource Control (RRC) protocol is used in UMTS and LTE on the Air interface. It is layer that exists between UE and eNB and exists at the IP level. This protocol is specified by 3GPP in TS 25.331 for UMTS and in TS 36.331 for LTE. RRC messages are transported via the PDCP-Protocol.
	The major functions of the RRC protocol include connection establishment and release functions, broadcast of system information, radio bearer establishment, reconfiguration and release, RRC connection mobility procedures, paging notification and release and outer loop power control. By means of the signaling functions the RRC configures the user and control planes according to the network status and allows for Radio Resource Management strategies to be implemented. 
	The operation of the RRC is guided by a state machine which defines certain specific states that a UE may be present in. The different states in this state machine have different amounts of radio resources associated with them and these are the resources that the UE may use when it is present in a given specific state.  Since different amounts of resources are available at different states the quality of the service that the user experiences and the energy consumption of the UE are influenced by this state machine. [3]
User association and mobility management protocols in LTE
Association messaging

 
Attach procedure and combined attach procedure
 

UE initiated detach procedure
 
RRC Connection Establishment, network accepts RRC connection
 
RRC Connection Establishment, network rejects RRC connection
 
RRC Connection Release procedure on the DCCH

 
RRC Connection Release procedure on the CCCH

 
Sample runs of initial cell selection in UE and timing of related events

 
Parameters measurement in LTE for the UE side:

In LTE network, a UE measures:
	RSSI – Received Signal Strength Indicator: The carrier RSSI (Receive Strength Signal Indicator) measures the average total received power observed only in OFDM symbols containing reference symbols for antenna port 0 (i.e., OFDM symbol 0 & 4 in a slot) in the measurement bandwidth over N resource blocks.

The total received power of the carrier RSSI includes the power from co-channel serving & non-serving cells, adjacent channel interference, thermal noise, etc. Total measured over 12-subcarriers including RS from Serving Cell, Traffic in the Serving Cell

	RSRP – Reference Signal Received Power: RSRP is a RSSI type of measurement, as follows there are some definition of it and some details as well.

It is the power of the LTE Reference Signals spread over the full bandwidth (RSSI) and narrow-band (RSRP). A minimum of -20 dB SINR (of the S-Synch channel) is needed to detect RSRP/RSRQ

	RSRQ – Reference Signal Received Quality: Quality considering also RSSI and the number of used Resource Blocks (N) RSRQ = (N * RSRP) / RSSI measured over the same bandwidth. 

RSRQ is a C/I type of measurement and it indicates the quality of the received reference signal. The RSRQ measurement provides additional information when RSRP is not sufficient to make a reliable handover or cell re-selection decision. 

Note: The reference point for the RSRP shall be the antenna connector of the UE.

In the procedure of handover, the LTE specification provides the flexibility of using RSRP, RSRQ, or both.

Of course, it must to be measured over the same bandwidth:

	Narrow-band N = 62 Sub Carriers (6 Resource Blocks)
	Wide-band N = full bandwidth (up to 100 Resource Blocks / 20 MHz)

RSRP 3GPP Definition
	RSRP is the average received power of a single RS resource element
	UE measures the power of multiple resource elements used to transfer the reference signal but then takes an average of them rather than summing them.
	The reporting range of RSRP is defined from -140 dBm to – 44 dBm with 1 dB resolution. 
	RSRP does a better job of measuring signal power from a specific sector while potentially excluding noise and interference from other sectors
	RSRP levels for usable signal typically range from about -75 dBm close in to an LTE cell site to -120 dBm at the edge of LTE coverage.
Reference Signals recap: OFDMA Channel Estimation
In simple terms the Reference Signal (RS) is mapped to Resource Elements (RE). This mapping follows a specific pattern (see to below).
	So at any point in time the UE will measure all the REs that carry the RS and average the measurements to obtain an RSRP reading.
	Channel estimation in LTE is based on reference signals
	Reference signals position in time domain is fixed (0 and 4 for Type 1 Frame) whereas in frequency domain it depends on the Cell ID
	In case more than one antenna is used (e.g. MIMO) the Resource elements allocated to reference signals on one antenna are DTX on the other antennas
	Reference signals are modulated to identify the cell to which they belong
MORE INFO ABOUT OFDMA
 
 
RSSI (Received Signal Strength Indicator) is a parameter which provides information about total received wide-band power (measure in all symbols) including all interference and thermal noise. 
RSSI is not reported to e-NodeB by UE. 
RSSI = wideband power = noise + serving cell power + interference power
So, without noise and interference, we have that 100% DL PRB activity: RSSI=12*N*RSRP
Where: N, number of RBs across the RSSI

Based on the above, under full load and high SNR:
RSRP (dBm) = RSSI (dBm) – 10*log (12*N)
 
 
RSRQ 3GPP Definition
In formula:
 
Where:
	N is the number of Physical Resource Blocks (PRBs) over which the RSSI is measured, typically equal to system bandwidth
	The reporting range of RSRQ is defined from -3…-19.5dB

 

So we have that RSRQ depends on serving cell power and the number of Tx antennas E-UTRA – RSSI (Carrier Received Signal Strength Indicator), comprises the linear average of the total received power (in [W]) observed only in OFDM symbols containing reference symbols for antenna port, in the measurement bandwidth, over N number of resource blocks by the UE from all sources, including co-channel serving and non-serving cells, adjacent channel interference, thermal noise etc.

Impact of serving cell power to RSRQ:
Example for noise limited case (no interference): If all resource elements are active and are transmitted with equal power, then

	RSRQ = 10*log(N / 12N) = -10.8 dB for 1Tx
	RSRQ = 10*log(N / 20N )= -13 dB for 2Tx taking DTX into account

Remember that RSSI is only measured at those symbol times during which RS REs are transmitted – We do not have to take into the count DTx!!!

So, when there is no traffic, and assuming only the reference symbols are transmitted (there are 2 of them within the same symbol of a resource block) from a single Tx antenna then the RSSI is generated by only the 2 reference symbols so the result becomes

	RSRQ = N / 2N = -3 dB for 1Tx
	RSRQ = -6dB for 2Tx

SINR Definition

SINR is the reference value used in the system simulation and can be defined:
	Wide band SINR
	SINR for a specific sub-carriers (or for a specific resource elements)
 
All measured over the same bandwidth!
SNR vs. RSRP
RSRP is measured for a single subcarrier, noise power for 15KHz = -125.2dBm

 
	Noise figure = 7 dB
	Temperature = 290 K
Assumption: RSRP doesn’t contain noise power
 



Testbed setup
In this section, we first present the testbed system models. Then, we present steps to build UE, Cognitive BS (or eNB), EPC, and SDN-controller. 
Testbed system model
We setup a testbed model for a two-tier cognitive heterogeneous network consisting a single macrocell base station (MBS) and 03 cognitive base stations (BSs) are deployed to serve a set of mobile user equipments (UEs) as shown in Figure 3.3 and Table 3.1. The network resource allocation are controlled and managed by a SDN-controller. The sub-channels usage in cognitive BSs is utilized from subchannel usage of the MBS. We denote K is a set of sub-channels that cognitive BSs reuse from the MBS radio resources. The information of these sub-channels are observed and collected by the SDN-controller. Both the cognitive BS and UE are equipped with cognitive radio capacity. We assume that the sub-channels are allocated to each cognitive BS by SDN-controller, in which there is an existence of interference graph among cognitive BS. 
Table 3.1: Network entities in the testbed model
Network entity	Device name	Computer	Quantity
Cognitive base station (BS) or eNB	USRP-B210	Core-i5, 8Gb	03
Mobile UE using USRP-B210	USRP-B210	Core-i5, 8Gb	02
Commercial off-the-shelf (COSTs) UE	Samsung Galaxy S3-4-5		03
Mobility Management Entity (MME)	
EPC core 	
Core-i5, 16 Gb	
01
Home Subscriber Server (HSS)			
Serving-Gateway			
PDN GW-Packet Data Network Gateway			
 
Figure 3.3. Testbed system model
The data plan is built based on a standard-compliant implementation of a subset of Release 10 LTE for UE, Cognitive BS (eNB), and EPC (that is composed of the MME, HSS, SGw and PGw) on standard Linux-based computing equipment (Intel x86 PC/ARM architectures) as shown in Figure 3.1.  In this model, we make a connection of the OAI Cognitive BS (USRP B210)/EPC/HSS with COST UE and UE (USRP-B210) for the data plan. 
Reference: https://gitlab.eurecom.fr/oai/openairinterface5g/wikis/OpenAirUsage. 
We implement the 5g-EmPower in the testbed, where the controller, UE and Cognitive BS are running on separated computers. The HSS, MME, SGW, PGW, SDN-controller are integrated inside a unique computer (Core-i5, 16 Gb).  Each UE and Cognitive BS is formed from the combination of a pair (USRP-B210 device, computer (core i5, 08 Gb Ram)). The EPC core, SDN Controller, eNBs and UEs (USRP-B210s) are managed via a LAN network. Cognitive BSs or eNBs are connected to the MME via the S1 interface using LAN connection. UEs connect to the Cognitive BSs via the air-interface. UEs database information are stored at the HSS.  UEs’ IP address are allocated and managed by the PGW.  Testbed logical connection model is shown as in Figure 3.4.  
 
Figure 3.4. Logical connection model in our testbed
The OAI EPC/HSS, OAI cognitive BS, OAI UE, and COST UE implementation status
We have implemented the OAI EPC/HSS, OAI eNB and OAI UE installation using the S1 interface. This tested allowed the UE to connect to eNB and surfing Internet. We use 2 Ubuntu machines (EPC/HSS and eNB running in same host) or 3 Ubuntu machines (EPC/HSS and eNB running in separate host).
The procedures includes the following:
	Build and run the UE with NAS support in 1st Ubuntu machine.
	Build and run the eNB with S1 interface in 2nd Ubuntu machine.
	Build and run the EPC/HSS with S1 interface in 3rd Ubuntu machine
	Results
Remark : In our test-bed model, we utilize the frequency band 39 (1900 Mhz, 1880 Mhz -1920 MHz) from the macrocell network.  We setup a badwidth equal to 5Mhz. This band is devided into 25 resource blocks (RBs). These RBs are allocated to user equipment for both downlink and uplink transmittion. 
Installing, building and running the OAI UE (B210) with S1 interface 
To control that USRP device we need to install UHD driver. There are two types  of installing (building) UHD driver , binary installtion and building and installing UHD from source. In our project we are using UHD from source https://www.ettus.com/product/details/UB210-KIT
Step 1: OAI installation:
	Ubuntu 14.04 LTS (32-bit or 64-bit)
	Kernel setup
	Disable C-states from BIOS (or from GRUB)
	Disable CPU frequency scaling
	Install low-latency kerne
	Install subversion with command:
	sudo apt-get install subversion fo SVN version 
	 Install git with command : 
	sudo apt-get install git for GIT version
	  Install UHD driver for USRP Hardware B210 using the following commands:
	 sudo  bash -c 'echo "deb http://files.ettus.com/binaries/uhd/repo/uhd/ubuntu/`lsb_release -cs` `lsb_release -cs` main" > /etc/apt/sources.list.d/ettus.list'
	sudo apt-get install -t `lsb_release -cs` uhd
	sudo apt-get update 
Step 2: Installing UE with NAS Support (S1) on 1st Ubuntu Machine
Download the source codes using git (tested version r7772):                  
	mkdir -p ~/openairinterface5g
	git clone https://gitlab.eurecom.fr/oai/openairinterface5g.git
	git clone https://gitlab.eurecom.fr/oai/openair-cn.git
Remark : Make sure that the openair-cn inside the openairinterface5g folder.
Step 3: Run automated build script for UE with S1 interface 
Build the UE supporting B210:
	cd ~/openairinterface5g/cmake_targets./build_oai –w USRP –UE 
    This should starts the building process in ~/openairinterface5g/cmake_targets/lte_build_oai.
Reference: https://twiki.eurecom.fr/twiki/bin/view/OpenAirInterface/HowToConnectOAIENBWithOAI  
Step 4: Run UE on the Ubuntu Machine: 
 The command of running the UE should be as follow:
cd ~/openairinterface5g/
sudo ./targets/bin/init_nas_s1 UE
sudo -E ./targets/bin/lte-softmodem.Rel10 -U –C1910000000 -r25 --ue-scan-carrier --ue-txgain 70 --ue-rxgain 80 2>&1 | tee UE.log
Installing, building and running the OAI Cognitive BS (B210) with S1 interface 
Step 1: Installing the OAI as Step 1 of the UE installation. 
Step 2: Download the source codes using git
https://github.com/5g-empower/empower-openairinterface
Step 3: Build OAI for the Cognitive BS or eNB: 
cd ~/ empower-openairinterface
source oaienv
cd cmake_targets
./build_oai -I --eNB -x --install-system-files -w USRP       # for USRP
Then, make sure the networking parameters are properly specified in eNB and EPC configuration files. In eNB configuration file (~/openairinterface5g/targets/PROJECTS/GENERIC-LTE-EPC/CONF/enb.band7.tm1.usrpb210.conf),
tracking_area_code  =  "1";
mobile_country_code =  "208";
mobile_network_code =  "93";
////////// MME parameters:
    mme_ip_address      = ( { ipv4       = "192.168.100.10x"; // x = 1,2,3. Each x value corresponding to x-th Cognitive BS 
                              active     = "yes";
                              preference = "ipv4";
                            }
                          );
    NETWORK_INTERFACES :
    {
        ENB_INTERFACE_NAME_FOR_S1_MME         = "eth0";
        ENB_IPV4_ADDRESS_FOR_S1_MME           = "192.168.100.101/24";

        ENB_INTERFACE_NAME_FOR_S1U            = "eth0";
        ENB_IPV4_ADDRESS_FOR_S1U              = "192.168.100.101/24";
        ENB_PORT_FOR_S1U                      = 2152; # Spec 2152
    };
where mme_ip_address is network interface's IP address of your EPC/HSS, and NETWORK_INTERFACE is your eNB related network interface information.

Step 4:  Run Cognitive BS (or eNB) 
cd ~/openairinterface5g
source oaienv
./cmake_targets/build_oai -w USRP -x -c --eNB
cd cmake_targets/lte_build_oai/build
sudo -E ./lte-softmodem -O $OPENAIR_DIR/targets/PROJECTS/GENERIC-LTE-EPC/CONF/enb.band39.tm1.usrpb210.conf -d
Installing, building and running the EPC, HSS
Step 1: Installing the OAI as Step 1 of the UE installation. Then download openair-cn software. 
Step 2: Run automated script for openair-cn
cd openair-cn
git checkout develop 
git pull
cd SCRIPTS
./build_mme -i #(Need to run only once to install missing packages)
./build_hss -i #(Need to run only once to install missing packages)
./build_spgw -i #(Need to run only once to install missing packages)

Step 3: HSS, MME, SPG, and PGW configuration
Copy the EPC config files in /usr/local/etc/oai
sudo mkdir -p /usr/local/etc/oai/freeDiameter
sudo cp ~/openair-cn/ETC/mme.conf /usr/local/etc/oai
sudo cp ~/openair-cn/ETC/hss.conf /usr/local/etc/oai
sudo cp ~/openair-cn/ETC/spgw.conf /usr/local/etc/oai
sudo cp ~/openair-cn/ETC/acl.conf /usr/local/etc/oai/freeDiameter
sudo cp ~/openair-cn/ETC/mme_fd.conf /usr/local/etc/oai/freeDiameter
sudo cp ~/openair-cn/ETC/hss_fd.conf /usr/local/etc/oai/freeDiameter
In MME configuration file (/usr/local/etc/oai/mme.conf):
REALM = "openair4G.eur";
    S6A :
    {
        S6A_CONF                   = "/usr/local/etc/oai/freeDiameter/mme_fd.conf"; # YOUR MME freeDiameter config file path
        HSS_HOSTNAME               = "hss";                                         # THE HSS HOSTNAME
    };
GUMMEI_LIST = ( 
        {MCC="208" ; MNC="93"; MME_GID="4" ; MME_CODE="1"; }                   # YOUR GUMMEI CONFIG HERE
     );
TAI_LIST = (
{MCC="208" ; MNC="93";  TAC = "1"; }                              # YOUR PLMN CONFIG HERE
);
   NETWORK_INTERFACES :
    {
        # MME binded interface for S1-C or S1-MME  communication (S1AP), can be ethernet interface, virtual ethernet interface, we don't advise wireless interfaces
        MME_INTERFACE_NAME_FOR_S1_MME         = "eth0";                        # YOUR NETWORK CONFIG HERE
        MME_IPV4_ADDRESS_FOR_S1_MME           = "192.168.100.100/24";            # YOUR NETWORK CONFIG HERE
        # MME binded interface for S11 communication (GTPV2-C)
        MME_INTERFACE_NAME_FOR_S11_MME        = "lo";                          # YOUR NETWORK CONFIG HERE
        MME_IPV4_ADDRESS_FOR_S11_MME          = "127.0.11.1/8";                # YOUR NETWORK CONFIG HERE
        MME_PORT_FOR_S11_MME                  = 2123;                          # YOUR NETWORK CONFIG HERE
    };
S-GW :
{
    # S-GW binded interface for S11 communication (GTPV2-C), if none selected the ITTI message interface is used
SGW_IPV4_ADDRESS _FOR_S11           = "eth1";      
SGW_IPV4_ADDRESS_FOR_S11                = "127.0.11.1/24";            # YOUR NETWORK CONFIG HERE
};
In SPGW configuration file (/usr/local/etc/oai/spgw.conf):
S-GW :
{
    NETWORK_INTERFACES : 
    {
        # S-GW binded interface for S11 communication (GTPV2-C), if none selected the ITTI message interface is used
        SGW_INTERFACE_NAME_FOR_S11              = "lo";                        # YOUR NETWORK CONFIG HERE
        SGW_IPV4_ADDRESS_FOR_S11                = "127.0.11.2/8";              # YOUR NETWORK CONFIG HERE
        # S-GW binded interface for S1-U communication (GTPV1-U) can be ethernet interface, virtual ethernet interface, we don't advise wireless interfaces
        SGW_INTERFACE_NAME_FOR_S1U_S12_S4_UP    = "eth0";                       # YOUR NETWORK CONFIG HERE, USE "lo" if S-GW run on eNB host
        SGW_IPV4_ADDRESS_FOR_S1U_S12_S4_UP      = "192.168.100.100/24";           # YOUR NETWORK CONFIG HERE
        SGW_IPV4_PORT_FOR_S1U_S12_S4_UP         = 2152;                         # PREFER NOT CHANGE UNLESS YOU KNOW WHAT YOU ARE DOING
        # S-GW binded interface for S5 or S8 communication, not implemented, so leave it to none
        SGW_INTERFACE_NAME_FOR_S5_S8_UP         = "none";                       # DO NOT CHANGE (NOT IMPLEMENTED YET)
    };
}
P-GW =
{
    NETWORK_INTERFACES :
    {
        # P-GW binded interface for SGI (egress/ingress internet traffic)
        PGW_INTERFACE_NAME_FOR_SGI            = "eth0";                         # YOUR NETWORK CONFIG HERE
        PGW_IPV4_ADDRESS_FOR_SGI                = "163.180.140.75/24";            # YOUR NETWORK CONFIG HERE
        PGW_MASQUERADE_SGI                    = "yes";                          # YOUR NETWORK CONFIG HERE
       UE_TCP_MSS_CLAMPING                   = "no";                           # STRING, {"yes", "no"}.
    };
...
   # DNS address communicated to UEs
      DEFAULT_DNS_IPV4_ADDRESS     = "163.180.96.54/24";                            # YOUR NETWORK CONFIG HERE
...
}
In HSS freediameter configuration file (/usr/local/etc/oai/freeDiameter/hss_fd.conf):
Identity = "hss.openair4G.eur";
Realm = "openair4G.eur";
In MME freediameter configuration file (/usr/local/etc/oai/freeDiameter/mme_fd.conf):
Identity = "epc.openair4G.eur";
Realm = "openair4G.eur";
ConnectPeer= "hss.openair4G.eur" { ConnectTo = "127.0.0.1"; No_SCTP ; No_IPv6; Prefer_TCP; No_TLS; port = 3868;  realm = "openair4G.eur";};
In HSS configuration file (/usr/local/etc/oai/hss.conf):
MYSQL_user   = "root"; 
MYSQL_pass   = "hetnet1234"; #Put here the root password of mysql database that was provided during installation
OPERATOR_key = "1006020f0a478bf6b699f15c062e42b3"; # OP key for oai_db.sql, Must match to that of UE Sim card, OP_Key
Step 5:  Running EPC and HSS: 
	Compile & Run HSS (ALWAYS RUN HSS FIRST):
cd ~/openair-cn
cd SCRIPTS
./build_hss -c
./run_hss -i ~/openair-cn/SRC/OAI_HSS/db/oai_db.sql #Run only once to install database
./run_hss  #Run this for all subsequent runs
	Compile & Run MME:
cd ~/openair-cn/SCRIPTS
./build_mme -c
./run_mme
	Compile & Run SP-GW:
cd ~/openair-cn
cd SCRIPTS
./build_spgw -c
./run_spgw
UE, Cognitive BS, and EPC implementation status
We have implemented UE, Cognitive BS, HSS, MME, and SPGW in the testbed, where the controller, UE, and Cognitive BS are running on separated computers. 
Once the UE, eNB, and EPC are running, we achieved the results as follows: 
	A testbed model is built as shown in Figure 3.5
 
Figure 3.5. Test-bed connection model 
In this connection model, we run UE, eNB, and EPC using S1 interface. The results of SDN controller, HSS, MME, and SPGW are displayed at the left screen in Figure 3.5. The results of the cognitive BS are monitored at the middle screen.  UE information is displayed at  the right screen in Figure 3.5. 
	The UE is connected with the eNB via air interface as shown in Figure 3.6
 
Figure 3.6. Results at the UE of success UE attached to Cognitive BS or eNB

	The eNB is associated to the MME via S1 interface as shown in Figure 3.7. 

 
Figure 3.7 Results of Successful UE attached to eNB
The Figure 3.7 showed that the receiving of RRC Connection Reconfiguration Complete message from the UE and the UE state is moved to RRC_RECONFIGURED. 

	The MME, HSS, and SPGW results are shown in Figure 3.8.  
In figure 3.8, the MME associated to the HSS, the eNB associated to the MME.  
 

Figure 3.8. Connection status between MME, HSS, and SGPW

Development of the SDN-based architecture for controlling of the cognitive BSs and User Equipments
SDN controller in a Software Defined Network (SDN) plays a role of network brain, which acts as a strategic point of controlling and managing the network devices, applications, and business logic. In this subsection, we describe in details 5G-EmPOWER controller used as an SDN controller for cognitive BSs and User Equipment (UE) in our testbed and its implementation status.  
 5G-Empower controller solution for cognitive BSs and User Equipment (UE) 
  5G-EmPOWER (http://empower.create-net.org/ ) is an open source for SDN/NFV implemented in Linux operating system in order to deliver three main types of virtualize network resources, namely forwarding nodes, packet processing nodes and radio processing nodes.  In our testbed, we focus only on radio process node, where empower-openairinterface with the Empower agent is used at Cognitive BS/LTE eNodeB. 5G-EmPOWER architecture used in testbed is illustrated in Fig. 3.9 
 
Figure 3.9:  5G-EmPOWER architecture
The 5G-EmPOWER 0S controller interacts with 5G-EmPOWER agent installed at Cognitive BS. The 5G-EmPOWER agent provides the necessary callbacks that trigger certain event happening in the system, such as responding to the controller.  The interaction between 5G-EmPOWER agent and 5G-EmPOWER controller is described in below Fig. 3.10.
 
Figure 3.10: The interaction between Cognitive BS and 5G-EmPOWER controller
On controller side, the controller adds UE based on Cognitive BS ID and Radio Network Temporary Identifier (RNTI). However, each Cognitive BS manages all its attached User Equipment (UES), but the controller communicates with its VBS for configuration needs to be done in UE. 
The interaction between Cognitive BS and UE is described in below Fig. 3.11.
 
Figure 3.11:  The interaction between Cognitive BS and UE
Controller implementation status
We have implemented 5g-EmPower in the testbed, where the 5g-EmPower controller and 5g-EmPower agent are running on separated computers. 5g-EmPower implementation is designed as shown in Fig. 3.12. 
 
Fig. 3.12.  5g-EmPower implementation

The 5G-EMPOWER controller is installed on computer with IP 192.168.100.100 and run on port 2210, while the 5G-EMPOWER eNB agents are installed on computers with IP addresses 192.168.100.101 and 192.168.100.102.  
5g-EmPower controller is developed in python language, while 5g-EmPower controller is developed in C.  Therefore, the communication between both systems is based on Google Protocol buffers, which is a method of serializing structured data as shown in Figure 3.13. It helps the Controller and Agent to communicate with each other over network and exchange data. 
 
Fig. 3.13.  Data exchange between Cognitive BS Agent and 5G-EmPOWER controller
5G-EmPOWER implementation workflow is described as follows:
Step 1: Setting up 5G-EmPOWER controller
Hardware requirements:
PC running a recent Linux distribution (e.g. Ubuntu 16.10). There are no particular hardware requirements.
Required packages:
The following packages are required:
	python3-tornado (Version 4.4.2)
	python3-sqlalchemy (Version 1.0.8)
	python3-construct (Version 2.5.2)
	protobuf (Version 3.2.0)
	protobuf3-to-dict (Version 0.1.2)
                   The following commands are used to install the packages:
	sudo apt install python3-pip
	sudo pip3 install tornado sqlalchemy construct==2.5.2 protobuf protobuf3-to-dict 
Running the Controller:
The following commands are used for making controller running:
	git clone https://github.com/5g-empower/empower-runtime.git
	cd empower-runtime
	mkdir deploy
	./empower-runtime.py
Step 2: Setting up 5G-EmPOWER eNB agent 
Hardware requirements:
	For the machine running the eNB: A Quad core PC (i5 or better) with at least 8 GM RAM and running at least Ubuntu 14.04 LTS, and software defined radio platform (the Ettus USRP B210).
	For the machine running the EPC+MME+HSS: A Dual core PC (i5 or better) with at least 4 GM RAM and running Ubuntu 14.04 LTS.
Required packages:
The following packages are required:
	Protobuf and Protobuf-c libraries
                  The following commands are used to install the packages, update the packages    
                   cache, and install the standard Linux development tools:
	sudo apt-get update
	sudo apt-get install autoconf automake libtool curl make g++ unzip git
	wget https://github.com/google/protobuf/releases/download/v3.2.0/protobuf-cpp-3.2.0.tar.gz
	tar xvfz protobuf-cpp-3.2.0.tar.gz
	cd protobuf-3.2.0
Build and install the C++ Protocol Buffer runtime and the Protocol Buffer compiler:
The following commands are used:
	./configure
	make
	make check
	sudo make install
	sudo ldconfig
C implementation for the Google protocol buffer:
The following commands are used:
	wget https://github.com/protobuf-c/protobuf-c/releases/download/v1.2.1/protobuf-c-1.2.1.tar.gz
	tar xvfz protobuf-c-1.2.1.tar.gz
	cd protobuf-c-1.2.1
Compiling and Installing 5G-EmPOWER eNB agent:
The following commands are used:
	git clone https://github.com/5g-empower/empower-enb-agent.git
	cd empower-enb-agent/proto
	make
	sudo make install
	cd ../agent
	make
	sudo make install
Compilation/Configuration:
The following command is used:
	git clone https://github.com/5g-empower/empower-openairinterface.git .  For more information for building the OpenAirInterface that can be found  at    
https://gitlab.eurecom.fr/oai/openairinterface5g/wikis/HowToConnectCOTSUEwithOAIeNBNew
	The configuration file of EmPOWER eNB Agent agent.conf is in the /etc/empower directory, the IP address of the controller and port, which are 127.0.0.1 2210,  need to be included in configuration file.
Step 3: Preparing 5G-EmPOWER controller to communicate with eNB
Creating and modifying .proto files :
All communication between eNB and Controller use Google protocol buffer.  The message needs to be sent to eNB needs to be included in main.proto file as follows: 
message header {
        //Version of 1st level message.
        required uint32 vers = 1;
        required uint32 b_id = 2;
        required uint32 seq = 3;
        required uint32 t_id = 4;
        required double mUA=5;
        required double mPA=6;
        required double GRB1=7;
        required double GRB2=8;
        required double GRB3=9;
        required double GRB4=10;
        required double GRB5=11;
        required double td1=12; 
        required double td2=13; 
        required double td3=14; 
        required double td4=15; 
        required double td5=16; 
        required double td6=17; 
        required double td7=18; 
        required double td8=19; 
        required double td9=20; 
        required double td10=21;
        required double td11=22;
        required double td12=23;
        required double td13=24;
        required double td14=25;
        required double td15=26;
        required double td16=27;
        required double td17=28;
        required double td18=29;
        required double td19=30;
        required double td20=31;
}
Each field of message is designed to have unique index for facilitating serialization and deserialization of the message. Apart the main.proto file, there are other files needed, namely: hello.proto, statistics.proto, configs.proto and commands.proto
Compilation:
	The following command is used:
protoc --proto_path=proto --python_out=empower/vbsp/messages proto/hello.proto proto/main.proto proto/configs.proto proto/commands.proto proto/statistics.proto 
The above command will convert all the above .proto files (located inside the proto directory) into python files (.py) and post the files in empower/vbsp/messages directory 
Modifying vbspconnection:
	Some modifications need to be done at virtual base station directory located inside the empower directory, where vbspconnection.py file needs to be edited for having message header from main. proto
	In vbspconnection.py, create_header() needs to have all message header fields as the arguments. 
	In vbspconnection.py, serialize_message() function encodes the message that needs to be send to eNB through  Google protocol buffer,  while the function deserialize_message() is used to decode the message received from eNB
	The class VBSPConnection() is used to create socket, while stream_send() is used to send the stream of data. 
Step 4: Preparing to EmPOWER eNB Agent communicate with 5G-EmPOWER controller
Converting .proto files to .c files:
     The discussed above .proto files from controller need to be posted inside the   
     EmPOWER eNB Agent in proto 
     directory, where the following commands are used to convert .proto files 
     to .c files:
	./configure
	make
	make check
	sudo make install
	sudo ldconfig
Updating agent:
After converting .proto files to c. files, eNB agent needs to be updated in order to use these c. files, which are located in proto/pb directory.
The following files need to be updated in agent folder:
	agent.h and msg.c: the message heading fields need to be declared in these files and added to the header struct
	core. c and emage.h: em_start() and m_send() act as the entry point for starting the agent, and sending the message to the controller.
	int em_start(struct em_agent_ops * ops, int b_id, double mua, double mpa, double grb1, double grb2, double grb3, double grb4, double grb5, double td1, double td2, double td3, double td4, double td5, double td6, double td7, double td8, double td9, double td10, double td11,
		double td12, double td13, double td14, double td15, double td16,
		double td17, double td18, double td19, double td20) {}
	int em_send(int enb_id, double mua, double mpa, double grb1, double grb2, double grb3, double grb4, double grb5, double td1, double td2, double td3, double td4, double td5, double td6, double td7, double td8, double td9, double td10, double td11, double td12, double td13, double td14, double td15, double td16, double td17, double td18, double td19, double td20, EmageMsg * msg) {
After editing the above files, the following commands are used in agent directory to update the agent:
	./configure
	make
	sudo make install
Step 5: Modifying lte-softmodem and emage_tech_oai for empower-openairinterface
The lte-softmodem.c needs to be modified by including EmPOWER eNB Agent header files such as emage.h, net.h, emoai.h, and main.pb-c.h.  
	The net.h is linked to net.c in agent folder for unpacking the messages from controller and displaying them, through the use of Google protocol buffer
	emoai.h acts as an intermediate between empower-openairinterface and EmPOWER eNB Agent for exchanging the messages between eNB and controller. 
	main.pb-c.h is generated from .proto file and it includes all the message fields. 
	lte-softmodem.c needs to be modified as follows for receiving (pass_data_smodem function) and sending ( em_start function) the messages related to the actions need to be performed at the eNB: 
double td1=spectrum_sensing_grb1;
double td2=spectrum_sensing_grb2;
double td3=spectrum_sensing_grb3;
double td4=spectrum_sensing_grb4;
double td5=spectrum_sensing_grb5;
double td6=spectrum_sensing_grb5;
double td7=p_ue_rx1;
double td8=p_ue_rx2;
double td9=p_ue_rx3;
double td10=p_ue_rx4;
double td11=p_ue_rx5;
double td12=rsrp1;
double td13=rsrp2;
double td14=rsrp3;
double td15=rsrp4;
double td16=rsrp5;
double td17=0;
double td18=0;
double td19=0;
double td20=0;
double mua=1.0;
double mpa=2.5;
double grb1=58.0;
double grb2=58.0;
double grb3=58.0;
double grb4=45.5;
double grb5=12.0;
pass_data_smodem(HeaderVersion1,BaseStation_ID1, ControllerSequenceNumber1, vector_PA1, vector_UA1, vector_GRB1, vector_GRB2, vector_GRB3, vector_GRB4, vector_GRB5, m_RBA1[5][25], m_UA1[5], p_Tx1);
em_start(&sim_ops, enb_properties->properties[0]->eNB_id,mua, mpa, grb1, grb2,grb3,grb4,grb5, td1, td2, td3, td4, td5, td6, td7, td8, td9, td10, td11, td12, td13, td14, td15, td16, td17, td18, td19, td20);
printf("Check for eNB-3");
Inside emage_tech_oai directory, the following files need to be modified in order to include all the messages fields: emoai.c, emoai_common.c, emoai_common.h, emoai_rrc_measurements.c and emoai_rrc_measurements.h

Step 6: Modifying USRP B210 configuration file
	Each OAI soft eNB, where USRP B210 device are installed, needs to have unique ID. In our test bed, OAI soft  eNB_IDs are set to 0xe22, 0xe23 which are converted to 00:00:00:00:0E:22, 00:00:00:00:0E:23 as MAC addresses, and to 3618, 3619 as decimal OAI soft eNB IDs. 
The modification is done in enb.band39.tm1.usrpb210.conf, which is located in empower-openairinterface/tree/emage/targets/PROJECTS/GENERIC-LTE-EPC/CONF
Step 7:  Adding eNBs to the controllers 
The eNB_IDs needs to be added to the controller through web interface so that the controller can communicate to eNB, where the 5g-EmPower controller web interface can be reached via http:// 192.168.100.100:8888/  or http://163.180.140.75:8888/

 
Fig. 3.14.  5g-EmPower controller web interface
Step 8:  Running  5g-EmPower controller  and the eNB
	For running the controller the following command is used:
	./empower-runtime.py
Once controller starts, it establishes the communication with eNBs	 
Fig. 3.15 Connection establishment at 5g-EmPower controller
	For running the eNB the following commands are used:
	source oaienv
	./cmake_targets/build_oai -w USRP -x -c –eNB
	cd cmake_targets/lte_build_oai/build
	sudo -E ./lte-softmodem -O $OPENAIR_DIR/targets/PROJECTS/GENERIC-LTE-EPC/CONF/enb.band39.tm1.usrpb210.conf –d
Once eNB starts, it establishes the communication with 5g-EmPower controller
 
Fig. 4.16 Connection establishment at eNB
Source code for customizing 5g-Empower Agent in order to establish stable data exchange with controller, and improve data visualization. [Appendex 1]
The Google protocol buffer requires some interface description languages that describes the structure data and a program that generates source code by parsing a stream of bytes that represents the structured data. The following commands are used for installing Google protocol buffer:
At the Controller: See Appendex A
At the controller side, .proto file (main.proto) is converted Python file through the use of the following commands: See Appendex B
We modified OAI soft eNB sources codes for receiving and sending data as in Appendex C:
Protocol implementation and Test
In this section, we first develop the designed protocol, which is proposed in Section 2, for the joint user association and resource allocation in our test-bed. Then, we present the solutions to implement the proposed protocol. 
Protocol implementation status for the joint user association and resource allocation: 
The Efficient Self Organization Algorithm (EESA), which is proposed in section 2, consists of two main parts including User Association and Resource Allocation. In the start of this algorithm, SDN controller will build the conflicts which will be used by UE for association. After building the conflicts, UE starts user association. In our design, Conflict graphs, Reuse graphs, and UE utility are determined at the controller side given UE information sending to SDN controller. Following diagram shows the overall flow of EESA algorithm. 
 
Figure 3.17. Flow Chart of EESA Algorithm
The python code of this protocol is provided in Appendex D
User Association: 
In user association, the main task is learning and consolidation. Algorithm starts when a user equipment (UE) i gets traffic demand. After getting the traffic demand, learning process for appropriate user association starts.   
 
Figure 3.17. Flow Chart of Learning Function for choosing the configuration of User Association
Above flow chart shows the process of user association. Each user generates a random variable and move to new configuration with probability ω¬i and selects the current configuration with probability (1-ω¬i).  Here ω¬I is exploration probability.  The user association processing is run at the SDN controller. 
The python code of this protocol is provided in Appendex E
Consolidation: 
The consolidation process is next task performed after randomly choosing the configuration for each user with exploration probability ω¬i. In this process the previously chosen configurations are compared together on the basis of utility. The configuration with higher utility is selected probabilistically. Following figure explains the flow chart of consolidation process. 
 
Figure 3.18. Flow Chart of Consolidation Function for choosing the configuration with higher utility
The consolidation process is almost similar to the learning process with minor modification in terms of calculating the exploration probability. Exploration probability in consolidation process can be called transition probability. After calculating this probability using the utility values for each configuration, the appropriate configuration is selected for the user.  
From above description it is clear that the outcome of user association is selection of high utility configuration. This process is performed with the help of learning process and consolidation process.  
	The python code of this protocol is provided in Appendex F




Learning algorithm implementation: 

After the association process, each user sends its configuration information to the SDN controller for resource allocation. Following figure describes the process.  
 
Figure 3.19 Sharing Association information with SDN Controller for Resource Allocation 
In order to execute this algorithm, some modules are designed and implemented into the testbed system in the following session. 
Resource Allocation module in learning algorithm: 
After the association is done which consists of learning and consolidation process, UE stops the learning process and consolidation process. Now SDN controller will allocate the resources to every connection. UE will persist on the selected configuration while its request period is in progress. 
Functions developed for performing allocation: 
User Association and Resource Allocation is mainly performed with the help of some functions. Following sections shows the input parameters and outputs of these important functions. 
	Fun_ChoosProb
fun_Chooserob randomly chooses an action x (configuration or choice) depending on its probability p(x).

Input Parameters: 
	P	Probability vector p(x)
	X 	Action Vector 
Output: 
	F	Chosen Action 
	The python code of this protocol is provided in Appendex G

	Fun_Sigmoid
fun_Sigmoid calculates the probability (p_f) of a configuration (f) based on the utility or payoff (U_f).
Input Parameters: 
	Beta		Annealing Factor 
	U_f     		Utility vector [1 x nChoice]
Output: 
	p_f     		Probability vector [1 x nChoice]
 The python code of this protocol is provided in Appendex F

	Fun_SelfOrganize
fun_SelfOrganize performs the self organization via learning and consolidation.

Input Parameters: 
	F_v    		Vector of all feasible configurations
	U_v     		Utility corresonding to all feasible configurations
	f_t     		Historical vector of chosen configurations
	u_t     		Historical utilities of chosen configurations
	iExp    		Indicator showing Explored (1) / Unexplored (0)  status at previous timeslot
	pExp    		Exploration probability (learning rate)
	beta    		Annealing factor
Output: 
	f_t,
	u_t, 
	iExp
 The python code of this protocol is provided in Appendex E
Data communication protocol in learning algorithm: 
In order to run the Learning algorithm, some parameters have to exchange between UE-eNB, eNB and SDN Controller.  These procedures are addressed as below figure: 
 
                                      Figure 3.20. Data communication model in the Learning algorithm
	For the transmiting from UE side to controller, UE first measures information of the RSSI, RSVP, and RSRQ on each eNB. Then, these information is colleted and stored before coding and sending to the eNB. The transmission protocol between UE and eNB is established using TCP connection. We build it using socket in Python. 
	After receving data at the eNB side, eNB will collect data from all its UEs. Then, eNB perform coding data and send to the SDN controller via .proto protocol. 
	The feeback information from controller will send to eNB and UE agents to execute command from output of the Learning algorithm. 
In this session, in order to turn on UE device, we provide a function to control keeping online UE using script in Ubuntu as in shown in Appendix H
Programming code (See Appendixes): 
         Function sending information to eNB: See Appendix G
Decoding data at the eNB agent:  See Appendix K
Coding data at the eNB agent before sending to SDN controller: See Appendix L


Evaluation results: 
 
Figure 3.21. Evaluation model using Python
 
Figure 3.22. Evaluation RB allocation using Python
 
Figure 3.23. Evaluating the learning algorithm with Python

Analysis, design and test the control modules for resource block and power allocations in the UE and Cognitive BS

Analysis: 
 
Fig 3.24: Action Cycle of UE Agent
Phases::1: Collection 2: Sending 3: Returning 4: Update
	The process consists of three main building blocks: UE Agent / Cognitive BS agent and SDN controller
	UE and Cognitive BS agents acts as a facilitator between UE and SND controller,
	UE/Cognitive BS agent and SDN controller are able to exchange downlink frequency (DL_Freq), uplink frequency (UL_Freq), number of downlink resource block (N_RB_DL), and transmitter gain (Tx_gain), receiver gain (Rx_gain) etc. information with the help of UE agent. 
	Fig. 3.20 shows the communication among them. In the first phase, UE and Cognitive BS agents collect the above mentioned information from the UE. In the second phase, the agents send the information to the SDN controller for further processing. After getting the information about all agents, SDN controller runs the algorithm for optimized resource allocation and sends the output to the UE agent that is shown in the phase thee. The agents updates the information to the corresponding UE so that it can get optimized output and it is indicated in phase four. 
Resource block allocation design: 

Step (1):    Need SINR (or) CQI information from the user equipment (UE)
Step (2):     UE send downlink SINR value to eNB and then eNB agent send that information to SDN 
                     controller.
Step (3):      SDN controller will decide which modulation scheme will be used and how many resource 
                     blocks will be allocated to user . After that, controller sends that information to eNB.
Step (4):     Finally, eNB will allocate resource blocks to UE according to the information of controller.
Resource Allocation is the job of the MAC scheduler, and it starts from the function eNB_dlsch_schedular. It also calls schedule_ulsch and schedule_ue_spec. That is under ( openair2/LAYER2/Mac ) and we can know how eNB allocates resource blocks to users. However, we can’t modify simulation code there. Now, we are finding the file where we can modify the modulation, resource allocation to users according to controller’s Learning algorithm.
*** empower-openairinterface/ openair1/ simulation/ LTE_PHY/ dlsim.c where we can modify resource allocation .

Currently, we are working on customizing Empower-OpenairInterface to develop control modules based on C/C++ at the UE and Cognitive BS agents. The goals of these control modules are to control parameters such as transmit power and sub-channel at the UE and Cognitive BS side.  
Analysis, design and test the control module for user association. 
	
 
                      Fig 3.25: User association execution 








Reference
[1] http://www.openairinterface.org/
[2] www.3gpp.org/DynaReport/ 
[3] SeungJune Yi,  SungDuck Chun, YoungDae Lee,  SungJun Park and SungHoon Jung. “Radio Protocols for LTE and LTE-Advanced” 2012

