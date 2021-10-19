#!/usr/bin/env python3
# TCP SYN Ping
# Author Yehia Elghaly

from scapy.all import * 

ans,unans=sr( IP(dst="192.168.79.6")/TCP(dport=80,flags="A") )
ans.summary(lambda s_r: s_r[1].sprintf("%IP.src%, is Up"))