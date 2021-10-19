#!/usr/bin/env python3
# Packet DNS Sniffer
# Author Yehia Elghaly

from scapy.all import *

print ("DNS Sniffer")

while True:
	packets = sniff(filter="tcp[tcpflags] & (tcp-syn) !=0 or port 53", session=IPSession,
	 count=2, prn=lambda s_r: s_r[1].summary()) 