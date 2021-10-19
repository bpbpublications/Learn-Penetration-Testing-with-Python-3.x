#!/usr/bin/env python3
# Scapy Port Scanner
# Author Yehia Elghaly

from scapy.all import *

target = input("Enter Target IP: ")

ans,unans=sr(IP(dst=target)/TCP(sport=RandShort(),dport=[22, 445, 80],flags="S"))
ans.summary( lfilter = lambda s_r: s_r[1].sprintf("%TCP.flags%") )