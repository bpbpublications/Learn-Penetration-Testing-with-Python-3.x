#!/usr/bin/env python3
# Malicious Connection Detection
# Author Yehia Elghaly

from scapy.all import *
from colorama import init, Fore

network_inter = "eth0"

def ip_packet(packet):
    ip_deep = packet.getlayer(IP)
    print(Fore.GREEN + "[!] New Packet: {src} -> {dst}".format(src=ip_deep.src, dst=ip_deep.dst))
    if ip_deep.dst == "172.217.19.4":
        print (Fore.RED + "Malicious Connection ==> " + ip_deep.dst)
    else:
        pass

print("[*] sniffing Started...")
sniff(iface=network_inter, filter="ip", prn=ip_packet)
print("[*] sniffing Stoped")