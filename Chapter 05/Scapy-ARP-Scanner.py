#!/usr/bin/env python3
# Scapy ARP Scanner
# Author Yehia Elghaly

from scapy.all import * 
import colorama
from colorama import Fore, Back, Style

target = input("Enter Target Range: ")

ans,unans = srp(Ether(dst="ff:ff:ff:ff:ff:ff")/ARP(pdst=target),timeout=2)
MM = (Fore.CYAN + "MAC: %Ether.src% ")
IP = (Fore.GREEN + "IP:%ARP.psrc%")
ans.summary(lambda s_r: s_r[1].sprintf(Fore.RED + "Live Hosts: " + MM + IP) )