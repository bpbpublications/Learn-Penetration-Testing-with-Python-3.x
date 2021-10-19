#!/usr/bin/env python3
# Scan Wireless SSID's
# Author Yehia Elghaly

import pandas
from scapy.all import *
from threading import Thread
import time
import os

WIFIN = pandas.DataFrame(columns=["BSSID", "SSID", "Channel", "Encryption"])
WIFIN.set_index("BSSID", inplace=True)

def callback(packet):
	if packet.haslayer(Dpt11Beacon):
		bassid = packet[Dot11].addr2
		ssid = packet[Dot11Elt].info.decode()
		stats = packet[Dot11Beacon].network_stats()
		channel = stats.get("channel")
		Encryption = stats.get("Encryption")
		WIFIN.loc[bssid] = (ssid, channel, Encryption)

def OSS():
	while True:
		os.system("clear")
		print(WIFIN)
		time.sleep(0.5)

def change_hop():
	cc = 1
	while True:
		os.system(f"iwconfig {interface} channel {cc}")
		cc = cc % 12 + 1
		time.sleep(1.0)

if__name__ == "__main__":
interface = input (Fore.GREEN + "Enter interface Name:")
OSP = Thread(target=OSS)
OSP.daemon = True
OSP.start()
channel_hopy = Thread(target=change_hop)
channel_hopy.daemon = True
channel_hopy.start()
sniff(prn=callback, iface=interface)