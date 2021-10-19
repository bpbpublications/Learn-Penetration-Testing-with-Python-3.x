#!/usr/bin/env python3
# Packet MAC Sniffer
# Author Yehia Elghaly

import socket
import textwrap
import struct
from colorama import Fore, Back, Style

def main():
	connection = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.ntohs(3))
	while True:
		read_data, addr = connection.recvfrom(65536)
		send_mac, recv_mac, protocol, packet_data = ethernet(read_data)
		print ('\nEthernet Data:')
		print (Fore.GREEN + 'Destination: {}, Source: {}, Protocol: {}'. format (send_mac, recv_mac, protocol))

def ethernet(packet_data):
	send_mac, recv_mac, protocol = struct.unpack('!6s 6s H', packet_data[:14])
	return read_mac_addr(send_mac), read_mac_addr(recv_mac), socket.htons(protocol), packet_data[:14]

def read_mac_addr(bytes):
	bytes_s = map('{:02x}'.format, bytes)
	return  ':'.join(bytes_s).upper() 

main()