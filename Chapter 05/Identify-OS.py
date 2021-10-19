#!/usr/bin/env python3
# Identify OS on target machine
# Author Yehia Elghaly

from scapy.all import *

ans = input("Enter target IP? : ")

ip = IP()
ping = ICMP()
ip.dst = ans
replay = sr1(ip/ping)
if reply.ttl < 65:
	os = "Linux"
else:
	os = "Windows"

print ("Opreating System is: " + os)