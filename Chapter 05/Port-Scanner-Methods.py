#!/usr/bin/env python3
# Nmap Port Scanner Using Different Methods
# Author Yehia Elghaly

import nmap
from colorama import Fore, Back, Style
import time
from time import sleep


scanner = nmap.PortScanner()

print ("Custom Automated Nmap Script")

ip_addr = input("Enter Target Host: ")
portrange = input("Enter Port Range: ")

resp = input ("""\nSelect Scan Method:
	              1) SYN Scan
	              2) UDP Scan
	              3) Custom Scan \n""")

print ("You have selected option: ", resp)

from tqdm import *
print ("")
print (Fore.CYAN + "Scanning in Progress")
print ("")
for i in tqdm(range(4)):
	time.sleep(1)

print ("")

while True:
	if resp == '1':

		scanner.scan(ip_addr, portrange, '-vvv -sS -T4')
		print (Fore.RED + 'Info: ', scanner.scaninfo())
		print ("IP Status: ", scanner[ip_addr].state())
		for proto in scanner[ip_addr].all_protocols():
			print ("")
			print('******************************')
			print('Protocol  : {}'.format(proto))
			lport = scanner[ip_addr][proto].keys()
			for port in lport:
				print (Fore.GREEN + 'port : {}\tstate : {}'.format(port, scanner[ip_addr][proto][port]['state']))



	elif resp == '2':
		scanner.scan(ip_addr, portrange, '-vvv -sU -T4')
		print (Fore.RED + 'Info: ', scanner.scaninfo())
		print ("IP Status: ", scanner[ip_addr].state())
		for proto in scanner[ip_addr].all_protocols():
			print ("")
			print('******************************')
			print('Protocol  : {}'.format(proto))
			lport = scanner[ip_addr][proto].keys()
			for port in lport:
				print (Fore.GREEN + 'port : {}\tstate : {}'.format(port, scanner[ip_addr][proto][port]['state']))


	elif resp == '3':
		scanner.scan(ip_addr, portrange, '-vvv -sW -ff  -T4')
		print (Fore.RED + 'Info: ', scanner.scaninfo())
		print ("IP Status: ", scanner[ip_addr].state())
		for proto in scanner[ip_addr].all_protocols():
			print ("")
			print('******************************')
			print('Protocol  : {}'.format(proto))
			lport = scanner[ip_addr][proto].keys()
			for port in lport:
				print (Fore.GREEN + 'port : {}\tstate : {}'.format(port, scanner[ip_addr][proto][port]['state']))