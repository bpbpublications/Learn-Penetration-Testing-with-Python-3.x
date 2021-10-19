#!/usr/bin/env python3
# TCP Port Scanner
#Author Yehia Elghaly

import threading
import socket

target = input('Enter the Target IP: ')
xx = 1 

def portscan(port):

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.5)#

    try:
        scan = s.connect((target,port))

        print('Port :',port,"Is Open.")

        scan.close()
    except:
        pass

for x in range(1,9000): 

    trea = threading.Thread(target=portscan,kwargs={'port':xx}) 
    xx += 1     
    trea.start() 