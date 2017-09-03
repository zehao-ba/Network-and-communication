# Network-and-communication
From this course, I had a basic comprehensive in the field of computer networks and communications. 
It shows throught a system approach to networks by examing the hardware and protocol components that comprise a network.
The course also examines the interactions and interdependencies between protocols. 
Topics covered in this course include network principles and concepts, transmission principles, network architecture, 
routers and routing protocols, direct link networks, wireless networks, internetworking, and emerging network technologies.

### Assignment 1: 
1. Experimental study of traceroute;
2. Research question: The Center for Applied Internet Data Analysis (CAIDA) (www.caida.org) conducts a number of research studies and projects in the areas of Internet topology, Internet traffic measurements, security, routing, etc. Visit their website and investigate one research area or project or tool. Summarize its goals, methodology, and some of their results.
3. Short snappers: Bandwidth delay problems.
4. Suppose two hosts, A and B, are separated by 20,000 kilometers and are connected by a direct link of R = 2 Mbps. Suppose the propagation speed over the link is 2.5*108 meters/sec. Consider sending a file of 800,000 bits from Host A to Host B. Suppose the file is sent continuously as one big message. How long does it take to send the file? Suppose now the file is broken up into 20 packets each with each packet containing 40,000 bits.Suppose the receiver acknowledges each packet and the transmission time of an acknowledgement packet is 100 ms. Finally, assume that the sender cannot send a packet until the preceding one is acknowledged. How long does it take to send the file?
5. Calculate the total time required to transfer a 1.5 MB file in the following cases, assuming RTT of 80ms, a packet size of 1KB and an initial 2XRTT of “handshaking” before it is sent.
a) The b/w is 10Mbps, and the data packets can be sent continuously.<br>
b) The b/w is 10Mbps, but after we finish sending each data packet, we must wait one RTT before sending the next. <br>
c) The link allows infinitely fast transmits, but limits bandwidth such that only 20 packets can be sent per RTT zero transmit time as in (c), but during the first RTT, we can send one packet during the 2nd RTT we can send 2 packets, during the 3rs we can send 4 = 23-1 and so on.<br>
6. Short snapper: Addressing problem: The following figure depicts an internetwork. The IP and the MAC addresses of the significant interfaces are shown. An FTP connection is set up from S to D (S is the client and D is the server) and a SSH connection is set up from D to S (D is the client and S is the server). Write the formats of the following message entities, showing the port addresses, IP addresses and MAC addresses using the format:

|Source MAC address|Destination MAC address|Source IP address|Destination IP address|Source port address|Destination port address|
| ------------- | ------------- | ------------- | ------------- | ------------- | ------------- |

      a. Frame on Token Ring1 – FTP message from S to D. <br>
      b. Frame on FDDI – FTP message from S to D. <br>
      c. Frame on Token Ring 2 – FTP message from S to D. <br>
      d. Frame on Ethernet – FTP message from S to D. <br>
      e. Frame on Token Ring 1 – FTP message from D to S. <br>
      f. Frame on FDDI – FTP message from D to S. <br>
      g. Frame on Token Ring 2 – FTP message from D to S. <br>
      h. Frame on FDDI – SSH message from S to D. <br>
      i. Frame on Token Ring 2 – SSH message from S to D. <br>
      j. Frame on Ethernet – SSH message from S to D. <br>
      k. Frame on Token Ring 1 – SSH message from D to S. <br>
      l. Frame on FDDI – SSH message from D to S. <br>

### Assignment 2: 
1. Experimental study with Wireshark;

### Assignment 3:
1. Write a simple program to simulate the bridge processing flowchart discussed in the lectures. The program should read a text file that contains the forwarding database (FDB). The first line in the text file contains the number of ports on the bridge. The program should then read another text file containing randomly generate frames – just the source and destination numbers and port numbers of arrival. For each frame, the program should use the flowchart to make an update of the forwarding database and/or to forward/discard the frame. Ignore the CRC error detection part (that is, assume that the frames are error free). Include the source code and sample runs of the program.<br>
As a simple example, the text file containing the FDB and port numbers could look like this:<br>
|4| |
| ------------- | ------------- | 
|A|1|
|B|1|
|C|1|
|D|2|
|E|3|
|F|3|
|X|3|
In the above example, the bridge has four ports (1, 2, 3 and 4) and the current FDB has 7 entries. (Port no.4 has not yet received any frame and hence there is no entry for port no. 4).<br>
The second text file could be like this:<br>
|A|B|1|
| ------------- | ------------- | ------------- | 
|X|B|3|
|A|M|1|
|X|M|4|
|Etc.| | |
The first line means that the frame has source address A and destination address B and arrives at port 1 of the bridge. In this case, the frame should be discarded by the bridge. <br>
The output would look something like this:<br>
|A|B|1|Frame discarded|
| ------------- | ------------- | ------------- | ------------- | 
|X|B|3|Frame sent on port 1|
|A|M|1|Frame broadcast on all out ports|
|X|M|4|FDB updated; Frame sent on port 3|
|Etc.| | | |

