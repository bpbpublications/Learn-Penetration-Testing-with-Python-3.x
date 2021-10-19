#!/usr/bin/env python3
# Scan for Live IP's
#Author Yehia Elghaly

import sh    
from colorama import Fore, Back, Style 

for octt in range(106,112):  
    target = "192.168.0."+str(octt)  
  
    try:  
        sh.ping(target, "-c 1",_out="/dev/null")  
        print (Fore.GREEN + "PING ",target , "Live")
    except sh.ErrorReturnCode_1:  
        print (Fore.RED + "PING ", target, "Dead")