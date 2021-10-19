#!/usr/bin/env python3
# UDP Ping
# Author Yehia Elghaly 

from scapy.all import * 

ans, unans = sr( IP(dst="192.168.*.100-128")/UDP(dport=1) )
ans.summary(lambda s_r: s_r[1].sprintf("%IP.src% is UP") )