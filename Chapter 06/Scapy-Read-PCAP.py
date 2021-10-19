#!/usr/bin/env python3
# Read PCAP File
# Author Yehia Elghaly

from scapy.all import *

DNSPACK = rdpcap('test1.pcap')

for dpacket in DNSPACK:
    if dpacket.haslayer(DNSRR):
        if isinstance(dpacket.an, DNSRR):
            print(dpacket.an.rrname)