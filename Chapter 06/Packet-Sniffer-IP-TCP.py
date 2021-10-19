#!/usr/bin/env python3
# Packet Sniffer TCP/IP
# Author Yehia Elghaly

import socket
import struct
import textwrap
from colorama import Fore, Back, Style

def main():
    connection = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.ntohs(3))
    while True:
        read_data, addr = connection.recvfrom(65536)
        recv_mac, send_mac, eth_proto, packet_data = ethernet(read_data)

        print (Fore.RED + '********************Ethernet Header********************')
        print ('\tDestination MAC : {0}'.format(recv_mac))
        print ('\tSource MAC      : {0}'.format(send_mac))
        print ('\tProtocol        : {0}'.format(hex(eth_proto)))
        print ('*******************************************************')
        print ('')

        if eth_proto == 8:
            (version, header_length, ttl, protocol, src, target, packet_data) = ipv4_Packet(packet_data)
            print (Fore.GREEN + '=======================IP Header=======================')
            print ('\tVersion                : {0}'.format(version))
            print ('\tInternet Header Length : {0}'.format(header_length))
            print ('\tTime To Live           : {0}'.format(ttl))
            print ('\tProtocol               : {0}'.format(protocol))
            print ('\tSource Address         : {0}'.format(src))
            print ('\tDestination Address    : {0}'.format(target))
            print ('=======================================================')
            print ('')

            # TCP
            if protocol == 6:
                src_port, dest_port, sequence, acknowledgment, flag_urg, flag_ack, flag_psh, flag_rst, flag_syn, flag_fin = struct.unpack(
            '! H H L L H H H H H H', read_data[:24])
                print (Fore.CYAN + '####################TCP Header########################')
                print ('\tSource Port           : {0}'.format(src_port))
                print ('\tDestination Port      : {0}'.format(dest_port))
                print ('\tSequence number       : {0}'.format(sequence))
                print ('\tAcknowledgment Number : {0}'.format(acknowledgment))
                print ('Flags:')
                print ('\tUrg Flag              : {0}'.format(flag_urg))
                print ('\tAcknowledgment Number : {0}'.format(flag_ack))
                print ('\tPsh Flag              : {0}'.format(flag_psh))
                print ('\tRst Flag              : {0}'.format(flag_rst))
                print ('\tSyn Flag              : {0}'.format(flag_syn))
                print ('\tFin Flag              : {0}'.format(flag_fin))
                print ('######################################################')

        else:
            print('\nEthernet Data:')
            print((packet_data))

# Unpack Ethernet Frame
def ethernet(packet_data):
    recv_mac, send_mac, protocol = struct.unpack('! 6s 6s H', packet_data[:14])
    return read_mac_addr(recv_mac), read_mac_addr(send_mac), socket.htons(protocol), packet_data[14:]

    # Format MAC Address
def read_mac_addr(bytes):
    bytes_str = map('{:02x}'.format, bytes)
    mac_addr = ':'.join(bytes_str).upper()
    return mac_addr

# Unpack IPv4 Packets Recieved
def ipv4_Packet(packet_data):
    version_header_len = packet_data[0]
    version = version_header_len >> 4
    header_len = (version_header_len & 15) * 4
    ttl, protocol, src, target = struct.unpack('! 8x B B 2x 4s 4s', packet_data[:20])
    return version, header_len, ttl, protocol, ipv4(src), ipv4(target), packet_data[header_len:]

# Returns Formatted IP Address
def ipv4(addr):
    return '.'.join(map(str, addr))

# Unpacks for any TCP Packet
def tcp_seg(packet_data):
    (src_port, destination_port, sequence, acknowledgenment, offset_reserv_flag) = struct.unpack('! H H L L H', packet_data[:14])
    offset = (offset_reserv_flag >> 12) * 4
    flag_urg = (offset_reserved_flag & 32) >> 5
    flag_ack = (offset_reserved_flag & 16) >>4
    flag_psh = (offset_reserved_flag & 8) >> 3
    flag_rst = (offset_reserved_flag & 4) >> 2
    flag_syn = (offset_reserved_flag & 2) >> 1
    flag_fin = offset_reserved_flag & 1

    return src_port, dest_port, sequence, acknowledgement, flag_urg, flag_ack, flag_psh, flag_rst, flag_syn, flag_fin, packet_data[offset:]

main()