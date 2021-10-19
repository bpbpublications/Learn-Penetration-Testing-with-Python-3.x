#!/usr/bin/env python3
# Scan for Live IP's
#Author Yehia Elghaly

import socket
import os
from colorama import Fore, Back, Style 

URM = input("Name of hosts file  ")

hostsFile = open(URM, "r")
hostsFile = hostsFile.readlines()

for ip in hostsFile:
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	rep = os.system('ping -c 1 ' + ip)
	if rep == 0:
		print ("")
		print (Fore.GREEN + 'Host is Online')
		print ("")
	else:
		print (Fore.RED + 'Host is Offline')