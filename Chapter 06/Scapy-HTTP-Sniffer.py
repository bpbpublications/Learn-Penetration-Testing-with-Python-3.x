#!/usr/bin/env python3
# Scapy HTTP Sniffer
# Author Yehia Elghaly

from scapy.all import *

def packet(packet):
    if packet[TCP].payload:
        if packet[IP].dport == 80:
            print("\n{} <SRC--HTTP--DST> {}:{}:\n{}".format(packet[IP].src, 
            	packet[IP].dst, packet[IP].dport, str(bytes(packet[TCP].payload))))

sniff(filter='tcp', prn=packet, store=0, count=0)