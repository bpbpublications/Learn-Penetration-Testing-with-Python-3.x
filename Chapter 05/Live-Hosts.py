#!/usr/bin/env python3
# Identify Live Hosts
# Author Yehia Elghaly

import sys
from scapy.all import *

print("pinging the target host....")
target = sys.argv[1]
icmp = IP(dst=target)/ICMP()

recv = sr1(icmp,timeout=10)
if recv == None:
    print("This host is down")
else:
    print("This host is up")