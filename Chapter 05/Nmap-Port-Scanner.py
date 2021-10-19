#!/usr/bin/env python3
# NMAP Port Scanner
# Yehia Elghaly

import nmap

addr = input("Enter Target Adresse: ")
print ("port range Ex: 20-443, or Single Port")
portrange = input("Enter port Range: ")
portt = nmap.PortScanner()
portt.scan(addr, portrange)
print(portt.command_line())

for host in portt.all_hosts():
	print ("")
	print('Scanning in progress')
	print('Target Host : {} ({})'.format(host, portt[host].hostname()))
	print('State : {}'.format(portt[host].state()))
	for proto in portt[host].all_protocols():
		print ("")
		print('************')
		print('Protocol  : {}'.format(proto))

		lport = portt[host][proto].keys()
		for port in lport:
			print ('port : {}\tstate : {}'.format(port, portt[host][proto][port]['state']))