#!/usr/bin/env python3
# Send Custom Sequence Number
#Author Yehia Elghaly

from scapy.all import *


target = input("Eenter Target IP: ")

def packet_seq():
    packet = IP(dst=target, src="192.168.0.115")/TCP(sport=333, dport=445, seq=112233)/"Sequence number 112233"
    send(packet)
    sendp(packet, iface="eth0")


packet_seq()