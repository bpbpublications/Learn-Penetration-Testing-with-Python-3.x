#!/usr/bin/env python3
# Scan DNS Records
#Author Yehia Elghaly

import dns.resolver
from colorama import Fore, Back, Style 

print ("Example : google.com")
ans = input("Enter Doamin name: ")
answers = dns.resolver.query(ans, 'MX')
answers1 = dns.resolver.query(ans, 'A')
answers2 = dns.resolver.query(ans, 'AAAA')
answers3 = dns.resolver.query(ans, 'NS')
for rdata in answers:
    print ("")
    print (Fore.RED + "MX Rec")
    print ('Host', rdata.exchange, 'has preference', rdata.preference)
for radata in answers1:
    print ("")
    print (Fore.CYAN + "A Rec")
    print ('Host', rdata.exchange, 'has preference', rdata.preference)
for radata in answers2:
    print ("")
    print (Fore.YELLOW + "AAAA Rec")
    print ('Host', rdata.exchange, 'has preference', rdata.preference)
for radata in answers3:
    print ("")
    print (Fore.BLUE + "NS Rec")
    print ('Host', rdata.exchange, 'has preference', rdata.preference)